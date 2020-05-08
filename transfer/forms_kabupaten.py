from django import forms




class Form_Transfer_Kabupaten(forms.Form):

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




    nama_kegiatan       = forms.CharField(
                                            label = "Uraian",
                                            max_length = 30,
                                            widget = forms.TextInput(
                                                attrs = {
                                                    'class' : 'form-control',
                                                    'placeholder' : "masukan kegiatan"
                                                }
                                                )
                                            )
    jumlah_transfer        = forms.FloatField(
                                            label = "Jumlah Transfer"

                                            )
