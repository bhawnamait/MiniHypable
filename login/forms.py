
from models import Articles

from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'body', 'pub_date', 'thumbnail')

'''
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body','name')
'''