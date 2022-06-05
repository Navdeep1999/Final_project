import imp
from sre_constants import BRANCH
from django import forms

class DegreeForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    branch = forms.CharField(label='Branch', max_length=40)
    
    
class StudentsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=51)
    roll_number = forms.CharField(label="RollNumber", max_length=20)
    year = forms.CharField(label='year', max_length=51)
    dob = forms.CharField(label='Dob', max_length=51)      
    