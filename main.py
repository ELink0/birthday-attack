from random import randint

def gerar_hash(texto, max, hash_dict):
    valor = 0
    for i in texto:
        valor += ord(i)
    hash = valor % max

    if hash in hash_dict:
        # Ocorreu uma colisão
        print("Colisão de hashs!")
        print("Hash1:", hash)
        print("Texto 1:", texto)
        print("Hash2:", hash_dict[hash])
        print("Texto 2:", hash_dict[hash])
    else:
        hash_dict[hash] = texto

def substitui_tag(texto, adjetivos):
    texto_novo = ""
    z = 0
    estado = "fora"

    for i in texto:
        if estado == "fora":
            if i != "<":
                texto_novo += i
            else:
                texto_novo += str(adjetivos[z])
                estado = "dentro"

        elif estado == "dentro":
            if i == ">":
                estado = "fora"
                z += 1
    return texto_novo

def permuta(adjetivos, adjpermutados, z):
    k = 0
    if len(adjetivos) == z:
        print(k, ' ', adjpermutados)
        k += 1
    else:
        for i in range(len(adjetivos[z])):
            nova_lista = list(adjpermutados)
            nova_lista.append(adjetivos[z][i])
            permuta(adjetivos, nova_lista, z+1)

def sortear_adjetivos(adjetivos):
    nova_lista = []
    for x in range(len(adjetivos)):
        z = randint(0, len(adjetivos[x])-1)
        nova_lista.append(adjetivos[x][z])
    return nova_lista

def identifica_parenteses(texto):
    texto_convertido = ""
    adjetivos = []
    adjetivo = ""
    estado = "fora"
    contador = 0
    linha = []

    for t in texto:
        if estado == "fora":
            if t != "(":
                texto_convertido += t
            else:
                texto_convertido += "<t"+str(contador)+">"
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

    return adjetivos, texto_convertido

def salvar_arquivo(hash1, hash2, max):
    with open("resultados.txt",'a') as f:
        f.write('Máx ')
        f.write(str(max))
        f.write(': \t')
        f.write(str(hash1))
        f.write('\t')
        f.write(str(hash2))
        f.write('\n')

def iniciar(num_iteracoes):
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
    hash_dict = {}
    while controle_loop < num_iteracoes:
        adjetivos_1, texto_convertido_1 = identifica_parenteses(texto_1)
        adjetivos_2, texto_convertido_2 = identifica_parenteses(texto_2)

        adjetivos_sorteados_1 = sortear_adjetivos(adjetivos_1)
        adjetivos_sorteados_2 = sortear_adjetivos(adjetivos_2)

        # Chama a função de substituir Tags
        texto_novo1 = substitui_tag(texto_convertido_1, adjetivos_sorteados_1)
        texto_novo2 = substitui_tag(texto_convertido_2, adjetivos_sorteados_2)

        # Chama função de gerar Hash
        gerar_hash(texto_novo1, max, hash_dict)
        gerar_hash(texto_novo2, max, hash_dict)

        controle_loop += 1

    # Salva o dicionário de hashs em um arquivo
    with open("colisoes.txt", "w") as f:
        for hash, texto in hash_dict.items():
            f.write(f"Hash: {hash}\n")
            f.write(f"Texto: {texto}\n\n")

num_iteracoes = 1000
iniciar(num_iteracoes)
