from django import forms




class Form_Rab(forms.Form):
    nama_kegiatan       = forms.CharField(
                                            label = "Nama Kegiatan",
                                            max_length = 30,
                                            widget = forms.TextInput(
                                                attrs = {
                                                    'class' : 'form-control',
                                                    'placeholder' : "masukan kegiatan"
                                                }
                                                )
                                            )


    deskripsi           = forms.CharField(
                                            required = False,
                                            widget = forms.Textarea(
                                                attrs = {
                                                    'class' : 'form-control',
                                                    'placeholder': 'masukan deskripsi kegiatan'
                                                }

                                                ))
    tujuan              = forms.CharField(required = False, widget = forms.Textarea)
    jumlah_biaya        = forms.FloatField()
    upload_proposal     = forms.FileField(label = "Upload Proposal")



