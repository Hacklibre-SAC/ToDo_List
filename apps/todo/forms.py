from django import forms

from apps.todo.models import Todo


class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        
        self.fields['TodoName'].widget.attrs.update(
            {"class": 'input_todo_list', 'placeholder': 'Ingrese item'})

    class Meta:
        model = Todo

        fields = [
            'TodoName'
        ]

        labels = {
            'TodoName': 'Nombre de la tarea',
        }
