from django import forms




class Form_Transfer(forms.Form):




    uraian       = forms.CharField(
                                           max_length = 30,
                                            widget = forms.TextInput(
                                                attrs = {
                                                    'class' : 'form-control',
                                                    'placeholder' : "Masukan Uraian"
                                                }
                                                )
                                            )


    jumlah_biaya        = forms.FloatField()
