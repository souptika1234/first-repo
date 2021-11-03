from flask import Flask as x
app=x(__name__)

@app.route('/soumi')
def hello():
    return "<body bgcolor='red' text='yellow'><h1>HI I am Soumi...</h1></body>"

@app.route('/ishita')
def hello2():
    return "<body bgcolor='green' text='yellow'><h1>HI I am Ishita...</h1></body>"
if __name__=='__main__':
    app.run()