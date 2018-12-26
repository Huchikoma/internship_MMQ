from django import forms

class RawDataForm(forms.Form):
	Hatch_Distance = forms.FloatField(label="Hatch Distance (mm)")
	Beam_Current = forms.FloatField(label="Beam Current (mA)")
	Scan_Speed = forms.FloatField(label="Scan Speed (mm/s)")