import random

from aiogram import types
from misc import dp,bot
import asyncio
from .sqlit import update_status_access
from .admin import new_password1,new_password2,new_password3,new_password4,new_password5,new_password6,new_password7,new_password8,new_password9

ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID = [ADMIN_ID_1,ADMIN_ID_2]
channel = -1001506311095
flag1 = 1 #НАСТРОЙКА РЕЖИМА ПОКАЗА FILE ID

@dp.message_handler(content_types=['text', 'photo', 'video_note', 'animation', 'document', 'video','file'])
async def all_message(message: types.Message):
    from .admin import passwd1,passwd2,passwd3,passwd4,passwd5,passwd6,passwd7,passwd8,passwd9
    if str(passwd1) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        await bot.send_message(chat_id=channel,text= f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass1""")
        update_status_access(message.chat.id)
        new_password1()

    elif str(passwd2) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password2()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass2""")

    elif str(passwd3) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password3()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass3""")

    elif str(passwd4) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password4()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass4""")

    elif str(passwd5) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password5()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass5""")

    elif str(passwd6) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password6()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass6""")

    elif str(passwd7) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password7()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass7""")

    elif str(passwd8) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password8()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass8""")

    elif str(passwd9) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password9()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass9""")

    else:
        await message.answer('Неверный пароль')