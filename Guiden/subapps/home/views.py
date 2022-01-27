from flask import current_app, render_template
import pymongo

from Guiden import mongo


def home():
    context = dict()
    context['news'] = mongo.db.news \
        .find() \
        .sort('edited_at', pymongo.DESCENDING) \
        .limit(current_app.config['HOME_NEWS_LIMIT'])
    context['premieres'] = mongo.db.anime \
        .find() \
        .sort('premiere_date', pymongo.DESCENDING) \
        .limit(current_app.config['HOME_PREMIERES_LIMIT'])
    return render_template('home.j2', **context)
