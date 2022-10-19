import random
import string

# Este script gera senhas de 18 caracteres
word_length = 18
# Gerar uma lista de letras, dígitos e alguma pontuação
components = [string.ascii_letters, string.digits, "!@#$%&"]
# achatar os componentes em uma lista de caracteres
chars = []
for clist in components:
  for item in clist:
    chars.append(item)
def generate_password():
  # Armazenar a senha gerada
  password = []
  # Escolha um item aleatório de 'chars' e adicione-o a 'password'
  for i in range(word_length):
    rchar = random.choice(chars)
    password.append(rchar)
  # Retorna a senha composta como uma string
  return "".join(password)
# Senha gerada na tela
print(generate_password())
