import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types, utils
from darkHumorScraper import BotScraper

load_dotenv()

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
bot = Bot(token=TELEGRAM_API_KEY)
scraper = BotScraper()
num_of_warnings = 0

try:
    dp = Dispatcher(bot)
    print('Bot is running...')
except Exception as e:
    raise NameError('Telegram API key is not valid')


@dp.message_handler(commands=['poll'])
async def create_poll(message: types.Message):
    global num_of_warnings
    """
    poll command handler
    Create a poll with a question (first parameter) and a list of answers (the rest of the parameters). Example: /poll question | option2 | option3
    :param message: types.Message object
    :return:
    """
    arguments = message.get_args().split(' | ')
    if len(arguments) < 2:
        await message.reply('You must specify at least two options\nExample: /poll question | option2 | option3')
        return
    else:
        await bot.send_poll(message.chat.id, question=utils.markdown.bold(arguments[0]),
                            options=arguments[1:],
                            is_anonymous=False)
        try:
            await message.delete()
        except Exception as e:
            if num_of_warnings < 3:
                await message.reply("Bot doesn't have rights to delete messages!")
                num_of_warnings += 1


@dp.message_handler(commands=['anonymous_message'])
async def create_anonymous_message(message: types.Message):
    global num_of_warnings
    """
    anonymous_message command handler
    Create an anonymous message with a text (first parameter). Example: /anonymous_message Hello world
    :param message: types.Message object
    :return:
    """
    if len(message.get_args()) < 1:
        await message.reply('You must specify at least two options\nExample: /anonymous_message Hello world')
        return
    else:
        try:
            await message.delete()
        except Exception as e:
            if num_of_warnings < 3:
                await message.reply("Bot doesn't have rights to delete messages!")
                num_of_warnings += 1
        await bot.send_message(message.chat.id, message.get_args())


@dp.message_handler(commands=['dark_humor_pl'])
async def print_random_dark_humor_message(message: types.Message):
    """
    dark_humor_pl command handler
    Print a random dark humor message
    :param message: types.Message object
    :return:
    """

    await bot.send_message(message.chat.id, scraper.get_dark_joke(), parse_mode='html')
    try:
        await message.delete()
    except Exception as e:
        if num_of_warnings < 3:
            await message.reply("Bot doesn't have rights to delete messages!")
            num_of_warnings += 1


if __name__ == '__main__':
    executor.start_polling(dp)
