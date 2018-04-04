from flask import render_template
from web import app



#====================================================================
#====================================================================
#====================================================================




@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/red', methods=['GET', 'POST'])
def red():
    return render_template('red.html')

@app.route('/white', methods=['GET', 'POST'])
def white():
    return render_template('white.html')