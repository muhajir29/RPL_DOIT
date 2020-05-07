from django import forms




class Form_Transfer_Provinsi(forms.Form):

    # select
    PILIHAN = (
            ('Banten','Banten'),
            ('Jawa Barat','Jawa Barat'),
            ('Jakarta','Jakarta'),
        )
    provinsi        = forms.ChoiceField(choices=PILIHAN)




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
