import os
import logging
from string import punctuation, digits

 
from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level = logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, котто {user_name}! \n Нацарапай ФИО на кириллице и отправляйся в путь! Моу!'

    logging.info(f'{user_name} {user_id =} sent message: {message.text}')
    await bot.send_message(user_id, text)





@dp.message_handler()
async def translit1(message: types.Message):
    capital_letters = {
        u'А': u'A',
        u'Б': u'B',
        u'В': u'V',
        u'Г': u'G',
        u'Д': u'D',
        u'Е': u'E',
        u'Ё': u'E',
        u'Ж': u'Zh',
        u'З': u'Z',
        u'И': u'I',
        u'Й': u'I',
        u'К': u'K',
        u'Л': u'L',
        u'М': u'M',
        u'Н': u'N',
        u'О': u'O',
        u'П': u'P',
        u'Р': u'R',
        u'С': u'S',
        u'Т': u'T',
        u'У': u'U',
        u'Ф': u'F',
        u'Х': u'Kh',
        u'Ц': u'Ts',
        u'Ч': u'Ch',
        u'Ш': u'Sh',
        u'Щ': u'Shch',
        u'Ъ': u'',
        u'Ы': u'Y',
        u'Ь': u'',
        u'Э': u'E',
        u'Ю': u'Iu',
        u'Я': u'Ia'
    }

    lower_case_letters = {
        u'а': u'a',
        u'б': u'b',
        u'в': u'v',
        u'г': u'g',
        u'д': u'd',
        u'е': u'e',
        u'ё': u'e',
        u'ж': u'zh',
        u'з': u'z',
        u'и': u'i',
        u'й': u'i',
        u'к': u'k',
        u'л': u'l',
        u'м': u'm',
        u'н': u'n',
        u'о': u'o',
        u'п': u'p',
        u'р': u'r',
        u'с': u's',
        u'т': u't',
        u'у': u'u',
        u'ф': u'f',
        u'х': u'kh',
        u'ц': u'ts',
        u'ч': u'ch',
        u'ш': u'sh',
        u'щ': u'shch',
        u'ъ': u'ie',
        u'ы': u'y',
        u'ь': u'',
        u'э': u'e',
        u'ю': u'iu',
        u'я': u'ia'
    }

    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text 

    logging.info(f'{user_name} {user_id =} sent message: {message.text}')
    translit_string = ""
    
    for index, char in enumerate(text):
        if (char in punctuation) or (char in digits): #лучше использовать регулярку
            await bot.send_message(user_id, f'Нацарапанное ФИО не должно содержать символов "{punctuation}"  или цифр!')
            break
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(text) > index+1:
                if text[index+1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char

    await bot.send_message(user_id, translit_string)

if __name__ == '__main__':
    executor.start_polling(dp)
