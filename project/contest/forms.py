from django import forms


class ContestForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20)
    description = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '40', 'rows': '10'}),
                                  label='Описание'
                                  )
    price = forms.IntegerField(label='Цена',
                               min_value=10,
                               max_value=100,
                               help_text='Рекомендованная розничная цена')
    comment = forms.CharField(widget=forms.Textarea,
                              label='Комментарий',
                              required=False)
