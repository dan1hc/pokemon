from flask import Blueprint
from flask_restx import Api

from . import constants
from . import healthz


class Constants(constants.CommonApiConstants):

    pass


blueprint = Blueprint(
    f'{Constants.AppNameClean} - Common',
    __name__
    )

api = Api(
    app=blueprint,
    title=Constants.AppNameClean,
    version=None,
    description=None,
    terms_url=None,
    license=None,
    license_url=None,
    contact=None,
    contact_url=None,
    contact_email=None,
    authorization=None,
    security=None,
    doc='/',
    default='default',
    default_label='healthz namespaces.',
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

api.add_namespace(healthz.namespace)
