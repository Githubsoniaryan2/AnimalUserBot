import asyncio

from ... import *
from .buttons import *
from .wrapper import *
from pyrogram.types import *


async def help_menu_logo(answer):
    image = None
    if image:
        thumb_image = image
    else:
        thumb_image = "https://te.legra.ph/file/ec19cf227791a167abedc.jpg"
    button = paginate_plugins(0, plugs, "help")
    answer.append(
        InlineQueryResultPhoto(
            photo_url=f"{thumb_image}",
            title="🥀 Help Menu ✨",
            thumb_url=f"{thumb_image}",
            description=f"🥀 Open Help Menu Of Animal-Userbot ✨...",
            caption=f"""
**🥀 Welcome To Help Menu Of
Animal Userbot » {__version__} ✨...

Click On Below 🌺 Buttons To
Get Userbot Commands.

🌷Powered By : [Animal Server](https://t.me/AnimalJanwarrrr).**
            """,
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def help_menu_text(answer):
    from ... import __version__
    button = paginate_plugins(0, plugs, "help")
    answer.append(
        InlineQueryResultArticle(
            title="🥀 Help Menu ✨",
            input_message_content=InputTextMessageContent(f"""
**🥀 Welcome To Help Menu Of
Animal Userbot » {__version__} ✨...

Click On Below 🌺 Buttons To
Get Userbot Commands.

🌷Powered By : [Animal Server](https://t.me/AnimalJanwarrrr).**""",
            disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def run_async_inline():
    @bot.on_inline_query()
    @inline_wrapper
    async def inline_query_handler(bot, query):
        text = query.query
        if text.startswith("help_menu_logo"):
            answer = []
            answer = await help_menu_logo(answer)
            try:
                await bot.answer_inline_query(
                    query.id, results=answer, cache_time=10
                )
            except Exception as e:
                print(str(e))
                return
        elif text.startswith("help_menu_text"):
            answer = []
            answer = await help_menu_text(answer)
            try:
                await bot.answer_inline_query(
                    query.id, results=answer, cache_time=10
                )
            except Exception as e:
                print(str(e))
                return
        else:
            return
