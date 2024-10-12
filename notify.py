import os

import requests  # type: ignore
from dotenv import load_dotenv


def main():
    load_dotenv(override=True)
    url = os.getenv("DISCORD_WEBHOOK_URL")
    data = {
        "content": "content",
    }
    resp = requests.post(url=url, data=data)
    print(resp.status_code)


if __name__ == "__main__":
    main()
