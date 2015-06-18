from django import forms


class TotalForm(forms.Form):

    line_total = forms.CharField('Cart Sub Total')
    tax = forms.IntegerField('Eco Tex')
    shipping = forms.CharField('Shipping Cost')
    total = forms.IntegerField('Total')
