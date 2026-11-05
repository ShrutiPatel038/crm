from flask import Flask, request, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 50000},
    {"id": 2, "name": "Phone", "category": "electronics", "price": 20000},
    {"id": 3, "name": "T-Shirt", "category": "clothing", "price": 500},
]

LOGIN_PAGE = """
<h2>Login</h2>
<form method="post">
  <input id="username" name="username" placeholder="Username">
  <input id="password" name="password" type="password" placeholder="Password">
  <button id="login-btn" type="submit">Login</button>
</form>
<p id="message">{msg}</p>
"""


@app.route("/")
def home():
    return "E-commerce Product Management App"


@app.route("/products")
def products():
    category = request.args.get("category")
    if category:
        return jsonify([p for p in PRODUCTS if p["category"] == category])
    return jsonify(PRODUCTS)


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            msg = "Login successful"
        else:
            msg = "Invalid username or password"
    return LOGIN_PAGE.format(msg=msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
