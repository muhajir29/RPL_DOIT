from django import forms

from .models import Pusat, Rab , Sub, Transfer, ValTransfer, ValRab




class FormTransfer(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = [
            'pusat','sub', 'uraian', 'jumlah'
        ]

        label = {
            'pusat' : "pengirim",
            'sub' : "penerima"
        }



class FormRab(forms.ModelForm):
    class Meta :
        model = Rab
        fields = [
            'pusat', 'sub', 'nama_kegiatan', 'deskripsi','tujuan', 'jumlah', 'proposal'
        ]


class FormValTransfer(forms.ModelForm):
    class  Meta:
        model = ValTransfer
        fields = ['transfer', 'uraian', 'harga', 'bukti_item', 'bukti_transfer']













































