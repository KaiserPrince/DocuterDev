from django import forms
from .models import MyDataModel
from .models import SchoolDetailModel

class SchoolDetailForm(forms.ModelForm):
    class Meta:
        model = SchoolDetailModel
        fields = '__all__' 

class DataEntryForm(forms.ModelForm):

    # dropdown_field = forms.ChoiceField(choices=[
    #     ('default', '--Select the type of question--'),
    #     ('mcq', 'Multiple Choice Questions'),
    #     ('fb', 'Fill In The Blanks'),
    # ])

    class Meta:
        model = MyDataModel
        fields = '__all__' 
