from django.urls import path, include

urlpatterns = [
    path("edit_row/", include("components.edit_row.urls")),
]
