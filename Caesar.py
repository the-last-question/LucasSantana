def caesar(Texto, shift):
	saida = []
	criptografia = []
	
	caixaalta = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	caixabaixa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in Texto:
		if eachLetter in caixaalta:
			index = caixaalta.index(eachLetter)
			crypting = (index + shift) % 26
			criptografia.append(crypting)
			newLetter = caixaalta[crypting]
			saida.append(newLetter)
		elif eachLetter in caixabaixa:
			index = caixabaixa.index(eachLetter)
			crypting = (index + shift) % 26
			criptografia.append(crypting)
			newLetter = caixabaixa[crypting]
			saida.append(newLetter)
	return saida

code = caesar('abc', 2)
print()
print(code)
print()
