# 專案卷

> 每份文件的結構固定：**解什麼問題 → 架構 → 難題與解法 → 成果 → 面試怎麼講**。
> 「難題與解法」是重點，其他章節是為了讓那一節有脈絡。

---

## 索引

### 自主發起（以個人時間與設備開發）

| # | 專案 | 期間 | 技術棧 | 規模 |
|---|---|---|---|---|
| [01](01-ai-memory-vault.md) | AI Memory Vault | 2026-04 ~ 進行中 | Python 3.12 · ChromaDB · LangChain · FastMCP · PyInstaller · Tauri | 2,397 tests · 25 MCP tools · v4.2.x |
| [02](02-remote-ai-task-platform.md) | Remote AI Task Platform | 2026-07 ~ 進行中 | Python · SQLite(WAL) · Discord.py · Windows API | 528 tests · Phase 1B 完成 |
| [04](04-jarvis-core-and-dashboard.md) | Jarvis Core / Dashboard | 2026-07 ~ 維持 | Python · TypeScript(Node 原生) · JSON Schema | 135 + 87 tests · kernel ≤1500 LOC |
| [07](07-team-adoption-path.md) | AI Memory Vault 帶進團隊的落地路徑 | — | 設計推導 | 三個缺口 · 三個風險 |

### ⚖️ 為工作場景開發（需求來自職務現場）

於此記錄的是技術問題與解法，**不是所有權主張**；歸屬各不相同，逐項標註。內容已去識別化。

| # | 專案 | 期間 | 技術棧 | 規模 | 歸屬 |
|---|---|---|---|---|---|
| [03](03-window-computer-use.md) | Window Computer Use | 2026-07 ~ 凍結 | C# · .NET 8 · UI Automation · Windows Graphics Capture | ~10,300 LOC · 14 MCP tools | 個人時間與設備；依職務發明條款認定 |
| [05](05-legacy-toolchain-modernization.md) | Legacy 建置鏈現代化 | 2026-05 ~ | TypeScript · C++ · DAP · VS Code Extension API | VS2003 + UE2 全鏈打通 | 職務中開發，屬雇主 |
| [06](06-ai-enablement.md) | 團隊 AI 能力養成 | 2026-07 ~ | — | 六階段通關制 · 講義可直接開課 | 職務中開發，屬雇主 |

---

## 一句話定位（面試用）

**01 · AI Memory Vault**
> 我做了一個把個人知識庫變成 AI 長期記憶的 RAG 後端。它不只是「能搜」——真正難的是**讓 AI 每次進場都自動拿到對的脈絡**，而且在四種部署形態下行為一致。

**02 · Remote AI Task Platform**
> 我想讓 AI CLI 能在我不在電腦前的時候幫我做事。這件事的核心不是「跑起來」，是**在什麼都能出錯的前提下，讓每一步都留下可稽核的痕跡**。

**03 · Window Computer Use**（需求來自職務現場）
> Computer Use 工具都在搶你的滑鼠鍵盤，所以測試人員沒辦法一邊讓它跑一邊做別的事。我做了一個只操作指定視窗、完全不碰實體輸入裝置的版本——**這個約束不是我加的，是使用場景本身要求的**，而它逼出了整套架構。

**04 · Jarvis Core / Dashboard**
> 一個刻意寫得很薄的核心，加上三個用 JSON Schema 契約掛進來的消費端。重點是**證明契約真的是語言中立的**：第三個消費端我故意用 TypeScript 寫。

**07 · AI Memory Vault 從個人到團隊的落地路徑**
> 那個 RAG 知識庫的形狀從第一天就是多方協作的，所以擴展成團隊共用不是重寫，是補上三件單人環境用不到的東西。而這三件我都已經踩過**相鄰的問題**——跨節點同步已經在運行，只是節點目前是兩台機器而不是兩個人。

**05 · Legacy 建置鏈現代化**（職務產出）
> 20 年前的 Visual Studio .NET 2003 專案，現在能在 VS Code 裡按 F5 除錯 UnrealScript——那個除錯器是往遊戲引擎的 C++ 裡注入 DAP 實作做出來的。

**06 · 團隊 AI 能力養成**（職務產出）
> 帶一群不寫程式的同仁從零開始用 AI。最重要的一個決定是：**把期程制改成通關制**，因為對零基礎的人，時間表比能力門檻更容易讓人放棄。

---

## 跨專案的共同主題

如果面試官問「你這幾個專案有什麼共通點」，答案是這三件事——它們在每個專案都以不同形狀重演過：

1. **沉默的失敗**（**知識點**）
   機制存在、掛在錯的地方、而失敗不會叫。這是我踩過最多次的形狀，多到我為它寫了一條規則。

2. **驗證的方向性**（**知識點**）
   「測試綠」不等於「機制正確」，「改完」不等於「改對」。我有好幾次是被自己的實測打回來的。

3. **安全預設的方向**（**知識點**）
   一個預設是開的安全開關不是開關，是裝飾。
