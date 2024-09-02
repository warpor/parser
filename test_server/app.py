from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return render_template_string('''
        <html>
            <head><title>Main Page</title></head>
            <body>
                <h1>Main Page</h1>
                <a href="/page1">Page 1</a><br>
                <a href="/page2">Page 2</a><br>
                <a href="/page4">Page 2</a><br>
            </body>
        </html>
    ''')


@app.route('/page1')
def page1() -> str:
    return render_template_string('''
        <html>
            <head><title>Page 1</title></head>
            <body>
                <h1>Page 1</h1>
                <a href="/">Home</a><br>
                <a href="/page2">Page 2</a>
            </body>
        </html>
    ''')


@app.route('/page2')
def page2() -> str:
    return render_template_string('''
        <html>
            <head><title>Page 2</title></head>
            <body>
                <h1>Page 2</h1>
                <a href="/">Home</a><br>
                <a href="/page1">Page 1</a>
            </body>
        </html>
    ''')


if __name__ == '__main__':
    app.run(port=5000)
