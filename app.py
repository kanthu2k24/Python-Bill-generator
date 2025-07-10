from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    base_price = 300
    extra_cheese = 100 if 'cheese' in request.form else 0
    extra_toppings = 100 if 'toppings' in request.form else 0
    water = 40 if 'water' in request.form else 0
    ketchup = 10 if 'ketchup' in request.form else 0
    soft_drink = 150 if 'softdrink' in request.form else 0
    take_out = 20 if 'takeout' in request.form else 0

    total = base_price + extra_cheese + extra_toppings + water + ketchup + soft_drink + take_out
    gst = round(total * 0.18, 2)

    return render_template('bill.html', base_price=base_price, extra_cheese=extra_cheese,
                           extra_toppings=extra_toppings, water=water, ketchup=ketchup,
                           soft_drink=soft_drink, take_out=take_out, gst=gst)

if __name__ == '__main__':
    app.run(debug=True)
