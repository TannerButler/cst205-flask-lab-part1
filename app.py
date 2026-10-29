from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Replace these sample names/acronyms with answers from three real classmates.
classmate_acronyms = [
    ('Alex', 'BRB', 'Be Right Back'),
    ('Jordan', 'IMO', 'In My Opinion'),
    ('Sam', 'IDK', "I Don't Know"),
]


@app.route('/')
def home():
    # Task 2: Generate HTML in the Python view, without a template.
    html = '<h1>Classmate Acronyms</h1>'
    for name, acronym, meaning in classmate_acronyms:
        html += f'<p>{name}: {acronym} ({meaning})</p>'
    return html


@app.route('/tanner')
def tanner():
    # Task 3: Pass a Python variable into a Jinja template.
    return render_template('template.html', favorite_acronym='TIL (Today I Learned)')


@app.route('/photo')
def photo():
    # Task 4: Bootstrap classes + directly linked Lorem Picsum image.
    return render_template('photo.html')


if __name__ == '__main__':
    app.run(debug=True)
