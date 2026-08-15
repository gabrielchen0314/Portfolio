# 工程作品集

> 這裡放的不是履歷，是**證據**。
> 每個結論後面都掛著一次實際踩過的坑、一組跑得出來的數字，或一份被同儕審查推翻過的判斷。

---

## 一分鐘版本

過去半年獨立設計並交付了一組互相咬合的 AI 工程系統。

**這組系統由我一個人開發，但機制全部照團隊規格。**契約邊界、code review、五段稽核鏈、
機器強制的閘門，它們存在的理由都是同一句話：**不要依賴任何人記得**。
這是職務上的工作標準，不會因為某個專案只有我一個人寫就放掉。
也因為是契約驅動，從個人擴展到團隊共用不是重寫，是新增一個消費端。

```
Vault / AI Engine        知識層：RAG 檢索 + MCP 工具面 + 記憶注入
      ↓ 契約（JSON Schema，語言中立）
jarvis-core              薄核心：只產出決策，不執行、不投遞（≤1500 LOC 機器強制）
      ↓ 契約
RATP                     執行層：低權限帳號、五段稽核、fail-closed 安全邊界
      ↓ 契約
jarvis-dashboard         觀測層：有 UI 沒權限（結構上無法旁路）
```

---

## 可以自己跑的一個

下面的專案卷是**敘述**，讀者只能選擇相信或不相信。所以我另外開了一個小 repo，
把其中一塊做成**可以 clone、五分鐘跑完、看得到數字**的東西：

### 🔬 [hybrid-retrieval-demo](https://github.com/gabrielchen0314/hybrid-retrieval-demo)

BM25 與向量檢索的加權 RRF 融合、有界時間衰減重排，以及一個超出預算時
**會發出聲音而不是靜默截斷**的注入預算契約。語料全部合成，零私人內容。

| | recall@5 | MRR@10 |
|---|---|---|
| 單模式基準（取較好者） | 0.800 | 0.615 |
| **hybrid** | **0.867** | **0.638** |

它要證明的不是「我會寫 RAG」，是**每個參數都是量出來的**：360 格參數網格全掃、
149 格勝出、選定組態由 `sweep.json` 回推，而不是手寫在 README 上。
另有 12 道機器閘門，包含一條**突變驗證**（把產生指標的邏輯拿掉，斷言必須變紅）。

```bash
git clone https://github.com/gabrielchen0314/hybrid-retrieval-demo
pip install -r requirements.txt && python scripts/eval.py
```

從乾淨 clone 跑出來的 `results.json` 跟上表**逐位元相同**。這是刻意設計的：
評估時點是版控裡的固定日期，程式中禁用牆上時鐘，由靜態掃描擋。

---

## 專案卷

### 自主發起（以個人時間與設備開發）

| # | 專案 | 技術棧 | 一句話 |
|---|---|---|---|
| [01](projects/01-ai-memory-vault.md) | **AI Memory Vault** | Python · ChromaDB · MCP · PyInstaller | 個人知識庫的 RAG 後端，25 個 MCP 工具，四種部署形態 |
| [02](projects/02-remote-ai-task-platform.md) | **Remote AI Task Platform** | Python · SQLite · Discord | 讓 AI CLI 以低權限帳號在背景安全執行任務 |
| [04](projects/04-jarvis-core-and-dashboard.md) | **Jarvis Core / Dashboard** | Python · TypeScript · JSON Schema | 契約驅動的薄核心 + 零建置觀測面板 |

延伸：[07 · AI Memory Vault 從個人到團隊的落地路徑](projects/07-team-adoption-path.md)

### 需求來自職務現場

這三項的共同點是需求不是我想出來的，是工作現場長出來的。於此記錄的是技術問題與解法，
不是所有權主張，歸屬逐項標註。三篇都已去識別化，不含僱主、專案代號、內部系統與路徑。

| # | 專案 | 技術棧 | 一句話 | 歸屬 |
|---|---|---|---|---|
| [03](projects/03-window-computer-use.md) | **Window Computer Use** | C# · .NET 8 · UIA · WGC | 鎖定單一視窗的 Computer Use，不碰你的滑鼠鍵盤 | 個人時間與設備；依職務發明條款認定 |
| [05](projects/05-legacy-toolchain-modernization.md) | **Legacy 工具鏈現代化** | TypeScript · C++ · DAP | 20 年前的建置鏈，接上今天的 IDE 與 AI | 職務中開發，著作權屬雇主 |
| [06](projects/06-ai-enablement.md) | **團隊 AI 導入** | — | 帶零基礎團隊從 0 開始用 AI，通關制而非期程制 | 職務中開發，教材著作權屬雇主 |

每份文件的結構固定：**解什麼問題 → 架構 → 難題與解法 → 成果**。
「難題與解法」是重點，其他章節是為了讓那一節有脈絡。

完整索引與跨專案主題見 [`projects/README.md`](projects/README.md)。

---

## 貫穿三個專案以上的主題

1. **沉默的失敗** — 機制存在、掛在錯的地方、而失敗不會叫。這是踩過最多次的形狀
2. **驗證的方向性** — 「測試綠」不等於「機制正確」，「改完」不等於「改對」
3. **安全預設的方向** — 一個預設是開的安全開關不是開關，是裝飾

---

## 關於數據

文件裡出現的測試數、版本號、時間、位元組數，都是**當時實際跑出來的值**，不是估計。
會過時，但不會是編的。過時的地方會標註量測日期。

---

## 目錄

| 路徑 | 內容 |
|---|---|
| [`projects/`](projects/) | 專案卷 7 篇，每篇「解什麼問題 → 架構 → 難題與解法 → 成果」 |
| [`index.html`](index.html) | 線上履歷的來源檔，發布於 <https://gabrielchen0314.github.io/Portfolio/> |
| [`PUBLISHING.md`](PUBLISHING.md) | 發布方式與「唯一來源」原則 |

---

## 這個 repo 沒有放的東西

**知識卷**（12 篇技術知識點的學習版）與**面試素材**不在這裡，
它們住在個人知識庫，是寫給自己的持續演化材料。

這條界線是這樣劃的：

| | 讀者 | 內容 |
|---|---|---|
| **這個 repo** | 別人 | 我做了什麼、遇到什麼難題、怎麼解的、數字是多少 |
| 個人知識庫 | 我自己 | 那些東西怎麼講、對方會追問什麼、哪句先出口 |

技術細節本來就是要給人看的；但「怎麼把它講出來」是準備稿，公開等於把腳本先交出去。

**專案卷已去識別化**：不含專案代號、內部系統、工單與機器路徑。
履歷頁（`index.html`）載明任職公司，那是履歷的必要欄位，不是漏掉的去識別化。
