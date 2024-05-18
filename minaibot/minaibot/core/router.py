import re
from telebot.types import Optional
from minaibot.bot import server


class Router:
    def __init__(self, bot):
        self.bot = bot
        self.message = None
        self.pathbefore = {}
        self.server = server()

    def __check_path(self, _path):
        if self.message.content_type == _path[1]:
            if _path[1] == 'text':
                if _path[4] == "string":
                    if _path[5]:
                        if _path[5] == self.pathbefore[self.message.chat.id]:
                            return self.message.text == _path[3]
                    else:
                        return self.message.text == _path[3]
                elif _path[4] == 'regex':
                    if _path[5]:
                        if _path[5] == self.pathbefore[self.message.chat.id]:
                            return re.match(_path[3], self.message.text)
                        else:
                            return False
                    else:
                        return re.match(_path[3], self.message.text)
                else:
                    return False
            return False
        return False

    def routing(self, message, routes: list[callable]):
        self.message = message
        if routes:
            for _path in routes:
                if self.__check_path(_path):
                    _path[2](self.bot, self.message, self.server)
                    self.pathbefore[self.message.chat.id] = _path[0]
                    break


def path(
        pathname: str,
        msgtype: str,
        answer: callable,
        text: Optional[str] = None,
        textcheckmethod: Optional[str] = None,
        pathbefore: Optional[str] = None
):
    """
    Функция для обозначения пути во время диалога с ботом
    :param pathname: Уникальное название пути
    :param msgtype: Тип сообщения:
    :param answer: Функция ответа
    :param text: Текст сообщения
    :param textcheckmethod: Метод проверки текста сообщения: "string" или "regex"
    :param pathbefore: Название пути, который было до текущего
    :return:
    """
    return pathname, msgtype, answer, text, textcheckmethod, pathbefore
