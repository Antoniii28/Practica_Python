# Act. 2.3: Práctica Python
# Brayan Zepeda Cuahutencos

import re

def normalizar(texto):
    # Paso 1: minúsculas y sin signos; conserva acentos.
    return re.sub(r'[¡!¿?.,;:«»]', '', texto.lower())

def tokenizar(texto_normalizado):
    # Paso 2: separar el texto en palabras.
    return texto_normalizado.split()

def construir_vocabulario(tokens_por_doc):
    # Paso 3: juntar las palabras, quitar repetidas y ordenar.
    palabras = []
    for tokens in tokens_por_doc:
        palabras.extend(tokens)
    return sorted(set(palabras))

def quitar_stopwords(vocabulario, stopwords):
    # Paso 4: conservar las palabras que no son stopwords.
    return [palabra for palabra in vocabulario if palabra not in stopwords]

CORPUS = {
    'A': ['¡El altar es hermoso y la música crea un ambiente muy emotivo!','La tradición es colorida y la familia comparte la comida con los visitantes.','Hermoso desfile pero el ambiente es muy ruidoso en la ciudad.'],
    'B': ['El turismo es excesivo y la celebración se vuelve un negocio caro.','La película Coco popularizó la tradición y el turismo crece muy rápido.','El respeto por la tradición es esencial y el turista necesita aprender de la familia.'],
    'C': ['El Día de Muertos es diferente al Halloween porque honra a la familia y no asusta.','En mi país Halloween es comercial pero aquí la muerte es parte de la vida.','Los disfraces de calavera son divertidos y el significado es profundo.'],
    'D': ['El pan de muerto es delicioso y el chocolate caliente es perfecto para la noche.','La UNESCO protege esta tradición y el patrimonio cultural es un orgullo para México.','Los cementerios iluminados con velas y flores son un espectáculo inolvidable.'],
}
STOPWORDS = set(['a','al','aquí','con','de','del','el','en','es','esta','la','las','los','mi','muy','no','para','pero','por','porque','se','son','un','una','y'])

TITULOS = {'A':'Primera vez: emoción y asombro','B':'Turismo y comercialización','C':'Día de Muertos frente a Halloween','D':'Gastronomía, patrimonio y cementerios'}
ESPERADOS = {'A':[36,25,10,15],'B':[39,27,9,18],'C':[42,32,15,17],'D':[40,31,11,20]}

def procesar_corpus(comentarios):
    tokens_por_doc = []
    for comentario in comentarios:
        limpio = normalizar(comentario)
        tokens_por_doc.append(tokenizar(limpio))
    vocabulario = construir_vocabulario(tokens_por_doc)
    filtrado = quitar_stopwords(vocabulario, STOPWORDS)
    n = sum(len(tokens) for tokens in tokens_por_doc)
    s = len(vocabulario) - len(filtrado)
    return {'N': n, 'V': vocabulario, 'S': s, 'Vf': filtrado, 'porcentaje': s / len(vocabulario) * 100}

def ficha_metricas(corpus, resultado):
    n, v, s, vf = ESPERADOS[corpus]
    valores = [resultado['N'], len(resultado['V']), resultado['S'], len(resultado['Vf']), resultado['porcentaje']]
    esperados = [n, v, s, vf, s / v * 100]
    nombres = ['1. Tokens totales (N)', '2. Vocabulario |V|', '3. Stopwords |S|', '4. Vocabulario filtrado |Vfiltrado|', '5. Stopwords respecto de V (%)']
    print(f'FICHA DE MÉTRICAS · Corpus {corpus} · {TITULOS[corpus]}')
    print('Métrica                              Valor     Estado')
    correctas = 0
    for i, (nombre, valor, esperado) in enumerate(zip(nombres, valores, esperados)):
        bien = abs(valor - esperado) < 0.01
        correctas += bien
        valor_texto = f'{valor:.2f}' if i == 4 else str(valor)
        print(f'{nombre:<37}{valor_texto:<10}{"✓ correcto" if bien else "✗ revisar"}')
    if correctas == 5:
        print('RESULTADO: ficha completa ✓ ¡Corpus validado!')
    else:
        print(f'RESULTADO: {correctas} de 5 métricas correctas. Corrige y vuelve a ejecutar.')

for corpus in CORPUS:
    ficha_metricas(corpus, procesar_corpus(CORPUS[corpus]))
    print()
