"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint(
    "user", __name__, url_prefix="/dashboard", static_folder="../static"
)


@blueprint.route("/")
@login_required
def dashboard():
    """User dashboard."""
    return render_template("users/dashboard.html")
