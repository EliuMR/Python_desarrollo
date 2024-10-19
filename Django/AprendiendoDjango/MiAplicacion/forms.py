#El archivo de forms.py se encarga de validar los datos que se pasan por el formulario
#Para ello se importa el modulo forms de django
from django import forms

#Para validar 
from django.core import validators

#forms.Form es una clase que se encarga de validar los datos y generar un formulario en HTML
class FromArticle(forms.Form):
    title = forms.CharField(label="Titulo",
                            max_length=100,
                            required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder':'Escribe el titulo',
                                        'class':'titulo_formulario', #Clase de css
                                       }
                                ),
                            validators=[validators.MinLengthValidator(4,'El titulo es muy corto'), #Validador de longitud minimas 
                                        validators.RegexValidator('^[A-Za-z0-9]*$', #Validador de expresion regular
                                        message='El titulo solo puede contener letras y numeros',
                                        code='invalid_title') #Codigo de error
                                        ]
                            
                            )
    content = forms.CharField(label="Contenido",
                              widget=forms.Textarea)
    #podemos tambien actualizar el widget
    content.widget.attrs.update({'class':'contenido_formulario',
                                 'placeholder':'Escribe el contenido del articulo'})
                              
    public = forms.TypedChoiceField(
                                label="Publico",
                                choices=[
                                    (1,"Si"),
                                    (0,"No")
                                ]) #Para que sea un campo de tipo entero
