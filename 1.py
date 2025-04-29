from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def glav():
    return f"""<!doctype html>
                <html lang="en">
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def index():
    return f"""<!doctype html>
                <html lang="en">
                  <body>
                    <h3>И на Марсе будут яблони цвести!</h3>
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <body>
                    <h3>Человечество вырастает из детства.</h3>
                    <h3>Человечеству мала одна планета.</h3>
                    <h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                    <h3>И начнем с Марса!</h3>
                    <h3>Присоединяйся!</h3>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}"alt="здесь должна была быть картинка, но не нашлась">
                        <br>Вот она какая, красная планета.
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
