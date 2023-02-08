from django import forms
from.models import Booking


class dateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets = {
            'booking_date':dateInput
        }
        labels ={
            'p_name':"Patient Name",
            'p_phone':"Patient Phone",
            'p_email':"Patient email",
            'doc_name':"Doctor name",
            'booking_date':"Booking date"
        }
