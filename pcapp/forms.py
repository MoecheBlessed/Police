from django import forms

from . models import Record, Criminal, Staff, Crime


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = '__all__'


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = 'status'


class CriminalForm(forms.ModelForm):
    class Meta:
        model = Criminal
        fields = '__all__'


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class CrimeForm(forms.ModelForm):

    class Meta:
        model = Crime
        fields = '__all__'

