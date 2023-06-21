import os
import setuptools


PACKAGE_NAME = 'api'
VERSION = os.getenv('VERSION')
INSTALL = [
    'pandas',
    'flask==1.1.1',
    'flask_restx==1.1.0',
    'flask_caching==1.10.1',
    'flask_cors==3.0.10',
    'flask_login==0.5.0',
    'itsdangerous==2.0.1',
    'pyjwt==1.7.1',
    'werkzeug==2.0.3',
    'jinja2<3.1.0'
    ]

if __name__ == '__main__':
    setuptools.setup(
        name=PACKAGE_NAME,
        version=VERSION,
        install_requires=INSTALL,
        packages=setuptools.find_packages(),
        package_data={
            PACKAGE_NAME: [
                'static/*'
                ]
            },
        license='GPL'
        )
