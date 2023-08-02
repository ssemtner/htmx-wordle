import flask

app = flask.Flask(__name__)

word = 'hello'

valid_guesses = set()
with open('valid_guesses.txt', 'r') as f:
    for line in f:
        valid_guesses.add(line.strip())


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/guess')
def guess():
    guess = flask.request.args.get('guess').lower()
    i = int(flask.request.args.get('i'))

    if guess not in valid_guesses:
        return flask.render_template('partials/active_guess.html', guess=guess, i=i, invalid=True)

    return flask.render_template('partials/guess_results.html', guess=guess, word=word, i=i)


@app.route('/partials/activeguess')
def activeguess():
    i = int(flask.request.args.get('i'))

    return flask.render_template('partials/active_guess.html', i=i)


@app.route('/victory')
def victory():
    i = int(flask.request.args.get('i'))

    return flask.render_template('partials/victory.html', word=word, guesses=i)


if __name__ == '__main__':
    app.run(debug=True)
