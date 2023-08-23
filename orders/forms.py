from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'payment_method']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['payment_method'].widget.attrs.update({"class": "form-control"})
        # or iterate over field to add class for each field
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':"form-control"})

        self.fields["first_name"].label = "Họ"
        self.fields["last_name"].label = "Tên"
        self.fields["address"].label = "Địa chỉ"
        self.fields["city"].label = "Thành phố"
        self.fields["payment_method"].label = "Phương thức thanh toán"
