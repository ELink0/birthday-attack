from random import randint
import hashlib

def ajusta_comprimento(texto, comprimento):
    return texto + ' ' * (comprimento - len(texto))

def gerar_hash(texto, max, hash_dict, adj_positivos, adj_pejorativos):
    hash_obj = hashlib.sha256(texto.encode())
    hash_hex = hash_obj.hexdigest()
    hash_int = int(hash_hex, 16)
    hash = hash_int % max

    if hash in hash_dict and hash_dict[hash] != texto:
        print(f"Colisão encontrada! Hash: {hash}")
        print(f"Texto 1: {texto}")
        print(f"Texto 2: {hash_dict[hash]}")
        
        # Tentar substituir adjetivos para manter o mesmo hash
        novo_texto = texto
        for pos, pej in zip(adj_positivos.items(), adj_pejorativos.items()):
            novo_texto = novo_texto.replace(pos[1], pej[1])
        
        novo_hash_obj = hashlib.sha256(novo_texto.encode())
        novo_hash_hex = novo_hash_obj.hexdigest()
        novo_hash_int = int(novo_hash_hex, 16)
        novo_hash = novo_hash_int % max

        if novo_hash == hash:
            print("Substituição bem-sucedida mantendo o mesmo hash com texto pejorativo:")
            print(novo_texto)
        return True
    else:
        hash_dict[hash] = texto
    return False

# Utilizando as funções substitui_tag, sortear_adjetivos, identifica_parenteses como definido anteriormente

def iniciar(num_iteracoes, max=2**16, adj_positivos={}, adj_pejorativos={}):
    texto_base = """Prezado José,

Quero parabenizar você pelo seu (excepcional, notável, impressionante) desempenho durante o último projeto. Sua capacidade de (liderar, coordenar, gerenciar) a equipe e (maximizar, otimizar, aumentar) a eficiência dos processos foi (crucial, essencial, fundamental) para o sucesso que alcançamos.

Como reconhecimento ao seu (esforço, comprometimento, dedicação), estamos considerando (promovê-lo, aumentar seu salário, expandir seu papel) na empresa. Acredito firmemente que sua (perspicácia, capacidade, habilidade) em lidar com desafios complexos pode ser (ainda mais explorada, amplamente utilizada, melhor aproveitada) em novos projetos.

Além disso, gostaria de (convidá-lo, pedir-lhe, sugerir-lhe) para liderar a próxima iniciativa que estamos planejando. Esta será uma oportunidade para (demonstrar, exibir, mostrar) suas (competências, habilidades, capacidades) em um estágio ainda maior.

Por favor, passe no RH para discutirmos (este assunto, estas propostas, estas possibilidades) mais detalhadamente.

Atenciosamente,"""
    hash_dict = {}
    num_colisoes = 0

    for _ in range(num_iteracoes):
        adjetivos, texto_convertido = identifica_parenteses(texto_base)
        adjetivos_sorteados = sortear_adjetivos(adjetivos)
        texto_novo = substitui_tag(texto_convertido, adjetivos_sorteados)
        if gerar_hash(texto_novo, max, hash_dict, adj_positivos, adj_pejorativos):
            num_colisoes += 1
            if num_colisoes > 1:  # Para fins de demonstração, parar após algumas colisões
                break

    print(f"Total de colisões encontradas: {num_colisoes}")

# Dicionários de adjetivos
adj_positivos = {
    "excepcional": ajusta_comprimento("excepcional", 20),
    "notável": ajusta_comprimento("notável", 20),
    "impressionante": ajusta_comprimento("impressionante", 20)
}
adj_pejorativos = {
    "excepcional": ajusta_comprimento("medíocre", 20),
    "notável": ajusta_comprimento("insignificante", 20),
    "impressionante": ajusta_comprimento("patético", 20)
}

adjetivos_positivos = {
    "excepcional": "excepcional    ",  # Adicionando espaços para igualar o comprimento/hash
    "notável": "notável      ",
    "impressionante": "impressionante"
}

adjetivos_pejorativos = {
    "excepcional": "medíocre      ",   # Comprimento ajustado para manter o hash
    "notável": "insignificante",
    "impressionante": "patético       "
}

# Exemplo de uso
iniciar(10000, max=2**16, adj_positivos=adj_positivos, adj_pejorativos=adj_pejorativos)
