
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == "POST":
        # Initialize data_list with all zeros
        data_list = [0, 0, 0, 0, 0, 0, 0]

        # Get selected genres
        selected_genres = request.form.getlist("GenresQuestion[]")
        family_genre = request.form.get("FamilyGenre")
        rating = request.form.get("RatingQuestion")

        # Mapping genres to their respective indexes in data_list
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
                data_list[genre_map[genre]] = 1 # marks which options were picked
        if family_genre == "Yes":
            data_list[5] = 1
        data_list[6] = int(rating)


        print(data_list)

        # Pass the result and user to the next page
        return render_template("survey.html", data=data_list)

    # For GET request, just display the survey page with an empty form
    return render_template("survey.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == username and password == password:
            return redirect(url_for("home"))
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

@app.route('/home')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
