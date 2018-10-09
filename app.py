from flask import Flask, render_template

app = Flask(__name_)

@app.route('/')
def index():
    return render_template('home.html')

if __name_ == '__main__':
app.run(debug=True)