# =========================================
# handlers/toss_pass.py
# =========================================

from telethon import events
from dynamic_emoji import get_text_custom_emojis
import re

from utils import send_text_safe
from handlers.toss_handler import toss_posts
from channels import CHANNELS
from memory.memory_manager import *


def register_toss_pass_handler(client):

    @client.on(events.NewMessage(pattern='/tpass'))
    async def toss_pass_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        raw = event.raw_text.strip()

        # =========================
        # STRICT FORMAT ONLY
        # /tpass 1 (TEAM NAME) BAT/BOWL
        # =========================

        match = re.match(
            r'^/tpass\s+(\d+)\s+\((.*?)\)\s+(BAT|BOWL)$',
            raw,
            re.IGNORECASE
        )

        if not match:
            await event.reply(
                "❌ WRONG FORMAT\n\nUSE:\n/tpass 1 (INDIA WOMEN) BAT"
            )
            return

        toss_id = int(match.group(1))
        team = match.group(2).strip().upper()
        choice = match.group(3).strip().upper()
        team_custom_emojis = get_text_custom_emojis(
            event,
            team,
            occurrence=1
        )

        print(
            "🔥 TPASS TEAM EMOJIS:",
            team_custom_emojis
        )

        data = load_memory()
        selected = None

        # find toss
        for toss in data["tosses"]:
            if toss["id"] == toss_id:

                if toss.get("status") == "passed":
                    await event.reply("❌ TOSS ALREADY PASSED")
                    return

                selected = toss.get("posts")
                break

        if not selected:
            await event.reply("❌ TOSS ID NOT FOUND")
            return
        # =========================
        # SEND TO CHANNELS
        # =========================

        for post in selected:

            channel = post["channel_id"]
            msg_id = post["photo_id"]
            channel_name = post["channel_name"]

            if channel_name == "ROYAL":
                text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

TOSS PASS...✅️
PUNTER KHUS...✅️
HUM KHUS...✅️

ROYAL WIN 💠"""

            elif channel_name == "BATMAN":
                text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

PREMIUM PASS CONFIRM 🔥

BATMAN (Official) 💠"""

            elif channel_name == "BETTING":
                text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

💰 BACK TO BACK PASS 💰
     BETTING KING
  HAIN TO PROFIT HAIN 

BETTING KING  💠"""

            elif channel_name == "GAME":
                text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅✅

👉 GAME CHANGER ( Abhi ) 💠"""

            elif channel_name == "GUDDU":
                text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

Back To Back pass 🔻

Back To Back pass 🔻

Play With :- GUDDU BHAIYA ✅"""

            elif channel_name == "ROCKY":
                text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅

Rocky bhai (Trending King) 💠"""

            elif channel_name == "JACKY":
                text = f"""{team} WON THE TOSS AND TO {choice} ✔️✔️

💣 BOOM 💣👍💣 BOOM 💣

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅️✅️

𝐎𝐍𝐋𝐘 👉 JACKY FIXER 💠"""

            elif channel_name == "PRIYANSHU":
                text = f"""{team} HAVE WON THE TOSS & ELECTED TO 🏏 {choice} FIRST ✔️

𝐓𝐎𝐒𝐒 𝐏𝐀𝐒𝐒

𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌✔️

ONLY 👉 PRIYANSHU BHAI 🏏 💠"""

            elif channel_name == "TOSSKING":
                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥
💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

CALL ➡️TOSS KING(Aditya)💠"""

            elif channel_name == "REDDY":
                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

FIX TOSS PASS 
SURE TOSS PASS 
LIFE TIME TOSS PASS ✔️

CALL ➡️REDDY ANNA 💠"""
            elif channel_name == "ANGAD":
                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

ONLY ONE IN MARKET

FIX TOSS PASS 
SURE TOSS PASS 
LIFE TIME TOSS PASS ✔️

CALL ➡️ANGAD DADA 💠"""

            elif channel_name == "RAHUL":
                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

JACKPOT KA BAAP

FIX TOSS PASS 
SURE TOSS PASS 
LIFE TIME TOSS PASS ✔️

CALL ➡️RAHUL DADA 💠"""

            elif channel_name == "SHIVA":
                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥 

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅

ONLY SHIVA 💠"""

            elif channel_name == "KING":
                text = f"""{team} WON THE TOSS AND TO {choice} ✔️✔️

💣 BOOM 💣👍💣 BOOM 💣

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

𝐎𝐍𝐋𝐘 👉 THE KING 💠"""

            else:
                text = f"""{team} HAVE WON THE TOSS & ELECTED TO 🏏 {choice} FIRST ✔️

𝐓𝐎𝐒𝐒 𝐏𝐀𝐒𝐒

OWNER UPDATE ✅"""

            await send_text_safe(
                client,
                channel,
                text,
                msg_id,
                channel_name,
                team,
                team_custom_emojis
            )

        # =========================
        # MARK AS PASSED
        # =========================

        for toss in data["tosses"]:
            if toss["id"] == toss_id:
                toss["status"] = "passed"
                break

        save_memory(data)

        await event.reply(
            f"✅ TOSS PASS POSTED\n🆔 ID: {toss_id}"
        )

print("✅ TOSS PASS HANDLER LOADED")            