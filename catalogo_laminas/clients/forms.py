from django import forms


class SubscripcionForm(forms.Form):
    email = forms.EmailField(label='Introduce tu correo', max_length=250)
    terms = forms.BooleanField(label='Acepto términos')


class RegistroProveedores(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    apellido_p = forms.CharField(label='Nombre', max_length=50)
    apellido_m = forms.CharField(label='Nombre', max_length=50)
    calle = forms.CharField(label='Nombre', max_length=50)
    num = forms.CharField(label='Nombre', max_length=50)
    colonia = forms.CharField(label='Nombre', max_length=50)
    estado = forms.CharField(label='Nombre', max_length=50)
    pais = forms.CharField(label='Nombre', max_length=50)


class CompanyForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    contacto = forms.CharField(label='Contacto', max_length=50)
    soporte = forms.CharField(label='Soporte', max_length=50)
    ventas = forms.CharField(label='Ventas', max_length=50)
