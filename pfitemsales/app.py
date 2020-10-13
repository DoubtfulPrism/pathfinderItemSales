import os
import sys
import flask

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from pfitemsales.infrastructure.view_modifiers import response

app = flask.Flask(__name__)


def get_latest_catagories():
    return [
        {'name': 'armour'},
        {'name': 'weapons'},
        {'name': 'rings'}
    ]


@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_catagories()
    return {'catagories': test_packages}
    # return flask.render_template('home/index.html', catagories=test_packages)


@app.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
    # return flask.render_template('home/about.html')


if __name__ == '__main__':
    app.run(debug=True)
