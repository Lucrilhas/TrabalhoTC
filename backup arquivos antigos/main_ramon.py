def leitura_arquivo(nome_arquivo):
	with open(nome_arquivo, 'r') as arquivo:
		automato = [linha.replace('\n', '') for linha in arquivo]
	return automato

def separa_elementos(automato):
	automato = [linha.split(',') for linha in automato]
	chaves = ('alfabeto', 'estados', 'estado_inicial', 'estados_finais')
	valores = automato[0:4].copy()
	dados = dict(zip(chaves, valores))
	regras_transicao = automato[4:]
	return dados, regras_transicao

def validar_automato(alfabeto, estados, estados_finais, regras):
	if len(estados) == 0:
		print("\n # Conjunto de estados vazio!")
		return False

	for ef in estados_finais:
		if ef not in estados:
			print("\n # Estados finais devem estar no conjunto de estados atingiveis!")
			return False

	for item in regras:
		if item[0] not in estados:
			print("\n # Os estados iniciais das regras devem estar no conjunto de estados atingiveis!")
			return False

		if item[1] not in alfabeto:
			print("\n # Os simbolos das regras devem estar no alfabeto!")
			return False

		if item[2] not in estados:
			print("\n # Os estados alvo das regras devem estar no conjunto de estados atingíveis!")
			return False

	return True

def ler_palavra(estado_inicial, estados_finais, regras):
	palavra = '01110'
	estado_atual = estado_inicial[0]

	for i, letra in enumerate(palavra):
		estado_validacao = False

		for item in regras:
			if (item[0] == estado_atual) and (item[1] == letra):
				print(f" - Estado atual: {estado_atual}", end=' ')
				print(f"| Restante palavra: {palavra[i:]}", end=' ')
				print(f"| Para o estado:", item[2])
				estado_atual = item[2]
				estado_validacao = True
				break

		if not estado_validacao:
			return False

	if estado_atual in estados_finais:
		return True
	else:
		return False

def main():
	# Faz a leitura do arquivo
	automato = leitura_arquivo('afd_ramon.txt')

	# Separa os dados do automato das regras de transicao
	dados, regras_transicao = separa_elementos(automato)

	# Mostra os dados
	print(" === Dados gerais do automato ===\n")
	print(f" * Alfabeto: {dados['alfabeto']}")
	print(f" * Estados: {dados['estados']}")
	print(f" * Estado Inicial: {dados['estado_inicial']}")
	print(f" * Estados Finais: {dados['estados_finais']}")

	print("\n === Regras de transicao ===\n")
	for regra in regras_transicao:
		print(' - ', regra)

	# Testa e faz a leitura de uma palavra
	print('\n === Inicio processamento ===\n')
	if validar_automato(dados['alfabeto'], dados['estados'], dados['estados_finais'], regras_transicao):
		validez_palavra = ler_palavra(dados['estado_inicial'], dados['estados_finais'], regras_transicao)

		print("\n # Resultado:", end=' ')
		if validez_palavra == True:
			print("palavra valida!")
		else:
			print("palavra invalida!")

if __name__ == '__main__':
	main()
