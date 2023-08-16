from django import forms


def get_city_form_class(city_input: list) -> forms.Form:
    class CityForm(forms.Form):
        cities = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=[(city, city) for city in city_input],
        )
    return CityForm
