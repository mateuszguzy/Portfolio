from django import forms
from django.forms import SelectDateWidget


class SearchForm(forms.Form):
    pages_to_search = forms.IntegerField(label='How many pages would you like to check:')
    date_in = forms.DateField(label='Check-in date:', widget=SelectDateWidget())
    date_out = forms.DateField(label='Checkout date:', widget=SelectDateWidget())
    adults = forms.IntegerField(label='Adults:')
    pets = forms.IntegerField(label='Pets:')
    house = forms.BooleanField(required=False)  # 1
    apartment = forms.BooleanField(required=False)  # 2
    cabin = forms.BooleanField(required=False)  # 4
    bungalow = forms.BooleanField(required=False)  # 38
    cottage = forms.BooleanField(required=False)  # 60
    bedrooms = forms.IntegerField(label='Bedrooms:')
    beds = forms.IntegerField(label='Beds:')
    bathrooms = forms.IntegerField(label='Bathrooms:')


class ChooseCurrency(forms.Form):
    choice = forms.ChoiceField(required=False, label=False, choices=(("USD", "USD"),
                                                                     ("EUR", "EUR"),
                                                                     ("GBP", "GBP"),
                                                                     ("DKK", "DKK"),
                                                                     ("PLN", "PLN"),
                                                                     ))


class FilterForm(forms.Form):
    choice = forms.ChoiceField(required=False, label=False, choices=(("", "None"),
                                                                     ("location", "Location"),
                                                                     ("max_guests", "Max Guests"),
                                                                     ("price", "Price"),
                                                                     ("title", "Title"),
                                                                     ))
