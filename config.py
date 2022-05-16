import aiogram as aio
from subTools import recoq_qr
URL = 't.me/MuseumPobeda_bot'
TOKEN = '5126180249:AAFJHMCFI59KSDYrdOJ2VcQQ-0PjldFhBf4'

bot = aio.Bot(token=TOKEN)
dp = aio.Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:aio.types.Message):
    await bot.send_message(message.chat.id, 'Привет, товарищ! Добро пожаловать  в музей Победы. Я телеграм-бот, который поможет тебе максимально комфортно провести время в музе Победы и получить максимум знаний!'
                                            'Чтобы получить подробную информацию об экспонате, просто пришли мне QR-код, расположенный рядом с экспонатом!')
@dp.message_handler(content_types="photo")
async def QR(message:aio.types.Message):
    '''
    result = recoq_qr(gg)
    '''
    #получение доступа к id изображения
    f = message.photo[0].file_id
    info: aio.types.File = await bot.get_file(f)
    #скачивание изображения из чата
    await message.photo[-1].download(f'{info.file_path}.jpg')
    #разделение информации об id экспоната и информации о нём
    result = recoq_qr(f'{info.file_path}.jpg').split(";")
    print(result)
    #отправка результата
    with open(f'expos/{result[0]}.png', 'rb') as filen:
        await bot.send_photo(message.chat.id, filen, result[1])
if __name__ == "__main__":
    aio.executor.start_polling(dp, skip_updates=True)