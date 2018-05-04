# language: pt
Funcionlidade: Pagina do python deve conter Python no títtulo da página

Cenário: Ná pagina inicial python deverá estar no título
  Dado que o usuário acesse a página "https://www.python.org/"
  Então a mensagem "Welcome to Python.org" deverá estar no título
