# Actividad 2.3 - Práctica Python
# Minería de Texto - Día de Muertos
# Jose Antonio Flores Cuamatzi

import re


def normalizar(texto):
    # Minúsculas, sin puntuación y conservando acentos.
    return re.sub(r'[¡!¿?.,]', '', texto.lower())


def tokenizar(texto):
    # Separa las palabras por espacios.
    return texto.split()


def construir_vocabulario(tokens):
    # Quita repetidos y ordena las palabras.
    return sorted(set(tokens))


def quitar_stopwords(vocabulario, stopwords):
    # Elimina las palabras vacías.
    return [palabra for palabra in vocabulario if palabra not in stopwords]

CORPUS = {
    'A': ['¡El altar es hermoso y la música crea un ambiente muy emotivo!','La tradición es colorida y la familia comparte la comida con los visitantes.','Hermoso desfile pero el ambiente es muy ruidoso en la ciudad.'],
    'B': ['El turismo es excesivo y la celebración se vuelve un negocio caro.','La película Coco popularizó la tradición y el turismo crece muy rápido.','El respeto por la tradición es esencial y el turista necesita aprender de la familia.'],
    'C': ['El Día de Muertos es diferente al Halloween porque honra a la familia y no asusta.','En mi país Halloween es comercial pero aquí la muerte es parte de la vida.','Los disfraces de calavera son divertidos y el significado es profundo.'],
    'D': ['El pan de muerto es delicioso y el chocolate caliente es perfecto para la noche.','La UNESCO protege esta tradición y el patrimonio cultural es un orgullo para México.','Los cementerios iluminados con velas y flores son un espectáculo inolvidable.'],
}
STOPWORDS = set(['a','al','aquí','con','de','del','el','en','es','esta','la','las','los','mi','muy','no','para','pero','por','porque','se','son','un','una','y'])

ESPERADOS = {'A': (36, 25, 10, 15), 'B': (39, 27, 9, 18), 'C': (42, 32, 15, 17), 'D': (40, 31, 11, 20)}

for nombre, comentarios in CORPUS.items():
    tokens = []
    for comentario in comentarios:
        tokens.extend(tokenizar(normalizar(comentario)))
    vocabulario = construir_vocabulario(tokens)
    filtrado = quitar_stopwords(vocabulario, STOPWORDS)
    cantidad_stopwords = len(vocabulario) - len(filtrado)
    resultado = (len(tokens), len(vocabulario), cantidad_stopwords, len(filtrado))
    assert resultado == ESPERADOS[nombre], f'Error en corpus {nombre}: {resultado}'
    print(f'CORPUS {nombre} — VALIDADO')
    print(f'Tokens totales: {resultado[0]}')
    print(f'Vocabulario: {resultado[1]}')
    print(f'Stopwords identificadas: {resultado[2]}')
    print(f'Vocabulario filtrado: {resultado[3]}')
    print(f'Porcentaje de stopwords: {cantidad_stopwords / len(vocabulario) * 100:.2f}%')
    print('Palabras útiles:', ', '.join(filtrado))
    print()
