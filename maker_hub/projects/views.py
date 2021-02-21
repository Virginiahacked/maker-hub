"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint(
    "projects_bp",
    __name__,
    template_folder="templates",
    url_prefix="/projects",
    static_folder="../static",
)


@blueprint.route("/")
@login_required
def landing():
    """Projects landing page."""
    return render_template("projects.html")
