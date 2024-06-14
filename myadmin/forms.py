from django import forms
from myadmin.models import Category,Subcategory,Blog
from .models import Contact,Ebook
from django.contrib.auth.models import User

# Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'image']

# Subategory Form
class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['cat_id','subcategory_name', 'image']


# Subategory Form
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['post_name', 'post_title', 'category_id', 'subcategory_id', 'details', 'image', 'audio', 'section', 'slug', 'status', 'publish_date', 'author','main_post']

        
class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
    


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'email', 'phone_number', 'query']


class SubscriptionForm(forms.Form):
    email = forms.EmailField(label='Enter your email:')


class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['title', 'author', 'description', 'price', 'file']