from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == username and password == password:
            return "Login Success"
        else:
            return "Invalid username or password, please try again"

    return render_template('login_screen.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        return f"Account {username} has been created. Please login."

    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
