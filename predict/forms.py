from django import forms

class HouseForm(forms.Form):
    bedrooms = forms.IntegerField(label="Number of Bedrooms")
    bathrooms = forms.FloatField(label="Number of Bathrooms")
    living_area = forms.IntegerField(label="Living Area (sqft)")
    floors = forms.IntegerField(label="Number of Floors")
    waterfront = forms.IntegerField(label="Waterfront Present (0 or 1)")
    grade = forms.IntegerField(label="Grade of the House")
    area = forms.IntegerField(label="Area (excluding basement)")
    basement_area = forms.IntegerField(label="Area of the Basement")
    views = forms.IntegerField(label="Number of Views")
    condition = forms.IntegerField(label="Condition of the House")
    year_built = forms.IntegerField(label="Year Built")
    schools = forms.IntegerField(label="Schools Nearby")
    airport_distance = forms.FloatField(label="Distance from Airport (km)")
    living_area_renov = forms.IntegerField(label="Living Area (Renovated)")
