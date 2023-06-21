from flask import Flask


app = Flask(
    __name__,
    static_url_path=None,
    static_folder='static',
    static_host=None,
    host_matching=False,
    subdomain_matching=False,
    template_folder='templates',
    instance_path=None,
    instance_relative_config=False,
    root_path=None
    )
