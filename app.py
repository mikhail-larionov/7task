from flask import Flask, render_template, request
import math
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main():
    return render_template('entry.html')


@app.route('/find', methods=['post'])
def calculate():
    summa = request.form['summa']
    percents = request.form['percents']
    month = request.form['month']
    title = 'Ваши результаты'
    amount_per_month = get_amount_of_payment_per_month(summa, month, percents)
    amount_per_all_period = get_amount_per_all_period(amount_per_month, month)
    return render_template('results.html', the_title=title,
                           summma=summa, percents=percents,
                           amount_per_month=amount_per_month, month=month, amount_per_all_period=amount_per_all_period)


def get_amount_per_all_period(amount_per_month, month):
    return int(amount_per_month * int(month))


def get_amount_of_payment_per_month(summa, month, percent):
    r = int(percent) / 1200
    result = int(summa) * r * pow((1 + r), int(month)) / (pow((1 + r), int(month)) - 1)
    return int(result)


if __name__ == '__main__':
    app.run()
