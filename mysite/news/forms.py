from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "is_published", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "rows": 5}
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r"\d", title):
            raise ValidationError("Название не должно начинаться с цифры")
        return title

    # title = forms.CharField(max_length = 150, label='Название',widget=forms.TextInput(
    #     attrs={'class': 'form-control'}))
    # content = forms.CharField(label = 'Текст', required= 'False',widget=forms.Textarea(
    #     attrs={
    #         'class': 'form-control',
    #         'rows': 5
    # }))
    # is_published = forms.BooleanField(label = 'Опубликовано',initial='True')
    # category = forms.ModelChoiceField(queryset= Category.objects.all(),label = 'Категория',
    # empty_label = 'Выберите категорию', widget=forms.Select( attrs={'class': 'form-control'}))
