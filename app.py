from urllib.parse import (
    urlencode,
    urljoin,
)

from flask import Flask, request
from client import my_proxy_client


app = Flask(__name__)


@app.route('/')
def proxy():
    params = urlencode(request.args)
    return my_proxy_client.session.post(
        f'https://im.hiding.behind.a.wall.com?{params}',
        data=request.data,
        headers=request.headers,
    )


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
