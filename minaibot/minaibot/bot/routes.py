from minaibot.core.router import path
from minaibot.answers.start import start, stop

routes = [
    path(pathname="start", msgtype="text", text="/start", textcheckmethod="string", answer=start),
    path(pathname="stop", msgtype="text", text="/stop", textcheckmethod="string", answer=stop),
]
