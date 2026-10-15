# 實例三：搜尋模組錯誤修復

不需要網站、瀏覽器或啟動伺服器。練習對象是兩個 Node.js 模組及同一份回歸測試。

從配件根目錄，逐條執行（第一條預期失敗，不要用 `&&` 把全部串起）：

```bash
node examples/03-search-bugfix/test_search.js ./search_faulty.js
node examples/03-search-bugfix/test_search.js ./search.js
node examples/03-search-bugfix/test_search.js
```

故障版應因空白查詢斷言失敗而非零退出；修正版與預設命令應退出 0，顯示 5 個搜尋情境通過。模組參數 `./search.js` 相對於測試檔所在位置解析。

故障版保留作比較，不要覆寫成修正版。用 [prompt.txt](prompt.txt) 分配修復、只讀審查、主 Agent 整合責任。完成收據包含修復前失敗、修復後成功、差異及已知限制；不得把這些結果稱為網站／UI 修復。

[回到首頁](../../README.md)
