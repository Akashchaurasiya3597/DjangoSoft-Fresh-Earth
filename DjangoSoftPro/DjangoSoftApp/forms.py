
from .models import FeedbackDatabase,ContactDatabase


from django import forms
from multiselectfield import MultiSelectFormField


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )


    ratting = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )
    Feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )


class ContactForm(forms.Form):
    Name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    Mobile_Number = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile Number'
            }
        )
    )
    Email = forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email ID'
            }
        )
    )
    COURSES_CHOICES = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('UI', 'UI'),
        ('Rest API', 'Rest API'),
        ('Flask', 'Flask'),
        ('MySQL', 'MySQL')
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES, label="Select Your Required Courses")
    TRAINERS_CHOICES = (
        ('Narayana', 'Narayana'),
        ('Mahesh', 'Mahesh'),
        ('Mohan Reddy', 'Mohan Reddy'),
        ('Srinivas', 'Srinivas'),
        ('Wilson', 'Wilson')
    )
    trainers = MultiSelectFormField(choices=TRAINERS_CHOICES, label="Select Your Required Trainer:")
    LOCATIONS_CHOICES = (
        ('Hyd', 'Hyd'),
        ('Bang', 'Bang'),
        ('Pune', 'Pune'),
        ('Delhi', 'Delhi'),
        ('Chennai', 'Chennai')
    )
    locations = MultiSelectFormField(choices=LOCATIONS_CHOICES, label="Select Your Required Locations")
    SHIFTS_CHOICES = (
        ('Morning', "Morning"),
        ('After Noon', "After Noon"),
        ('Evening', 'Evening'),
        ('Night', 'Night')
    )
    shifts = MultiSelectFormField(choices=SHIFTS_CHOICES,label="Select Your Comfortable Shifts")
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', "Female")
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=GENDER_CHOICES,
        label="Select Your Gender:"
    )
    start_date = forms.DateField(
        widget=forms.SelectDateWidget()
    )


