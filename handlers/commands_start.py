from aiogram import types
from misc import dp, bot


from aiogram.dispatcher import FSMContext



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f"Hello {message.from_user.full_name}")


@dp.message_handler(content_types=['text', 'photo', 'video_note', 'animation', 'document', 'video','file'])
async def all_message(message: types.Message):
    await message.answer(f"Hello {message.text}")
