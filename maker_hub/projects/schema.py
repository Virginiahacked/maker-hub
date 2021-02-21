"""Schema for Projects."""
from maker_hub.extensions import ma
from maker_hub.projects.models import Project


class ProjectSchema(ma.SQLAlchemySchema):
    """Project Schema."""

    class Meta:
        """Project Schema Meta information."""

        model = Project

    id = ma.auto_field()
    name = ma.auto_field()
    description = ma.auto_field()
    owner = ma.auto_field()
    public = ma.auto_field()
    created = ma.auto_field()
    updated = ma.auto_field()
