import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from config import BOT_TOKEN, JOIN_CHANNEL_ID, JOIN_CHANNEL_USERNAME
from join_check import is_joined
from keyboards import join_kb, main_kb
from referral import get_ref

dp = Dispatcher()

@dp.message(CommandStart())
async def start(m: Message, bot: Bot):
    payload = m.text.split(maxsplit=1)[1] if len(m.text.split()) > 1 else ""
    ref = get_ref(payload)

    joined = await is_joined(bot, m.from_user.id, JOIN_CHANNEL_ID)
    if not joined:
        await m.answer(
            "🔒 Continue ke liye channel join karo",
            reply_markup=join_kb(JOIN_CHANNEL_USERNAME)
        )
        return

    await m.answer("✅ Welcome! Menu choose karo", reply_markup=main_kb())

@dp.callback_query(F.data == "check_join")
async def check(cb: CallbackQuery, bot: Bot):
    if await is_joined(bot, cb.from_user.id, JOIN_CHANNEL_ID):
        await cb.message.edit_text("✅ Joined!", reply_markup=main_kb())
    else:
        await cb.answer("Abhi join nahi hua", show_alert=True)

@dp.callback_query(F.data == "wallet")
async def wallet(cb: CallbackQuery):
    await cb.message.answer("💳 Your Points: (backend se connect karega)")

@dp.callback_query(F.data == "earn")
async def earn(cb: CallbackQuery):
    link = f"https://t.me/{(await cb.bot.get_me()).username}?start=ref_{cb.from_user.id}"
    await cb.message.answer(f"🎁 Referral Link:\n{link}\n+3 Points per join")

async def main():
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)

asyncio.run(main())