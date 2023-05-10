from django import forms
from .models import Post, Category


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'categories']

    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs= {"class": "form-control", "placeholder": "Title of Your Blog"}
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs= {"class": "form-control"}
        )
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects,
        widget=forms.SelectMultiple(
            attrs={"class": "form-control"},
        ),
        help_text = "Press ctrl in keyborad to select more categories."
    )
