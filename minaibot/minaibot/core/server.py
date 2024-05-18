import requests
import types


class Server:
    url = "http://httpbin.org/get"
    headers = dict()

    def request(self, method, payload):
        return requests.request(method, self.url, data=payload)

    def check_permission(self, *args, **kwargs):
        """
        You can override this method in subclasses
        :return: True / False
        """
        return True

    def call_subclass_method(self):
        raise NotImplementedError("Subclasses should implement this method!")