from flask import Flask, request
import requests


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    return app


app = create_app()


@app.before_request
def proxy():
    headers = {h[0]: h[1] for h in request.headers}
    url = request.url
    # headers['x-token'] = '***'
    # print(headers)
    # 一些自己的逻辑...
    return requests.request(request.method, url, data=request.json, headers=headers).content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=18080)
