from django import forms
from django.core.validators import FileExtensionValidator

class DocumentForm(forms.Form):
    file = forms.FileField(
        validators = [
            FileExtensionValidator([
                'png',
                'jpg',
                'gif',
                'tif',
                'bmp',
                'pdf',
                'tiff'
            ])
        ]
    )
