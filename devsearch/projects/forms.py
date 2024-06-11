from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        #fields = '__all__'
        project_fields = Project._meta.fields
        fields = [field.name for field in project_fields if field.name not in ['id', 'owner', 'created']]
        fields.append('tag')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text'})
