from main import arquivo_string, arquivo_hash, comparar_hashes_arquivos

def test_senha():
    assert comparar_hashes_arquivos(arquivo_string, arquivo_hash)