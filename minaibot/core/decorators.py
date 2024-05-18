from minaibot.bot.config import PERMISSION_DENIED_MESSAGE


def check_permissions(bot, message, server):
    def decorator(view_func):
        def wrapped(*args, **kwargs):
            if not has_permissions(message, server):
                bot.send_message(message.chat.id,
                                 text=PERMISSION_DENIED_MESSAGE % (message.from_user.first_name,
                                                                       "@nikita_fomichev"))
                return
            return view_func(*args, **kwargs)
        return wrapped
    return decorator


def has_permissions(message, server):
    return server.check_permission(message)

