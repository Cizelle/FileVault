from django import forms
from .models import FileVault

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileVault
        fields = ['encrypted_file']
        widgets = {
            'encrypted_file': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
