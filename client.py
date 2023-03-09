import requests


class MyProxyClient:

    def __init__(self):
        self._session = None

    @property
    def session(self):
        if self._session:
            return self._session
        self._session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            max_retries=3,
            pool_maxsize=10,
        )
        self._session.mount('https', adapter)
        return self._session


my_proxy_client = MyProxyClient()
