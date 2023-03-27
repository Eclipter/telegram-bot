import openai
from aiogram import Bot, Dispatcher, executor, types
import logging

from settings import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_API_KEY)
chatgpt = OPENAI_API_KEY
dp = Dispatcher(bot)


@dp.message_handler(commands=['chat'])
async def chat_cmd(message: types.message):
    arg = message.get_args()
    openai.api_key = chatgpt
    model_engine = "text-davinci-003"
    prompt = f'{arg}'
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0
    )
    response = completion.choices[0].text
    await message.reply(f'{response}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
