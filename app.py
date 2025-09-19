from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Book Pickup Page
@app.route('/book_pickup', methods=["GET", "POST"])
def book_pickup():
    if request.method == "POST":
        name = request.form['name']
        address = request.form['address']
        waste_type = request.form['waste_type']
        # here you would save to database
        return redirect(url_for('track_order'))
    return render_template("book_pickup.html")

# Request Material Page
@app.route('/request_material', methods=["GET", "POST"])
def request_material():
    if request.method == "POST":
        name = request.form['name']
        site = request.form['site']
        material = request.form['material']
        # save to database
        return redirect(url_for('track_order'))
    return render_template("request_material.html")

# Track Order Page
@app.route('/track_order')
def track_order():
    return render_template("track_order.html")

if __name__ == '__main__':
    app.run(debug=True)
