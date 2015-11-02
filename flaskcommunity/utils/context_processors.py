

from flask import current_app


def get_site_name():
    """ Gets the name of the site. """
    return {'site_name': current_app.config['SITE_NAME']}


def configure_context_processors(app):
    app.template_context_processors[None].append(get_site_name)
