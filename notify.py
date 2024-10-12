import os

import requests  # type: ignore
from dotenv import load_dotenv


def main():
    load_dotenv(override=True)
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    payload = {
        "content": "content",
    }
    resp = requests.post(webhook_url, json=payload)
    print(resp.status_code)


if __name__ == "__main__":
    main()
