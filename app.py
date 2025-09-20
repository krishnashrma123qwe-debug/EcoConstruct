import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route("/", methods=["GET", "HEAD"])
def home():
    return render_template("index.html")

# Book Pickup Page
@app.route("/book_pickup", methods=["GET", "POST", "HEAD"])
def book_pickup():
    if request.method == "POST":
        name = request.form['name']
        address = request.form['address']
        waste_type = request.form['waste_type']
        # Example: Save to DB or log
        print(f"Pickup request: {name}, {address}, {waste_type}")
        return redirect(url_for("track_order"))
    return render_template("book_pickup.html")

# Request Material Page
@app.route("/request_material", methods=["GET", "POST", "HEAD"])
def request_material():
    if request.method == "POST":
        name = request.form['name']
        site = request.form['site']
        material = request.form['material']
        # Example: Save to DB or log
        print(f"Material request: {name}, {site}, {material}")
        return redirect(url_for("track_order"))
    return render_template("request_material.html")

# Track Order Page
@app.route("/track_order", methods=["GET", "HEAD"])
def track_order():
    return render_template("track_order.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # for Render
    app.run(host="0.0.0.0", port=port, debug=True)
