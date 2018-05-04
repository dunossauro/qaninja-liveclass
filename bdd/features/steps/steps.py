from behave import given, then

def conta_bananas(lista_de_bananas):
    return sum(lista_de_bananas)


@given('que alguém tenha {num:d} bananas')
def alguem_tem_bananas(context, num):
    context.alguem = num


@given('fulano tenha {num:d} bananas')
def fulano_tem_bananas(context, num):
    context.fulano = num


@given('luizinho tenha {num:d} bananas')
def luizinho_bananas(context, num):
    context.luizinho = num


@then('temos {num:d} bananas')
def soma_das_bananas(context, num):
    assert conta_bananas(
     [context.alguem, context.fulano, context.luizinho]
    ) == num
