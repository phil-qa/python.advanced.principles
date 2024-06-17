from flask import Flask, jsonify

app = Flask(__name__)

# Sample stock data
stocks = {
    'AAPL': 150.12,
    'GOOGL': 2750.45,
    'MSFT': 300.22,
    'AMZN': 3400.45
}

@app.route('/stock/<symbol>', methods=['GET'])
def get_stock_price(symbol):
    try:
        symbol = symbol.upper()
        if symbol in stocks:
            return jsonify({'symbol': symbol, 'price': stocks[symbol]})
        else:
            return jsonify({'error': 'Stock not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Failed to start the server: {e}")
