import flask_restx

from . import constants


class Constants(constants.CommonApiConstants):

    NAMESPACE   = 'healthz'
    DESCRIPTION = 'Health check endpoints.'


namespace = flask_restx.Namespace(
    Constants.NAMESPACE,
    description=Constants.DESCRIPTION
    )


@namespace.route('/')
class HealthCheck(flask_restx.Resource):

    def get(self):
        """Basic health check."""
        return 'OKAY', 200


@namespace.route('/synthetic')
class SyntheticCheck(flask_restx.Resource):

    def get(self):
        """Synthetic health check."""
        return 'OKAY', 200


@namespace.route('/orch')
class OrchestrationCheck(flask_restx.Resource):

    def get(self):
        """Orchestration health check."""
        return 'OKAY', 200


@namespace.route('/lb')
class LoadBalancerCheck(flask_restx.Resource):

    def get(self):
        """LoadBalancer health check."""
        return 'OKAY', 200
