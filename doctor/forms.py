from django import forms
from doctor.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"
