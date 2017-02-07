from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config.from_pyfile('config.py')
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/track")
def track():
    return render_template('under_construction.html')


@app.route('/showLost')
def showLost():
    return render_template('lostBaggage.html')

@app.route('/reportLost', methods=['POST'])
def reportLost():

    try:
        # read the posted values from the UI
        _name = request.form['inputName']
        _address = request.form['inputAddress']
        _telephone = request.form['inputTelephone']
        _email = request.form['inputEmail']
        _bookid = request.form['inputBookId']

        # validate the received values
        if _name and _email and _address and _telephone and _bookid:

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_reportLostBg',(_name, _address, _telephone, _email, _bookid))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                conn.close()
                locateDevice()
                return_msg = "{'message': 'User created successfully !'}"
                return json.dumps(return_msg)
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})

def locateDevice():
    conn = mysql.connect()
    cursor = conn.cursor()
    conn.close()
    print json.dumps({'html': '<span>Locate Device Def</span>'})


if __name__ == "__main__":
    app.run(debug=True)
