# =========================================
# templates/session_templates.py
# =========================================


def session_call_emoji(call):
    if call == "YES":
        return "✅"
    return "❌"


# =========================================
# ROYAL
# =========================================

def royal_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
{over} OVER 🌐 {call} KARO {emoji}

{run} RUN 🏏

Play only on 👇

Plat at -- Www.Khelking.com

""".strip()


def royal_session_pass(over, result):

    return f"""
{result} 🅿️🅰️💲💲✔️

{over} OVER 👑

SESSIONS PASS 💸❤️
""".strip()


def royal_session_loss():

    return """
LOSS RAHA APNA DONT WORRY ❤️

WAIT FOR NEXT ❌
""".strip()


# =========================================
# BETTING
# =========================================

def betting_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
{run} RUN 👍 {over} OVER 🏏

{call} KARO {emoji}

INDIA BEST SITE 👇

®️ www.stake888.games

10K LIMIT SE PLAY 🥳
""".strip()


def betting_session_pass(result):

    return f"""
{result} 🅿️🅰️💲💲✔️✔️

SESSIONS PASS 💰🔥

💫 🅱𝗢𝗢Ⓜ️ 💫 🅱𝗢𝗢Ⓜ
""".strip()


def betting_session_loss():

    return """
SESSION LOSS ❌
""".strip()


# =========================================
# BATMAN
# =========================================

def batman_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
{over} OVER 👉 {run} RUN

BINDASS 👍

{call} KARO 👉 {emoji}

PLAY ON 👉 Www.Khelking.com

SAME LIMIT SE PLAY 💰
""".strip()


def batman_session_pass(result):

    return f"""
{result} 🅿️🅰️💲💲 🤑🤑

🤑 SESSIONS PASS 💰
""".strip()


def batman_session_loss():

    return """
SESSION LOSS 😒
""".strip()


# =========================================
# GAME
# =========================================

def game_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
 🚨 ALL ACTIVE MEMBERS 🚨

 {call} KARO {emoji}

{over} OVER 🏏 {run} RUN 

INIDAN TRUSTED SITE 👇

Www.Khelking.com 💯

""".strip()


def game_session_pass(result):

    return f"""
 💸 SESSIONS PASS 💸

{result} 🅿️🅰️💲💲

🔥 TARGET HIT 🔥
""".strip()


def game_session_loss():

    return """
LOSS ❌ KOI BAAT NHI 

NEXT SESSION 💯 COVER HOGA 👍
""".strip()


# =========================================
# GUDDU
# =========================================

def guddu_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""

📊  SESSION UPDATE 📊 

{run} RUN 🎯 {over}  OVER 🏏

{call} KARO {emoji}

10K LIMIT SE PLAY 💰
""".strip()


def guddu_session_pass(result):

    return f"""
 💸 SESSIONS PASS 💸

{result} 🅿️🅰️💲💲✔️✔️

🏆 SESSION PASSED

📊 RESULT ➜ {result}

💰 PROFIT BOOKED
""".strip()


def guddu_session_loss():

    return """
 SESSION MISSED 😒

KEEP PATIENCE
NEXT ONE WILL COVER IT 💯
""".strip()


# =========================================
# ROCKY
# =========================================

def rocky_session(over, run, call):
    emoji = session_call_emoji(call)

    
    return f"""
 👇 LIVE SESSION 👇

{run} RUN 👉 {over} OVER

{call} KRO {emoji}

AISA BEST SITE 👇
Www.Khelking.com 💯
Www.Khelking.com 💯
""".strip()


def rocky_session_pass(result):

    return f"""
🅿️🅰️💲💲🏆🏆

🏏 RESULT 👉 {result}

🏆 BACK TO BACK PASS 🏆
""".strip()

def rocky_session_loss():

    return """
SESSION LOSS ❌

NEXT SESSION PASS ROCKY PROMISE
""".strip()


# =========================================
# PRIYANSHU
# =========================================

def priyanshu_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
🌐 LIVE UPDATE 🌐

{run} RUN 👉 {over} OVER 🏏

{call} KRO SAB {emoji}
""".strip()


def priyanshu_session_pass(result):

    return f"""
 {result} 🅿️🅰️💲💲🏆

💰 WINNING SESSION 💰

 WAIT FOR NEXT SESSION 💯
""".strip()

def priyanshu_session_loss():

    return """
❌ SESSION LOSS 😊 DON'T WORRY

NEXT SESSION WILL PASS 🎯 

WAIT FOR NEXT SESSION 💯
""".strip()


# =========================================
# JACKY
# =========================================

def jacky_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
PLAY WHIT SAME LIMIT ✔️

🏏 {run} RUN 🔻 {over} OVER

 {call} KRO {emoji}

""".strip()


def jacky_session_pass(result):

    return f"""
{result} RUN SESSION 🅿🅰🆂🆂 

🔻SESSIONS PASS 🔻

💣 BOOM 💣 BOOM 💣
""".strip()


def jacky_session_loss():

    return """
SESSION WILL BE LOSS❌
""".strip()


# =========================================
# KING
# =========================================

def king_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
🔻 SESSION LIVE 🔻

{run} RUN 👉 {over} OVER

{call} KARO SAB {emoji}

""".strip()


def king_session_pass(result):

    return f"""
{result} RUN 🅿️🅰️💲💲

🤑 SESSIONS PASS 🤑

💣 BOOM 💣 🔻 💣 BOOM 💣

👑 KING ENTRY 👑
""".strip()


def king_session_loss():

    return """

😒 SESSION LOSS 😒 KEEP TRUST

🎯 NEXT SESSION WILL PASS 🎯

""".strip()


# =========================================
# ANGAD
# =========================================

def angad_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
💠 RAHUL DADA ENTRY 💠

{call} {emoji}

🏏 {run} RUN • 📍 {over} OVER
""".strip()


def angad_session_pass(result):

    return f"""
🏏 {result} RUN

💯 🅿🅰🆂🆂 💯

🏏 {result} RUN

RAHUL DADA 💠
""".strip()


def angad_session_loss():

    return """
❌ 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗟𝗢𝗦𝗦

🎯 NEXT CALL WILL BE BETTER
""".strip()


# =========================================
# RAHUL
# =========================================

def rahul_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
✔️ SESSION CALL ✔️

{run} RUN 👉 {call} KARO SAB {emoji}

{over} OVER 🏏

PLAY ON 👉 WWW.KHELKING.COM 💯

""".strip()


def rahul_session_pass(result):

    return f"""
💯 SESSIONS PASS 💯

{result} RUN 🅿️🅰️💲💲

ACCURATE ENTRY 💯

RAHUL DADA 💠
""".strip()


def rahul_session_loss():

    return """
🔻 SESSION LOSS 🔻

 DON'T LOSE TRUST 👍
""".strip()


# =========================================
# SHIVA
# =========================================

def shiva_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
🔥 SHIVA REDDY  🔥

{over} OVER 👉 {run} RUN

{call} KARO SAB {emoji}

FULL SUPPORT ❤️
""".strip()


def shiva_session_pass(result):

    return f"""
{result} RUN 🔥 SHIVA REDDY

💯 🅿🅰🆂🆂 💯

🏏 {result} RUN

👑 PERFECT CALL
""".strip()


def shiva_session_loss():

    return """
💠 RAHUL DADA

❌ 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗟𝗢𝗦𝗦

🎯 NEXT CALL WILL BE BETTER
""".strip()

# =========================================
# REDDY
# =========================================

def reddy_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
ACTIVE ALL MEMBERS 🔔

🔻 {run} RUN | {over} OVER

🔻 {call} KRO FATA FAT {emoji}

🔻 PALY WITH SAME LIMIT 💰
""".strip()


def reddy_session_pass(result):

    return f"""
{result} RUN SESSION 🅿️🅰️💲💲

 🔻 SESSIONS PASS 🔻
💯 BACK TO BACK PASS 💯

ONLY 👉 REDDY ANNA 💠
""".strip()


def reddy_session_loss():

    return """
SESSION LOSS 😒

🎯 NEXT CALL SOON
""".strip()


# =========================================
# TOSSKING
# =========================================

def tossking_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
🌐 SESSION 🌐

🏏 {run} RUN • 🔻 {over} OVER

✅ {call} {emoji}
""".strip()


def tossking_session_pass(result):

    return f"""
💯🅿🅰🆂🆂💯

🏏 {result} RUN

🔥 KING'S PERFECT CALL
""".strip()


def tossking_session_loss():

    return """
⚠️ 🅻🅾🆂🆂 ⚠️

💎 TRUST THE PROCESS
""".strip()


# =========================================
# LOADED
# =========================================

print("✅ SESSION TEMPLATES LOADED")