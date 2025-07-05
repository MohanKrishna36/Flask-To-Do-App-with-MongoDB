from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes after app is created (to avoid circular imports)
    from flask_app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def create_app():
    app = Flask(__name__)

    app.secret_key = "mohan123$flasktodo"

    # -- custom Jinja filter --
    app.add_template_filter(lambda oid: str(oid)[-6:], name="last6")

    from flask_app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
