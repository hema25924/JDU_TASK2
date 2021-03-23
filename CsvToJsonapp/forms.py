from django import forms

class UserInput(forms.Form):
    CATEGORY_CHOICES =( 
    ("student", "Student"),
    ("teacher", "Teacher"),
    )
    category = forms.ChoiceField(choices = CATEGORY_CHOICES)
    age = forms.IntegerField(label='Enter Minimum age', label_suffix=' ',
                             help_text='years')
    name = forms.CharField(label='Enter Name', label_suffix=' ',
                           widget=forms.TextInput(attrs={'size': '40'}))
