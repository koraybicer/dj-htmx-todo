from django_components import component

from todos.models import Todo


@component.register("row_edit_row")
class RowEditRowComponent(component.Component):
    template = """
        {% if not editing %}
            <tr class="tr {% if todo.id in ids %} {{ update }} {% endif %}">
                <td class="td">{{ todo.title }}</td>
                
                <td class="td">
                    <button class="link" hx-get="{% url 'row_edit_row' id=todo.id %}?edit=True" hx-trigger="edit" onClick="editClick(this)">
                    Edit
                    </button>
                </td>
            </tr>
        {% else %}
            <tr hx-trigger='cancel' class='tr editing' hx-get="{% url 'row_edit_row' id=todo.id %}">
                <td class="td-tight"><input class="input" name='title' value='{{ todo.title }}'></td>
                <td class="td-tight flex flex-row gap-1">
                    <button class="btn-secondary-small" hx-get="{% url 'row_edit_row' id=todo.id %}">
                    ✘
                    </button>
                    <button class="btn-primary-small" hx-post="{% url 'row_edit_row' id=todo.id %}" hx-include="closest tr">
                    ✓
                    </button>
                </td>
            </tr>
        {% endif %}
    """

    js = """
        function editClick(e) {
            let editing = document.querySelector(".editing");
            if (editing) {
                let changeRow = confirm(
                    "Hey!  You are already editing a row!  Do you want to cancel that edit and continue?"
                );

                if (changeRow) {
                    htmx.trigger(editing, "cancel");
                } else {
                    return;
                }

                htmx.trigger(e, "edit");
            } else {
                htmx.trigger(e, "edit");
            }
        }
    """

    def get(self, request, id, *args, **kwargs):
        editing = request.GET.get("edit", False)
        todo = Todo.objects.get(id=id)
        context = {"todo": todo, "editing": editing}
        return self.render_to_response(context)

    def post(self, request, id, *args, **kwargs):
        todo = Todo.objects.get(id=id)
        todo.title = request.POST.get("title")
        todo.save()
        return self.render_to_response({"todo": todo, "editing": False})

    def get_context_data(self, todo, **kwargs):
        return {"todo": todo}