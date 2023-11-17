"""
SEL0456 - Desenvolvimento de Software Livre
Arquivo Leitura User do Trabalho 3-Branch1

Author: Ryan Fellipe Silva Costa - ryanfellipe2001@usp.br
n°USP: 11953369

"""
import hashlib

Senha_Correta = "123456"

def calcular_hash_senha(senha, salt):
    """"calcular a hash correspondente à senha correta"""
    senha_concatenada = senha.encode('utf-8') + salt
    hash_obj = hashlib.sha256(senha_concatenada)
    return hash_obj.hexdigest()


def comparar_hashes_arquivos(arquivo_string, arquivo_hash):
    """"Faz a comparação dos arquivos no diretório"""
    try:
        # Ler a string do arquivo
        with open(arquivo_string, 'r') as arquivo_str:
            string_lida = arquivo_str.read().strip()

        # Ler o hash e o salt do arquivo
        with open(arquivo_hash, 'r') as arquivo_hsh:
            linhas = arquivo_hsh.readlines()
            hash_lido = linhas[0].strip()
            salt_lido = bytes.fromhex(linhas[1].strip())  # Converte a representação hexadecimal para bytes

        # Calcular o hash da string lida com o salt do arquivo
        hash_calculado = calcular_hash_senha(string_lida, salt_lido)

        # Comparar os hashes
        if hash_calculado == hash_lido:
            return True
        else:
            return False

    except FileNotFoundError:
        print("Um dos arquivos não foi encontrado.")
        return False

# Nome dos Arquivos
arquivo_string = 'Senha.txt'
arquivo_hash = 'Senha_Crypt.txt'

def test_senha():
    assert comparar_hashes_arquivos(arquivo_string, arquivo_hash)
