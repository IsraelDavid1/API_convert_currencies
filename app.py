from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount'))

    # Chama a API externa para obter a taxa de câmbio
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
    data = response.json()

    # Faz a conversão
    rate = data['rates'][to_currency]
    converted_amount = amount * rate

    return jsonify({
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount': amount,
        'converted_amount': converted_amount,
        'rate': rate
    })

if __name__ == '__main__':
    app.run(debug=True)
