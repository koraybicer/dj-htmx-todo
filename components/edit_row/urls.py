from django.urls import path

from components.edit_row.row import RowEditRowComponent

urlpatterns = [
    path(
        "todo/<int:id>",
        RowEditRowComponent.as_view(),
        name="row_edit_row",
    ),
]