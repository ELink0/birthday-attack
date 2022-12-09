#-*- coding: UTF-8 -*-
from random import randint
from random import random
import csv

#### INICIO DAS FUNÇÕES ####
def gerarHash(texto, max):
	valor = 0
	for i in texto:
		valor += ord(i)

	hash = valor % max
	return hash

def substituiTag(texto, adjetivos):
	textoNovo = ""
	z = 0
	estado = "fora"

	for i in texto:
		if estado == "fora":
			if i != "<":
				textoNovo += i
			else:
				textoNovo += str(adjetivos[z])
				estado = "dentro"

		elif estado == "dentro":
			if i == ">":
				estado = "fora"
				z += 1
	return textoNovo

def permuta(adjetivos, adjpermutados, z):
	k = 0
	if len(adjetivos) == z:
		print (k, ' ', adjpermutados)
		k += 1

	else:
		for i in range(len(adjetivos[z])):
			nova_lista = list(adjpermutados)

			nova_lista.append(adjetivos[z][i])
			permuta(adjetivos, nova_lista, z+1)


def sortearAdjetivos(adjetivos):
	novaLista = []

	for x in range(len(adjetivos)):
		z = randint(0, len(adjetivos[x])-1)
		novaLista.append(adjetivos[x][z])
	return novaLista

def identificaParenteses(texto):
	textoConvertido = ""
	adjetivos = []
	adjetivo = ""
	estado = "fora"
	contador = 0
	linha = []

	for t in texto:
		if estado == "fora":
			if t != "(":
				textoConvertido += t

			else:
				textoConvertido += "<t"+str(contador)+">"
				linha = []
				estado = "dentro"
				adjetivo = ""

		elif estado == "dentro":
				if t == ")":
					estado = "fora"
					contador += 1
					linha.append(adjetivo)
					adjetivos.append(linha)

				elif t == ",":
					linha.append(adjetivo)
					adjetivo = ""

				else:
					adjetivo += t

	return adjetivos, textoConvertido

def salvarArquivo(hash1, hash2, max):
	with open("resultados.txt",'a') as f:
		f.write('Máx ')
		f.write(str(max))
		f.write(': \t')
		f.write(str(hash1))
		f.write('\t')
		f.write(str(hash2))
		f.write('\n')

def iniciar():
	texto_1 = """Olá José,
Venha por meio deste e-mail, lhe dizer que você é um (exímio funcionário, bom funcionário, excelente, funcionário) e ofereceu a nossa empresa (muitos ganhos, muito lucro). Você é uma pessoa que (merece o melhor, se dedica muito, se esforça muito) e por isso gostaria de lhe oferecer (um aumento, uma promoção, férias, uma bolsa de estudos). 
Por gentileza, fale com o responsável pelo RH para definirmos melhor o que fazer.

Por fim, peço que continue sendo este profissional (excelente, bom, exemplar) que você é. Tenho certeza que muitos (se inspiram em você, te admiram, te adoram).

Obrigado!"""
	texto_2 = """Olá José,
Venha por meio deste e-mail, lhe dizer que você é um (péssimo funcionário, mal funcionário, funcionário horrível) e ofereceu a nossa empresa (apenas derrota, muito desserviço). Você é uma pessoa que (me dá nojo, não se dedica, não quer saber de nada) e por isso gostaria de lhe oferecer (uma demissão, a porta da rua, que se retire da empresa). 
Por gentileza, fale com o responsável pelo RH para definirmos melhor o que fazer.

Por fim, peço que continue sendo este profissional (péssimo, ruim, fraco) que você é. Tenho certeza que muitos (te odeiam, não gostam de você).

Obrigado!"""

	controle_loop = 0
	max = 128
	while controle_loop == 0:
		adjetivos_1, textoConvertido_1 = identificaParenteses(texto_1)
		adjetivos_2, textoConvertido_2 = identificaParenteses(texto_2)

		adjetivos_sorteados_1 = sortearAdjetivos(adjetivos_1)
		adjetivos_sorteados_2 = sortearAdjetivos(adjetivos_2)

		# Chama a função de substituir Tags
		textoNovo1 = substituiTag(textoConvertido_1, adjetivos_sorteados_1)
		textoNovo2 = substituiTag(textoConvertido_2, adjetivos_sorteados_2)

		# Chama função de gerar Hash
		hash1 = gerarHash(textoNovo1, max)
		hash2 = gerarHash(textoNovo2, max)

		if hash1 == hash2:
			print("Colisão de hashs! \nHash1: {} \nHash2: {} \n Texto 1: {} \n Texto 2: {}".format(hash1, hash2, textoNovo1, textoNovo2))
			salvarArquivo(hash1, hash2, max)

#### FIM DAS FUNÇÕES ####

iniciar()