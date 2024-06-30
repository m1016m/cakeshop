from django import forms
from .models import Profile, Order, Cake
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['address', 'phone']
class OrderForm(forms.ModelForm):
    cake = forms.ModelChoiceField(queryset=Cake.objects.all(), empty_label="Select Cake")

    class Meta:
        model = Order
        fields = ['cake', 'quantity']
# from django import forms
# from .models import Profile
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile, Order, Cake

# class ProfileForm(forms.ModelForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = Profile
#         fields = ['address', 'phone']

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user
# class OrderForm(forms.ModelForm):
#     cake = forms.ModelChoiceField(queryset=Cake.objects.all(), empty_label="Select Cake")

#     class Meta:
#         model = Order
#         fields = ['cake', 'quantity']
