from django import forms
from cars.models import Brand, Car

        
#forms.ModelForm é uma função do django que deixaos formulários muito mais fáceis, como se vê abaixo. no Model você passa a classe que foi importada do cars.models e no fields oque deseja que seja mostrado no forms, que nesse caso é tudo.

class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    #fazendo a validação dos dados.
    def clean_value(self): #clean_ é um prefixo que o django entende para criar funções de validação. Sempre quefor criar uma função de validação, use clean_  assim o djando entende que é uma funcção de validação.
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser R$20.0000.') # 2 parâmetros devem ser passados, o primeiro é o atributo que deve ser analisado e depoisa mensagem que desejaque apareça.
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Só aceitamos com o ano de fabricação acima de 1975.')
        return factory_year
            
