import flask
import flask_restx

from . import constants
from . import site


class Constants(constants.V1ApiConstants):

    pass


blueprint = flask.Blueprint(
    f'{Constants.AppNameClean} - {Constants.Version}',
    __name__,
    url_prefix=f'/api/{Constants.Version}'
    )

api = flask_restx.Api(
    app=blueprint,
    title=Constants.AppNameClean,
    version=f'{Constants.Version}.0',
    description=None,
    terms_url=None,
    license=None,
    license_url=None,
    contact=None,
    contact_url=None,
    contact_email=None,
    authorization=Constants.Authorization,
    security=Constants.Security,
    doc='/',
    default='default',
    default_label='{Constants.Version} namespaces.',
    Validate=None,
    tags=None,
    prefix='',
    ordered=False,
    default_mediatype='application/json',
    decorators=None,
    catch_all_404s=False,
    serve_challenge_on_401=False,
    format_checker=None
    )

api.add_namespace(site.namespace)
