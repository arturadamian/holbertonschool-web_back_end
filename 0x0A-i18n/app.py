#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, render_template, request, g
from os import getenv
from flask_babel import Babel, gettext
import pytz
import datetime


app = Flask(__name__)


class Config:
    """ class config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """best match locale lang"""
    local_lang = request.args.get('locale')
    support_lang = app.config['LANGUAGES']
    if local_lang in support_lang:
        return local_lang
    user_id = request.args.get('login_as')
    if user_id:
        local_lang = users[int(user_id)]['locale']
        if local_lang in support_lang:
            return local_lang
    local_lang = request.headers.get('locale')
    if local_lang in support_lang:
        return local_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ get user by ID"""
    try:
        user_id = request.args.get('login_as')
        return users[int(user_id)]
    except Exception:
        return None


def get_timezone():
    """ getting timezone"""
    local_timezone = request.args.get('timezone')
    if local_timezone:
        if local_timezone in pytz.all_timezones:
            return local_timezone
        else:
            raise pytz.exceptions.UnknownTimeZoneError
    try:
        user_id = request.args.get('login_as')
        user = users[int(user_id)]
        local_timezone = user['timezone']
    except Exception:
        local_timezone = None
    if local_timezone:
        if local_timezone in pytz.all_timezones:
            return local_timezone
        else:
            raise pytz.exceptions.UnknownTimeZoneError
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    """before request"""
    g.user = get_user()
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    local_time_now = utc_now.astimezone(pytz.timezone(get_timezone()))


@app.route('/')
def index():
    """hello world"""
    return render_template("index.html")


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
