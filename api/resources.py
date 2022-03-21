from import_export import resources
from .models import Usuario


class UsersResource(resources.ModelResource):
    class Meta:
        model = Usuario
