from django import forms 

from .models import *

class PostForm (forms.ModelForm):
    class Meta:
        model = posts
        fields = {'snipet', 'category', 'title', 'body', 'image', 'create_time'}
        field_order = {'body', 'title',}
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Title'}),
            'snipet': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Snipet'}),
            'body': forms.Textarea(attrs = {'class':'form-control','placeholder':'Enter Body text'}),
            'create_time': forms.SelectDateWidget(),
        }


class EventForm (forms.ModelForm):
    class Meta:
        model = events
        fields = {'title', 'snipet', 'body', 'image', 'create_time'}
        field_order = {'title', 'snipet','create_time'}
        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Post Title'}),
            'snipet': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Snipet'}),
            'body': forms.Textarea(attrs = {'class':'form-control',}),
            'create_time': forms.SelectDateWidget(),
        }

class CommentForm (forms.ModelForm):
    class Meta:
        model = comments
        fields = {'fullname', 'subject', 'message','email','phone'}
        field_order = {'fullname', 'message'}
        widgets = {
            'fullname': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter FullName',}),
            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Enter Email Address',}),
            'subject': forms.TextInput(attrs = {'class':'form-control',}),
            'message': forms.Textarea(attrs = {'class':'form-control',}),
            'create_time': forms.SelectDateWidget(),
             'phone':forms.TextInput(attrs = {'class':'form-control','autocomplete':'off','pattern':'[0-9]+', 'title':'Enter Phone Number','placeholder':'Enter Number in this format "07000,08000 etc"'}),
        }

class UserForm (forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter First Name'}),
            'second_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Second Name'}),
            'username': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Username'}),
            'about': forms.Textarea(attrs = {'class':'form-control',}),
            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Enter Email Address',}),
            'create_time': forms.SelectDateWidget(),
        }


class UserApply (forms.ModelForm):
    class Meta:
        model = userapply
        fields = {'first_name','email', 'second_name', 'username', 'position', 'department', 'about', 'image', 'pdf', 'create_time','phone'}
        field_order = {'username','first_name'}
        widgets = {
            'first_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter First Name'}),
            'second_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Second Name'}),
            'username': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Username'}),
            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Enter Email Address',}),
            #'postition': forms.SelectMultiple(attrs = {'class':'form-control',}),
            #'department': forms.SelectMultiple(attrs = {'class':'form-control',}),
            'about': forms.Textarea(attrs = {'class':'form-control',}),
            'create_time': forms.SelectDateWidget(),
            'phone':forms.TextInput(attrs = {'class':'form-control','autocomplete':'off','pattern':'[0-9]+', 'title':'Enter Phone Number','placeholder':'Enter Number in this format "07000,08000 etc"'})
        }

