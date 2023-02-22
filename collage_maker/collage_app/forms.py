from django import forms

class CollageForm(forms.Form):
    # for collage styles
    collage_styles = [
        ('1', 'Style 1'),
        ('2', 'Style 2')
    ]

    style = forms.ChoiceField(label='Collage Style', choices=collage_styles, widget=forms.Select(attrs={'class': 'form-control'}))

    # for images
    images = forms.FileField(label='Images', required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control','id':'image-input', 'onchange':'previewFiles()', 'accept': 'image/*','multiple': True,'min':2,'max':6,'required':True}))
    