# 專案卷

> 每份文件的結構固定：**解什麼問題 → 架構 → 難題與解法 → 成果**。
> 「難題與解法」是重點，其他章節是為了讓那一節有脈絡。

---

## 索引

### 自主發起（以個人時間與設備開發）

| # | 專案 | 期間 | 技術棧 | 規模 |
|---|---|---|---|---|
| [01](01-ai-memory-vault.md) | AI Memory Vault | 2026-04 ~ 進行中 | Python 3.12 · ChromaDB · LangChain · FastMCP · PyInstaller · Tauri | <!--m:ai_memory_vault.tests_passed-->2,651<!--/m--> tests · <!--m:ai_memory_vault.mcp_tools_exposed-->25<!--/m--> MCP tools · <!--m:ai_memory_vault.version-->v4.4.0<!--/m--> |
| [02](02-remote-ai-task-platform.md) | Remote AI Task Platform | 2026-07 ~ 進行中 | Python · SQLite(WAL) · Discord.py · Windows API | <!--m:remote_ai_task_platform.tests_passed-->528<!--/m--> tests · Phase 1B 完成 |
| [04](04-jarvis-core-and-dashboard.md) | Jarvis Core / Dashboard | 2026-07 ~ 維持 | Python · TypeScript(Node 原生) · JSON Schema | 142 + 87 tests · kernel ≤1500 LOC |
| [07](07-team-adoption-path.md) | AI Memory Vault 帶進團隊的落地路徑 | — | 設計推導 | 三個缺口 · 三個風險 |

### 需求來自職務現場

於此記錄的是技術問題與解法，不是所有權主張。歸屬各不相同，逐項標註。
三篇都已去識別化，不含僱主、專案代號、內部系統與路徑。

| # | 專案 | 期間 | 技術棧 | 規模 | 歸屬 |
|---|---|---|---|---|---|
| [03](03-window-computer-use.md) | Window Computer Use | 2026-07 ~ 凍結 | C# · .NET 8 · UI Automation · Windows Graphics Capture | <!--m:window_computer_use.loc-->10,300<!--/m--> LOC · <!--m:window_computer_use.tools-->14<!--/m--> MCP tools | 個人時間與設備；依職務發明條款認定 |
| [05](05-legacy-toolchain-modernization.md) | Legacy 工具鏈現代化 | 2026-05 ~ | TypeScript · C++ · DAP · VS Code Extension API | VS2003 + UE2 全鏈打通 | 職務中開發，屬雇主 |
| [06](06-ai-enablement.md) | 團隊 AI 導入 | 2026-07 ~ | — | 六階段通關制 | 職務中開發，教材屬雇主 |

---

## 跨專案的共同主題

這幾個專案的共通點是三件事——它們在每個專案都以不同形狀重演過：

1. **沉默的失敗**（**知識點**）
   機制存在、掛在錯的地方、而失敗不會叫。這是我踩過最多次的形狀，多到我為它寫了一條規則。

2. **驗證的方向性**（**知識點**）
   「測試綠」不等於「機制正確」，「改完」不等於「改對」。我有好幾次是被自己的實測打回來的。

3. **安全預設的方向**（**知識點**）
   一個預設是開的安全開關不是開關，是裝飾。

---

## 知識點 × 專案：這些經驗是從哪裡長出來的

十二個知識點，對照它們各自在哪個專案被真的踩過。
**這張表的用途是讓你挑，而不是我挑**——指著任何一個 ●●● 問下去，都有一個具體案例、
一組當時的數字，以及一次判斷失誤可以講。

| 知識點 | 01 Vault | 02 RATP | 03 WCU | 04 Jarvis | 05 Legacy | 06 導入 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| 混合檢索（BM25＋向量＋時間重排） | ●●● | | | | | |
| MCP 協定與工具面設計 | ●●● | ●● | ●● | | | |
| 記憶分層與注入預算 | ●●● | | | | | |
| **沉默的失敗** | ●●● | ●●● | ●● | ●●● | ●● | |
| **fail-closed（安全預設的方向）** | ●● | ●●● | ●●● | ●● | | |
| Prompt Injection 與信任邊界 | | ●● | ●●● | | | |
| **透過真實入口驗證** | ●●● | ●● | ●●● | ●● | ● | ●● |
| 跨模型同儕審查 | ●●● | ●●● | ●●● | ●●● | | |
| 最小權限的工程落地 | ● | ●●● | ●●● | ●● | | |
| 契約驅動解耦 | ●● | ● | | ●●● | | |
| Legacy 編碼與工具鏈 | ● | ● | | | ●●● | |
| 打包與散布 | ●●● | | ●● | | ● | |

●●● 核心經驗，可以講五分鐘　●● 有實際案例　● 有碰到

三個粗體的知識點就是上一節那三個共同主題，它們**橫跨五個專案以上**，
而這正是為什麼它們被寫成規則而不是筆記。

> 07（從個人到團隊的落地路徑）不在表內：它是設計推導，不是實作經驗。
