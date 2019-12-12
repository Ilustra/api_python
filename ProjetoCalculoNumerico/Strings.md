-------Podemos checar se a string é alfa-numérica, ou seja, contém apenas letras e números, sem caracteres especiais.
>>> 'aa44'.isalnum()
True
>>> 'a$44'.isalnum()
False

-------É possível checar se uma string contém apenas letras.
>>> 'letters'.isalpha()
True
>>> 'letters4'.isalpha()
False

-------Agora checando se ela contém apenas números.
>>> '306090'.isdigit()
True
>>> '30-60-90 Triangle'.isdigit()
False