## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCD2YWNMx7G82D4lgONT06CRT8p1XPUi-8bjEZqWXjQaoUTSDG34uJxy2HdrVyt1IDIBPrFJI3Rvfp9MY74THNtAWdxAE04NNoYKp8lD0X65pIjX859ttQXUi_fsGjupV2re8MyHebqKiUpMls7bi27DAH4MHLtZw35-S0-wTvx4rEMEjCugKB9aziRWHIkBwbJ2nlZjFdpUfiJ-g5JXB4-eapvMlrgHe19DV5_SW8dY2s4ICLUARnPNxUMjdNj2BPn7MLXtRnYV48MfAB8mIemZIK-Sh6aVg5ZVDleBYsHSMOsH1o0IH5OfAmpvNYo-R8VXUZ38NADvr7o2fsCwiw-AAAAATFtMEgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5105942915:AAHTZeBScyuwgmDHKjZonW-HaLd3qtMtqxg")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME","Yuriko2_bot")
OWNER_ID = getenv("OWNER_ID", "1920507972")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LolKides")
GROUP_SUPPORT = getenv("GROUP_SUPPORT" "BotDuniyaXd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "YurikoRobot")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "Null")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY", "elsaa_Ro_bot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1920507972").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5433c44cab6436dcd0140.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/5433c44cab6436dcd0140.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
