from challange import julio_cesar_decoder


def test_decodificao_julio_cesar():
    numero_casas = 3
    cifrado = 'd oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr'

    texto_decodificado = julio_cesar_decoder(numero_casas, cifrado)

    assert texto_decodificado == 'a ligeira raposa marrom saltou sobre o cachorro cansado'
