from flask import Flask
from client import my_proxy_client


app = Flask(__name__)


@app.route('/proxy')
def proxy():
    params = request.form['params']

    return my_proxy_client.session.post(
        'https://imhidingbehindawall',
        data=params.to_json(),
        headers=request.headers,
    )


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)

