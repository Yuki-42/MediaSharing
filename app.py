"""
The main file for the MediaHost project.
"""

# Standard Library Imports
from os import environ, getcwd
from pathlib import Path
from secrets import token_urlsafe as tokenUrlSafe

# Third Party Library Imports
from flask import Flask, Blueprint, render_template as render, request, redirect, url_for as urlFor, flash, session
from dotenv import load_dotenv as loadDotenv

# Package Relative Imports
from internals.logging_ import createLogger, SuppressedLoggerAdapter, EndpointLoggerAdapter
from internals.config import Config

# Load the environment variables
loadDotenv()

# Load the config
config: Config = Config()

# Create the loggers
logger: SuppressedLoggerAdapter = createLogger("Main", level=config.loggingLevel)
endpointLogger: EndpointLoggerAdapter = createLogger("Endpoint", adapterMode="endpoint", level=config.loggingLevel)

# Create the app
app: Flask = Flask(__name__)
app.debug = config.debug
app.secret_key = tokenUrlSafe(32)

# Email regex used for validation
emailRegex: str = r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"

# Define blueprints
api: Blueprint = Blueprint("api", __name__, url_prefix="/api")
admin: Blueprint = Blueprint("admin", __name__, url_prefix="/admin")
auth: Blueprint = Blueprint("auth", __name__, url_prefix="/auth")


# Create the index route
@app.route("/", methods=["GET"])
def index() -> str:
    """
    The index route.

    Returns:
        str: The rendered index.html file.
    """
    endpointLogger.logRequest(request)
    return render("index.html")


if __name__ == '__main__':
    # Register the blueprints
    app.register_blueprint(api)
    app.register_blueprint(admin)
    app.register_blueprint(auth)

    # Run the app
    app.run()
