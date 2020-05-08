
from django import forms

class Form_Control(forms.Form):

    # select
    PILIHAN = (
            ('Banten','Banten'),
            ('Jawa Barat','Jawa Barat'),
            ('Jakarta','Jakarta'),
        )
    provinsi        = forms.ChoiceField(choices=PILIHAN)



    # select
    PILIHAN_KABUPATEN = (
            ('pandeglang','pandeglang'),
            ('bandung','bandung'),
            ('bandung','bandung'),
        )
    kabupaten        = forms.ChoiceField(choices=PILIHAN_KABUPATEN)


