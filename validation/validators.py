from django.core.exceptions import ValidationError

def valida_cpf(value):
    if(len(str(value)) != 11):
        raise ValidationError ('ERRO! CPF INCORRETO!')
    else:
        return value
    
def valida_senha(value):
    if(len(str(value)) != 6):
        raise ValidationError ('ERRO! SENHA INCOMPLETA!')
    else:
        return value
