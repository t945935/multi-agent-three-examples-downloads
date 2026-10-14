# 《用三個實例學會多 Agent 應用》讀者配件

這裡提供搭配學習使用的提示詞、實作說明、驗收清單與紀錄模板。

## 下載配件

**[下載全部配件 ZIP](https://github.com/t945935/multi-agent-three-examples-downloads/archive/refs/heads/main.zip)**

下載不需要 GitHub 帳號。下載後解壓縮，依序開啟各實例的 README.md 與 prompt.txt；Markdown 與文字檔都可用文字編輯器閱讀。ZIP 會跟隨 main 分支更新。

## 三個實例

| 實例 | 學習重點 | 操作說明 | 提示詞 |
| --- | --- | --- | --- |
| 台南旅遊規劃 | 平行分工與整合 | [閱讀說明](examples/01-travel-planning/README.md) | [開啟提示詞](examples/01-travel-planning/prompt.txt) |
| Python 教材製作 | 接力協作與交接 | [閱讀說明](examples/02-python-course/README.md) | [開啟提示詞](examples/02-python-course/prompt.txt) |
| 網站搜尋錯誤修復 | 修復、審查與驗證 | [閱讀說明](examples/03-search-bugfix/README.md) | [開啟提示詞](examples/03-search-bugfix/prompt.txt) |

另附 [實作紀錄模板](templates/run-record.md)，可複製後填寫分工、執行結果與驗證證據。

## 開始練習

1. 先閱讀實例說明，確認需要的資料與執行環境。
2. 將 prompt.txt 貼到支援子 Agent 的工具；也可以在不同對話視窗手動分工。
3. 在不同視窗間交接時，提供共同檔案的位置與具體任務，請接手 Agent 重新讀取檔案。
4. 按驗收清單核對結果，使用紀錄模板保存證據。

配件除了提示詞與文件，也包含可獨立驗證的最小實例產物：Python 檔案整理程式、搜尋邏輯修復模組，以及台南行程整合範本。這些不是自動執行 Agent 的框架；網站修復仍未包含完整故障網站。

## 問題回報

可至本 repository 的 [Issues](https://github.com/t945935/multi-agent-three-examples-downloads/issues) 回報文件問題，附上實例名稱、操作步驟與錯誤訊息。請先移除個人資料及 API 金鑰。
