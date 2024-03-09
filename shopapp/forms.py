from django import forms


class AddProduct(forms.Form):
    prod_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()


class EditProduct(forms.Form):
    prod_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()

class ImageForm(forms.Form):
    image = forms.ImageField()