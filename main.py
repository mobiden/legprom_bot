import aiogram  # импорт библиотеки aiogram для работы с Telegram Bot API

from settings import BASE_DIR, create_logs
from utils.views import dp

create_logs('starting application', printing=True)




# точка доступа
def app():
    create_logs('app starting', printing=True)
    aiogram.executor.start_polling(dp, skip_updates=True)


create_logs('start main.py', printing=True)

application = app()

if __name__ == '__main__':
    create_logs('starting __name__')
    app = application



