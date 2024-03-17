from django import forms
from borrow.models import BorrowList


class FormBorrow(forms.ModelForm):
    class Meta:
        model = BorrowList
        fields = ['employee_id', 'full_name', 'position']
