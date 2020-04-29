import requests
import json
import hashlib
from decouple import config

def julio_cesar_decoder(number, code_text):
    char_decoded = []
    for letter in code_text:
        char = ord(letter)
        if char == 32:
            ascii_number = 32
        elif char == 46:
            ascii_number = 46
        elif (char - number) < 97:
            ascii_number = (((char - number) + 122) - 97) + 1
        else:
            ascii_number = char - number
        char_decoded.append(chr(ascii_number))
    return "".join(char_decoded)

def request_challange(url):
    data = requests.get(url)
    data_dct = json.loads(data.content)
    with open("answer.json", "w") as f:
        json.dump(data_dct, f)

def read_properties(properties):
    with open('answer.json', 'r') as arq:
        data_readed = json.load(arq)
    return data_readed[f'{properties}']

def generate_cryptographic_summary(decode_text):
    return hashlib.sha1(decode_text.encode()).hexdigest()

def update_json(decode_text):
    cryptographic_summary = generate_cryptographic_summary(decode_text)
    with open('answer.json', 'r+') as f:
        data = json.load(f)
        data['decifrado'] = decode_text
        data['resumo_criptografico'] = cryptographic_summary
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def send_form(url):
    answer = {'answer': open('answer.json', 'rb')}
    submit = requests.post(url, files=answer)
    print(submit.headers)


if __name__ == '__main__':
    URL_REQUEST = f"https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={config('TOKEN')}"
    URL_POST = f"https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={config('TOKEN')}"

    request_challange(URL_REQUEST)
    numero_casas, cifrado = read_properties('numero_casas'), read_properties('cifrado')
    texto_decodificado = julio_cesar_decoder(numero_casas, cifrado)
    update_json(texto_decodificado)
    send_form(URL_POST)