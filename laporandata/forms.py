from django import forms




class Form_LaporanDana(forms.Form):
    Uraian       = forms.CharField(
                                            max_length = 30,
                                            widget = forms.TextInput(
                                                attrs = {
                                                    'class' : 'form-control',
                                                    'placeholder' : "masukan masukan uraian"
                                                }
                                                )
                                            )
    harga        = forms.FloatField()
    bukti_barang = forms.ImageField(
                            label = "masukan bukti barang/kegiatan"
        )
    bukti_transaksi = forms.ImageField(
                            label = "masukan bukti transaksi"
        )



