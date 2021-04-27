from flask import Flask, render_template, request
import math
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main():
    return render_template('login.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'Username - ' + name + ', user id - ' + str(id)


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/find', methods=['post', 'get'])
def login():
    summa = request.form['summa']
    percents = request.form['percents']
    month = request.form['month']
    title = 'Here are your results'
    amount_per_month = get_amount_of_payment_per_month(summa, month, percents) #str(phrase)
    amount_per_all_period = get_amount_per_all_period(amount_per_month, month)
    return render_template('results.html', the_title=title,
                           summma=summa, percents=percents,
                           amount_per_month=amount_per_month, month=month, amount_per_all_period=amount_per_all_period)


def get_amount_per_all_period(amount_per_month, month):
    return math.ceil(amount_per_month * int(month))


def get_amount_of_payment_per_month(summa, month, percent):
    r = int(percent) / (100 * int(month))
    result = int(summa) * r * pow((1 + r), int(month)) / (pow((1 + r), int(month)) - 1)
    return math.ceil(result)


    # message = ''
    # username = None
    # password = None
    # if request.method == 'POST':
    #     username = request.form.get('username')  # запрос к данным формы
    #     password = request.form.get('password')
    #     if username == 'root' and password == 'pass':
    #         message = "Correct username and password"
    #     else:
    #         message = "Wrong username or password"
    # print('tut')
    #
    # return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run()
