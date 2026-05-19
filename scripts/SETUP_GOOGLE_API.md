# Google Sheets API 設定指南

一次性設定，設定完成後 Routines 可完全自動執行。

---

## 步驟一：建立 Google Cloud 專案並啟用 API

1. 前往 [Google Cloud Console](https://console.cloud.google.com/)
2. 點選頂部下拉選單 → **新增專案**
   - 名稱：`investor-skill`（或任意名稱）
3. 確認專案已被選取，前往 **API 和服務 → 程式庫**
4. 搜尋並啟用以下兩個 API：
   - `Google Sheets API` → 啟用
   - `Google Drive API` → 啟用

---

## 步驟二：建立 OAuth2 憑證

1. 前往 **API 和服務 → 憑證**
2. 點選 **建立憑證 → OAuth 用戶端 ID**
3. 若出現「設定同意畫面」提示：
   - 選 **外部**（External）→ 建立
   - 填入應用程式名稱（如 `investor-skill`）
   - 填入你的 Google 帳號 email
   - 儲存並繼續（其餘欄位留空）
   - 在「測試使用者」加入你自己的 email → 儲存
4. 回到建立憑證，選擇：
   - 應用程式類型：**電腦版應用程式（Desktop app）**
   - 名稱：`investor-skill-local`
5. 點選 **建立** → 下載 JSON 檔案

---

## 步驟三：放置憑證檔案

將下載的 JSON 重新命名為 `credentials.json`，放到：

```
investor_skill/
└── config/
    └── credentials.json   ← 放這裡
```

> ⚠️ `credentials.json` 和 `token.json` 已加入 `.gitignore`，不會被 commit

---

## 步驟四：執行一次性認證

```bash
cd ~/Desktop/investor_skill
python3 scripts/google_auth.py
```

執行後會：
1. 自動開啟瀏覽器
2. 選擇你的 Google 帳號（需要有試算表查看權限的帳號）
3. 授權後自動儲存 `config/token.json`

---

## 步驟五：測試自動下載

```bash
python3 scripts/download_watchlist.py
```

成功後會輸出：
```
[2026-05-19] 取得 Google 認證...
認證成功
下載試算表至 .../Market Watchlist0519.xlsx...
下載完成（XXX KB）
解析 Watchlist...
輸出：reports/2026-05-19_watchlist.md
```

---

## Claude Code Routines 設定

確認以上步驟完成後，在 Routine 中加入：

```
python3 /home/evan/Desktop/investor_skill/scripts/download_watchlist.py
```

token 會自動 refresh，無需人工操作。

---

## 常見問題

| 問題 | 解法 |
|------|------|
| `credentials.json 找不到` | 確認檔案放在 `config/credentials.json` |
| `401 認證失敗` | 刪除 `config/token.json`，重新執行 `google_auth.py` |
| `403 沒有權限` | 確認登入的 Google 帳號有試算表查看權限 |
| `token 過期` | 正常情況腳本會自動刷新；若失敗則重新執行 `google_auth.py` |
