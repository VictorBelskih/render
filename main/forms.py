from django import forms
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='Ваш email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
             'class': 'input100',
             'id': 'form3Example3c',
             'placeholder': 'Полное имя',
            }
        )

        self.fields['email'].widget.attrs.update(
            {
             'class': 'input100',
             'placeholder': 'Email'
            }
        )
        self.fields['message'].widget.attrs.update(
            {
             'class': 'input100',
             'placeholder': 'Текст сообщения'
             }
        )