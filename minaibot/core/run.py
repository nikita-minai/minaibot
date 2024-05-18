import telebot
from minaibot.bot.config import TOKEN, DEBUG_MESSAGE
from .decorators import check_permissions
from .router import Router
from minaibot.bot.routes import routes


bot = telebot.TeleBot(TOKEN)
router = Router(bot)


@bot.message_handler(content_types=['photo', 'document', 'video', 'text'])
def handle_message(message):
    if DEBUG_MESSAGE:
        print(message.__dict__)

    @check_permissions(bot, message, router.server)
    def get_routes():
        return routes
    router.routing(message, get_routes())


bot.polling(none_stop=True)
