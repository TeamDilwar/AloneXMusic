from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔎 ʜᴏᴡ ᴛᴏ ᴜsᴇ ? ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🔥 sᴇᴛᴛɪɴɢs 🔥", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍁 ᴜᴘᴅᴀᴛᴇs 🍁", url=f"https://t.me/AloneXBots",
            ),
            InlineKeyboardButton(
                text="💫 sᴜᴘᴘᴏʀᴛ 💫", url=f"https://t.me/AlonesHeaven",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔎 ʜᴏᴡ ᴛᴏ ᴜsᴇ ? ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ",
                callback_data="settings_back_helper",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ ᴏᴡɴᴇʀ ✨",
                url=f"https://t.me/ALONE_WAS_BOT"
            ),
            InlineKeyboardButton(
                text="❄️ sᴏᴜʀᴄᴇ ❄️", url=f"https://te.legra.ph/file/5fa7b4d86dcd5720ef30c.mp4",
            )
        ],
     ]
    return buttons
