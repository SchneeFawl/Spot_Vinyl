import requests
from urllib.parse import quote
import json

def send_discord_webhook(webhook_url, title, artist, image_bytes, icon):
    if not webhook_url:
        return

    # spotify search query link
    search_query = quote(f"{title} {artist}")
    spt_search_url = f"https://open.spotify.com/search/{search_query}"

    embed = {
        "title": "🎧 Now Listening on Spotify",
        "description": f"**───••──────••──────••──────••───**\n\n**[{title}]({spt_search_url})**\nby {artist}\n\n**───••──────••──────••──────••───**",
        "color": 15560076,
        "footer": {
            "text": "Generated and sent via Spot_Vinyl",
            "icon_url": "attachment://icon.png"
        },
        "thumbnail": {
            "url": "attachment://cover.png"
        }
    }

    data = {
        "payload_json": json.dumps({"embeds": [embed]})
    }
    files = {}
    if image_bytes:
        files["file0"] = ("cover.png", image_bytes, "image/png")
    if icon:
        files["file1"] = ("icon.png", icon, "image/png")

    try:
        response = requests.post(webhook_url, data=data, files=files)
        response.raise_for_status()
    except Exception as e:
        print(f"Discord Webhook error: {e}")