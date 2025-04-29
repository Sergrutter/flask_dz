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


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="ru">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                </head>
                <body>
                <div class="container text-center mt-4">
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}"alt="Марс">
                    <div class="alert alert-secondary mt-4" role="alert">
                        Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                        И начнем с Марса!
                    </div>
                    <div class="alert alert-primary" role="alert">
                        А мы тут компонентами Bootstrap балуемся
                    </div>
                </div>
                </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
