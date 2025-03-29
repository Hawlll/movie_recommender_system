from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # Get responses from the form
        name = request.form.get("name")
        q1 = request.form.get("question1")
        q2 = request.form.get("question2")
        q3 = request.form.get("question3")

        # Store or process the data (for now, just displaying)
        return render_template('results.html', name=name, q1=q1, q2=q2, q3=q3)

    return render_template('survey.html')

if __name__ == '__main__':
    app.run(debug=True)
