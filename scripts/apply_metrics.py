#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把 `data/metrics.json` 的數字套用到各顯示面，或驗證它們沒有漂移。

    python scripts/apply_metrics.py           寫回各顯示面
    python scripts/apply_metrics.py --check    只驗證，不寫（CI 用；不一致即 exit 1）

為什麼需要這支：同一個數字在 index.html、projects/*.md、面試素材裡各寫一份，
改了其中一處而漏掉其他處時，**沒有任何東西會叫**。2026-08-13 實際踩到——
同一個測試數在三個地方是 2,601／2,603／2,635，而三個都不是實跑值（2,650）。

做法是「標記替換」而不是全文生成：顯示面的文案由人維護，只有**數字本身**
被機器管。整段生成會讓文案改動變成產物衝突，那比數字漂移更難用。

    <!--m:key-->舊值<!--/m-->        Markdown 與 HTML 共用同一種標記

@author gabrielchen
@version 1.0
@since portfolio 1.0
@date 2026.08.13
"""

import argparse
import json
import re
import sys
from pathlib import Path


# region 常數定義

REPO_ROOT: Path = Path( __file__ ).resolve().parent.parent
METRICS_PATH: Path = REPO_ROOT / "data" / "metrics.json"

## 會被掃描與寫回的顯示面。新增顯示面要加進來，否則它不會被管。
DISPLAY_FILES: tuple = ( "index.html", "README.md", "projects/README.md",
                         "projects/01-ai-memory-vault.md",
                         "projects/02-remote-ai-task-platform.md",
                         "projects/04-jarvis-core-and-dashboard.md",
                         "projects/07-team-adoption-path.md" )

MARK_PATTERN: re.Pattern = re.compile( r"<!--m:([a-z0-9_.]+)-->(.*?)<!--/m-->", re.S )

EXIT_OK: int = 0
EXIT_DRIFT: int = 1

# endregion


def load_metrics() -> dict:
    """
    載入單一真實來源並攤平成 "區塊.鍵" → 值。

    :return: { "ai_memory_vault.tests_passed": 2650, ... }
    :raises SystemExit: metrics.json 不存在時中止——缺來源不是「用預設值繼續」
    """
    if( not METRICS_PATH.exists() ):
        sys.stderr.write( "[apply_metrics] 找不到 %s\n" % METRICS_PATH )
        raise SystemExit( 2 )

    # utf-8-sig 而非 utf-8：Windows 的編輯器與 PowerShell 的 Set-Content 會加 BOM，
    # 而帶 BOM 的 JSON 用 utf-8 解析會直接炸。這裡容忍它，而不是要求每個人記得別加。
    _Raw = json.loads( METRICS_PATH.read_text( encoding="utf-8-sig" ) )
    _Dic_Flat: dict = {}

    for _Section, _Fields in _Raw.items():
        if( _Section.startswith( "_" ) or not isinstance( _Fields, dict ) ):
            continue
        for _Name, _Entry in _Fields.items():
            _Dic_Flat[ "%s.%s" % ( _Section, _Name ) ] = _Entry[ "value" ]

    return _Dic_Flat


def format_value( iValue ) -> str:
    """
    把值格式化成顯示用字串。

    整數加千分位（2650 → 2,650），浮點保留三位（0.69 → 0.690），其餘原樣。

    :param iValue: 來源值
    :return: 顯示字串
    """
    if( isinstance( iValue, bool ) ):
        return str( iValue )
    if( isinstance( iValue, int ) ):
        return "{:,}".format( iValue )
    if( isinstance( iValue, float ) ):
        return "%.3f" % iValue
    return str( iValue )


def process_file( iPath: Path, iDic_Metrics: dict, iIsCheckOnly: bool ) -> list:
    """
    處理單一顯示面。

    :param iPath: 檔案路徑
    :param iDic_Metrics: 攤平後的指標
    :param iIsCheckOnly: True 只比對不寫回
    :return: 漂移清單（每項為說明字串）
    """
    _Text = iPath.read_text( encoding="utf-8" )
    _List_Drift: list = []
    _List_Unknown: list = []

    def _replace( iMatch: re.Match ) -> str:
        _Key = iMatch.group( 1 )
        _Current = iMatch.group( 2 )

        if( _Key not in iDic_Metrics ):
            _List_Unknown.append( _Key )
            return iMatch.group( 0 )

        _Expected = format_value( iDic_Metrics[ _Key ] )
        if( _Current != _Expected ):
            _List_Drift.append( "%s：%s → %s（%s）"
                                % ( iPath.relative_to( REPO_ROOT ), _Current, _Expected, _Key ) )
        return "<!--m:%s-->%s<!--/m-->" % ( _Key, _Expected )

    _New = MARK_PATTERN.sub( _replace, _Text )

    for _Key in _List_Unknown:
        _List_Drift.append( "%s：標記 %s 在 metrics.json 裡不存在"
                            % ( iPath.relative_to( REPO_ROOT ), _Key ) )

    if( not iIsCheckOnly and _New != _Text ):
        iPath.write_text( _New, encoding="utf-8" )

    return _List_Drift


def main() -> int:
    """
    進入點。

    :return: 0 一致 / 1 有漂移 / 2 來源缺席
    """
    sys.stdout.reconfigure( encoding="utf-8" )

    _Parser = argparse.ArgumentParser( description="套用或驗證作品集數字" )
    _Parser.add_argument( "--check", action="store_true", help="只驗證不寫回（CI 用）" )
    _Args = _Parser.parse_args()

    _Dic_Metrics = load_metrics()
    _List_AllDrift: list = []
    _MarkCount = 0

    for _Rel in DISPLAY_FILES:
        _Path = REPO_ROOT / _Rel
        if( not _Path.exists() ):
            continue
        _MarkCount += len( MARK_PATTERN.findall( _Path.read_text( encoding="utf-8" ) ) )
        _List_AllDrift.extend( process_file( _Path, _Dic_Metrics, _Args.check ) )

    print( "指標 %d 項，顯示面標記 %d 處" % ( len( _Dic_Metrics ), _MarkCount ) )

    if( _List_AllDrift ):
        print( "\n%s %d 處：" % ( "偵測到漂移" if( _Args.check ) else "已更新", len( _List_AllDrift ) ) )
        for _Item in _List_AllDrift:
            print( "  %s" % _Item )
        return EXIT_DRIFT if( _Args.check ) else EXIT_OK

    print( "全部一致。" )
    return EXIT_OK


if( __name__ == "__main__" ):
    raise SystemExit( main() )
