from http.cookiejar import cut_port_re

from flask import Flask, render_template, request, redirect, url_for, session
import sys
from pathlib import Path

from src.account.account import getUserVector

currentDir = Path(__file__).resolve().parent.parent
currentDir = currentDir / 'account'
sys.path.append(str(currentDir))

import account

currentDir = currentDir.parent
currentDir = currentDir / 'ai'
sys.path.append(str(currentDir))

import getPfvector, getNsimilarmovies

app = Flask(__name__)
app.secret_key = "one_two_tree"

account.initializeDatabase()


# Add a user to the list
def add_to_group(username):
    if "group_members" not in session:
        session["group_members"] = []  # Initialize if not set

    if username not in session["group_members"]:
        session["group_members"].append(username)
    session.modified = True

# Get the group members
def get_group():
    return session.get("group_members", [])  # Return empty if not found


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    username = session.get('username')

    if not username:
        return redirect(url_for('login'))  # Checks if the user is in

    if request.method == "POST":
        # Initialize data_list with all zeros
        data_list = [0, 0, 0, 0, 0, 0, 0]


        # Get selected genres
        selected_genres = request.form.getlist("GenresQuestion[]")
        family_genre = request.form.get("FamilyGenre")
        rating = request.form.get("RatingQuestion")

        # oh yeah genre map
        genre_map = {
            "Action Adventure": 0,
            "Horror & Thriller": 1,
            "Sci-Fi & Fantasy": 2,
            "Drama & Romance": 3,
            "Historic": 4,
        }

        # Update data_list based on selected genres
        for genre in selected_genres:
            if genre in genre_map:
                data_list[genre_map[genre]] = 1  # marks which options were picked
        if family_genre == "Yes":
            data_list[5] = 1
        data_list[6] = int(rating)

        # Store the completed survey in the database
        account.setUserPreferences(username, data_list)

        return redirect(url_for("home"))

    # For GET request, just display the survey page with an empty form
    return render_template("survey.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if account.verifyUserLogin(username, password):
            session.clear()
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"

    return render_template("login_screen.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if account.doesUserExist(username):
            return "Username already exists"
        else:
            if account.createUser(username, password, None) == 0:
                session['username'] = username
                return redirect(url_for("home"))
            else:
                return "Error creating user"

    return render_template("register.html")

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == "POST":
        addUser = request.form.get("addUser")


        if account.doesUserExist(addUser):
            add_to_group(addUser)
            return redirect(url_for("home"))
        else:
            return "User not found"

@app.route('/results', methods=['GET', 'POST'])
def results():
    data = []
    if request.method == "GET":
        add_to_group(session["username"])
        res = [account.getUserVector(user) for user in session['group_members'] if account.getUserVector(user) != -1]
        groupPfvector = getPfvector.getPfvector(res)
        data = getNsimilarmovies.getNsimilarmovies(5, groupPfvector)
        for row in data:
            row[1] = ", ".join(row[1])
    return render_template("results.html", data=data)


@app.route('/home')
def home():
    username = session.get('username')

    if not username:
        return redirect(url_for('login'))  # makes sure the user is logged in

    user_preference = account.getUserVector(username)

    # If user preference is equal -1 it means the user is new
    if user_preference == -1:
        return redirect(url_for("survey"))

    return render_template("home.html", user_name=username, group_members=get_group())


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
