import toml

from wordle.create_app import create_app

config = toml.load('config.toml')

app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True)
