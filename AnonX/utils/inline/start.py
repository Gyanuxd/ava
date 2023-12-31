from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✨ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ 🍃",
                url=f"https://t.me/ava_x_music_bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✨ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ 🍃",
                url=f"https://t.me/ava_x_music_bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="sᴀsʜɪᴋᴀɴᴛ", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data="gib_source"
            )
        ],
     ]
    return buttons
