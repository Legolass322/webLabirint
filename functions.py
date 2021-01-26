from flask import url_for


def set_urls(params):
    # setup urls
    params['css'] = url_for('static', filename='css/')
    params['js'] = url_for('static', filename='js/')
    params['img'] = url_for('static', filename='img/')