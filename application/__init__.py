from flask import Flask


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Include routes
        from . import routes

        # Register blueprints
        # app.register_blueprint(routes.main_bp)

        return app
