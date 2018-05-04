from behave import given, then


@given('que o usuário acesse a página "{link}"')
def acessa_link(context, link):
    
