#!/bin/bash

source .env
CONTENT="content"
curl -X POST \
    -F "content=$CONTENT" \
    $DISCORD_WEBHOOK_URL
