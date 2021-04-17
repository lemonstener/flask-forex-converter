from flask import Flask, flash, request, redirect, render_template
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'forexccccccc'

c = CurrencyRates()
cc = CurrencyCodes()

currencies = c.get_rates('USD')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    curr_from = request.form['from'].upper()
    curr_to = request.form['to'].upper()
    amount = request.form['amount']
    errors = False
    if currencies.__contains__(curr_from) == False:
        erros = True
        flash(f'Invalid currency code to convert from: "{curr_from}"', 'error')
    if currencies.__contains__(curr_to) == False:
        errors = True
        flash(f'Invalid currency code to convert to: "{curr_to}"', 'error')
    try:
        float(amount)
    except:
        errors = True
        flash(f'Invalid amount: "{amount}"', 'error')

    if errors == True:
        return redirect('/')
    else:
        symbol_to = cc.get_symbol(curr_to)
        symbol_from = cc.get_symbol(curr_from)
        result = c.convert(curr_from, curr_to, float(amount))
        display = symbol_to + ' ' + str(round(result, 2))
        flash(f'{symbol_from} {amount} amounts to {display}', 'success')
        return redirect('/')
