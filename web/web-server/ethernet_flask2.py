from flask import Flask, render_template
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def home():
    return app.send_static_file('index.html')
@app.route('/home2/<thing>/<height>/<color>')
def home2(thing, height, color):
    return render_template('flask2.html', thing=thing, height=height, color=color)
app.run(port =5555, debug=True)
