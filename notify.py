import os

import requests
from dotenv import load_dotenv

load_dotenv(override=True)


def main():
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    payload = {
        "content": "content",
    }
    resp = requests.post(webhook_url, json=payload)
    print(resp.status_code)


if __name__ == "__main__":
    main()
