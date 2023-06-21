from flask_restx import Namespace

from .constants import NamespaceConstants as Constants


namespace = Namespace(
    Constants.SCOPE,
    description=Constants.DESC,
    path=None,
    decorators=None,
    validate=None,
    authorizations=Constants.Authorization,
    ordered=False,
    security=Constants.Security
    )
