from flask import render_template


def search_page(page: int):
    return render_template('search.j2')
