from flask_cors import CORS

from .apis.common import blueprint as healthz
from .apis.v1 import blueprint as apiv1
from .config import app


CORS(
    app=app,
    resources={
        r'/*': {
            'origins': '*'
            },
        r'/api/v1/*': {
            'origins': '*'
            }
        }
    )

app.register_blueprint(healthz)
app.register_blueprint(apiv1)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
