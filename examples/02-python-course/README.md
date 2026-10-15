# 實例二：Python 教材製作

將 [prompt.txt](prompt.txt) 依序交給教學設計、程式與試學角色。只用自行建立的假資料，絕不操作真實下載資料夾。

從配件根目錄執行測試：

```bash
python3 -m unittest discover -s examples/02-python-course -p 'test_*.py'
```

預期 7 項測試通過。分類含 `.txt`→文件、`.csv`／`.xlsx`→試算表；未知副檔名與無副檔名→其他。

以下在 Bash 建立新的臨時資料後先預覽，再明確套用：

```bash
TMP_DIR="$(mktemp -d)"
mkdir -p "$TMP_DIR/input"
printf 'fake notes\n' > "$TMP_DIR/input/notes.txt"
python3 examples/02-python-course/organize_downloads.py "$TMP_DIR/input"
python3 examples/02-python-course/organize_downloads.py "$TMP_DIR/input" --apply
```

預覽不搬檔；套用後假檔在 `文件/notes.txt`。同批次目的路徑與既有檔名衝突會加序號，子資料夾不遞迴。程式沒有把任意輸入路徑自動限制在臨時目錄；安全邊界仍由操作者核對。不要讓另一個程序同時改動練習目錄。

[回到首頁](../../README.md)
