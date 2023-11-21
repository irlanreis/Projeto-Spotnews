from django import forms
from news.models import Category, News


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=200)


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        self.fields["author"].label = "Autoria"
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )
        self.fields["image"].label = "URL da Imagem"
        self.fields["categories"] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=Category.objects.all().values_list("id", "name"),
            label="Categoria",
        )
