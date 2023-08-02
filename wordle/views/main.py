import flask

from wordle.words import is_valid_guess

blueprint = flask.Blueprint('main', __name__)

@blueprint.route('/')
def index():
    return flask.render_template('index.html')


@blueprint.route('/guess')
def guess():
    guess = flask.request.args.get('guess').lower()
    i = int(flask.request.args.get('i'))

    if not is_valid_guess(guess):
        return flask.render_template('guess/active.html', guess=guess, i=i, invalid=True)

    return flask.render_template('guess/result.html', guess=guess, word=flask.current_app.config['WORD'], i=i)


@blueprint.route('/partials/activeguess')
def activeguess():
    i = int(flask.request.args.get('i'))

    return flask.render_template('guess/active.html', i=i)


@blueprint.route('/victory')
def victory():
    i = int(flask.request.args.get('i'))

    return flask.render_template('victory.html', word=flask.current_app.config['WORD'], guesses=i)