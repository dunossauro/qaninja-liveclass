from behave import given, then


@given('que o usuário acesse a página "{link}"')
def acessa_link(context, link):
    context.browser.get(link)


@then('a mensagem "{sms}" deverá estar no título')
def checa_titulo(context, sms):
    assert context.browser.title == sms
