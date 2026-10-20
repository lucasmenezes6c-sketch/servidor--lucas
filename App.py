from flask import Flask, render_templast

app = Flask(__name__ )
@app.route('/')
def home():
    return render_templast ('index,html')

if __name__ == '__main__':
    app.run()