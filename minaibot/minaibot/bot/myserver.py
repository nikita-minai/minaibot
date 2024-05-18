from minaibot.core.server import Server


class MySever(Server):
    def check_permission(self, *args, **kwargs):
        return False