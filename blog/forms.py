from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from .models import site_User
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content' , 'image']
"""
 title = models.CharField(max_length=200)
    author = models.ForeignKey(site_User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']



class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    profile_pic = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = site_User
        fields = UserCreationForm.Meta.fields + ('bio', 'profile_pic',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = site_User
        fields = ['username', 'bio', 'profile_pic']