#!/usr/bin/env python3
"""
google_auth.py — 一次性 OAuth2 認證，儲存 token.json 供後續自動化使用

第一次執行：會開啟瀏覽器讓你登入 Google 帳號並授權
後續執行：自動用 refresh_token 換新 access_token，無需人工操作

用法：
    python3 scripts/google_auth.py
"""

import os
import sys

# oauthlib 預設當 Google 回傳的 scope 是請求的子集時會拋出錯誤。
# drive.readonly 在 export URL 時需要，但 Google 有時只回傳 spreadsheets.readonly，
# 設此變數讓 oauthlib 接受較窄的 scope 而不中斷。
os.environ.setdefault("OAUTHLIB_RELAX_TOKEN_SCOPE", "1")

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(PROJECT_ROOT, "config", "credentials.json")
TOKEN_PATH = os.path.join(PROJECT_ROOT, "config", "token.json")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
]


def get_credentials():
    """取得有效的 Google 憑證，必要時執行 OAuth2 流程或刷新 token。"""
    creds = None

    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        _save_token(creds)
        return creds

    # 需要使用者互動登入（第一次，或 token 遺失）
    if not os.path.exists(CREDENTIALS_PATH):
        print(f"[錯誤] 找不到 credentials.json：{CREDENTIALS_PATH}")
        print("請先依照 scripts/SETUP_GOOGLE_API.md 的步驟下載 OAuth2 憑證")
        sys.exit(1)

    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    creds = flow.run_local_server(port=0, open_browser=True)
    _save_token(creds)
    print(f"[完成] token 已儲存至 {TOKEN_PATH}")
    return creds


def _save_token(creds):
    with open(TOKEN_PATH, "w") as f:
        f.write(creds.to_json())


if __name__ == "__main__":
    print("開始 Google OAuth2 認證流程...")
    creds = get_credentials()
    print("認證成功！後續自動化腳本可直接使用 token.json")
    print(f"token 位置：{TOKEN_PATH}")
