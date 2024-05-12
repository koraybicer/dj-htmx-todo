from django.http import HttpResponse
from django_components import component

from todos.models import Todo


@component.register("table_edit_row")
class TableEditRowComponent(component.Component):
    template = """
        <table class="table">
            <thead class="thead">
                <tr>
                    <th scope="col" class="th">Title</th>
                    <th scope="col" class="th"></th>
                </tr>
            </thead>
            <tbody id="tbody" hx-target="closest tr" hx-swap="outerHTML">
                {% for todo in todos %}
                    {% component "row_edit_row" todo=todo only %}{% endcomponent %}
                {% endfor %}
            </tbody>
        </table>
    """

    def get_context_data(self, **kwargs):
        return {"todos": Todo.objects.all().order_by("id")[:5]}  # remove limit