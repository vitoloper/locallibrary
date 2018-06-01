from django import forms

from django.core.exceptions import ValidationError

# Translation function
from django.utils.translation import ugettext_lazy as _

# For checking renewal date range
import datetime


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in the past'))

        # Check range is in the allowed range.
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data
