from django import forms

from catalog.models import Product


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    danger_items = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                    'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        exclude = ('last_update',)

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')

        if cleaned_name.lower() in self.danger_items:
            raise forms.ValidationError('Указанное имя запрещено!')

        return cleaned_name

    def clean_overview(self):
        cleaned_overview = self.cleaned_data.get('overview')

        if cleaned_overview.lower() in self.danger_items:
            raise forms.ValidationError('Указанное описание запрещено!')

        return cleaned_overview
