# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
  if consumo <= 10:
    plano = 'Plano Essencial Fibra - 50Mbps'
  elif 10 < consumo <= 20:
    plano = 'Plano Prata Fibra - 100Mbps'
  elif consumo > 20:
    plano = 'Plano Premium Fibra - 300Mbps'
# TODO: Retorne o plano de internet adequado:
  return plano
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
