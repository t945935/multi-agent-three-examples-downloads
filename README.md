# 多 Agent 三實例：讀者配件 1.0.0

> 書籍讀者請下載 [1.0.0 固定配件 ZIP](https://github.com/t945935/multi-agent-three-examples-downloads/releases/download/v1.0.0/multi-agent-reader-resources-1.0.0.zip)，不要以 Code → Download ZIP 代替固定版本。
>
> [版本說明與附件](https://github.com/t945935/multi-agent-three-examples-downloads/releases/tag/v1.0.0)。固定 ZIP 的 SHA-256：`617a21d5e59e2ee7766a68c51fb15b67db5244e72a006c08fba33e343d5e5c79`。
>
> 本庫主分支為來源檢視用；根目錄 README 與 manifest 含公開下載說明，與固定 ZIP 的這兩個文件不同。範例、測試、提示詞與模板 bytes 相同。書中完整性核對請使用固定 ZIP 的 manifest；主分支的 manifest 則另涵蓋 `.gitignore` 與本庫 README。

本包僅含提示詞、原創範例、測試及可填寫模板，不含付費書稿或私人編輯紀錄。請先解壓縮到自行建立的練習工作區，不要在真實下載資料夾或個人檔案庫執行整理程式。

## 環境與開始方式

書中命令採 Ubuntu／WSL 的 Bash；先確認 `python3 --version`、`node --version` 可執行。Python 建議 3.10 以上，Node.js 需支援 `node:assert/strict`。從本包根目錄執行：

```bash
python3 -m unittest discover -s examples/02-python-course -p 'test_*.py'
node examples/03-search-bugfix/test_search.js
```

預期 Python 跑 7 項測試成功，Node 顯示 5 個搜尋情境通過。測試使用臨時假資料；這不是 AI 自動分工系統，也不是網站 UI 驗收。

## 配件入口

- [旅遊規劃](examples/01-travel-planning/README.md)：提示詞、條件式規劃表；未指定日期，不提供保證可出發行程。
- [Python 教材](examples/02-python-course/README.md)：預覽、套用、碰撞保留與非遞迴行為。
- [搜尋修復](examples/03-search-bugfix/README.md)：故障模組、修正版與同一回歸測試。
- [交接模板](templates/run-record.md)：記錄輸入、產物、命令、結果及限制。

`VERSION` 應為 `1.0.0`；`manifest.json` 記錄其餘全部檔案的 SHA-256。以版本及內容清單為準，不把會變動的 main 分支當成固定教材版本。此包本地建置不代表 GitHub 已更新。
