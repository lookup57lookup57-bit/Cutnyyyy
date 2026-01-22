from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def join_kb(channel):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Join Channel", url=f"https://t.me/{channel.replace('@','')}")],
        [InlineKeyboardButton(text="🔄 I Joined", callback_data="check_join")]
    ])

def main_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Wallet", callback_data="wallet")],
        [InlineKeyboardButton(text="🔥 Hot Accounts", callback_data="hot")],
        [InlineKeyboardButton(text="🎁 Earn Points", callback_data="earn")]
    ])