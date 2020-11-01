from django import forms
from .models import Post
from .models import Author
from .models import Catogory
from datetime import datetime 


class PostForm(forms.ModelForm):
    title       = forms.CharField(label='Title of New Post', required=False,widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    
    create_date = forms.DateTimeField(initial=datetime.now, required=False)

    author = forms.ModelChoiceField(queryset=Author.objects.all())
    catogory = forms.ModelChoiceField(label='Category',queryset=Catogory.objects.all())

    description = forms.CharField(label='Description', required=False,widget=forms.TextInput(attrs={"placeholder": "Description"}))
    body = forms.CharField(
                        label='',
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Body of your post",
                                    "class": "new-class-name",
                                    "id": "textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    
    image_url = forms.CharField(initial="header.jpeg",required=False, label='Image File Directory', 
                    widget=forms.TextInput())

    
    class Meta:
        model = Post
        fields = [
            'title',
            'create_date',
            'author',
            'catogory',
            'description',
            'body',
            'image_url'
        ]
