from django.urls import path
from . import views

urlpatterns = [
    path(
        "ApplicationType/",
        views.ApplicationTypeView.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "ApplicationType/<uuid:pk>/",
        views.ApplicationTypeView.as_view(
            {
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "Pattern/",
        views.PatternView.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "Pattern/<uuid:pk>/",
        views.PatternView.as_view(
            {
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
]
