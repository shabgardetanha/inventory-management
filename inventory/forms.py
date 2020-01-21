from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    #FIXME: fix the following code to something that doesn't look like garbage
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['stock_type'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Stock
        fields = ['name', 'stock_type', 'description', 'quantity', 'price']
        widgets = {
            'description' : forms.Textarea(
                attrs = {
                    'class' : 'textinput form-control'
                }
            )
        }