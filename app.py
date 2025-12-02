Arquivo app.py:

import re
import hashlib
import requests
import getpass

def check_pwned_api(password):
    """Verifica se a senha vazou usando a API Have I Been Pwned"""
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    url = 'https://api.pwnedpasswords.com/range/' + first5_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Erro na API: {res.status_code}')
    
    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return int(count)
    return 0

def calcular_forca(senha):
    score = 0
    feedback = []
    
    if len(senha) >= 12: score += 2
    elif len(senha) >= 8: score += 1
    else: feedback.append("Senha muito curta (min 8 chars).")
    
    if re.search(r"[A-Z]", senha): score += 1
    else: feedback.append("Adicione letras maiúsculas.")
    
    if re.search(r"[0-9]", senha): score += 1
    else: feedback.append("Adicione números.")
    
    if re.search(r"[@$!%*?&]", senha): score += 1
    else: feedback.append("Adicione caracteres especiais (@$!%*?&).")
    
    return score, feedback

def main():
    print("--- 🕵️‍♂️ Password Ninja - Analisador de Segurança ---")
    senha = getpass.getpass("Digite a senha para testar (input oculto): ")
    
    print("\nAnalisando...")
    score, feedback = calcular_forca(senha)
    
    print(f"Pontuação de Complexidade: {score}/5")
    if feedback:
        print("Dicas para melhorar:", ", ".join(feedback))
        
    # Verifica vazamento
    print("Verificando vazamentos em bancos de dados reais...")
    vazamentos = check_pwned_api(senha)
    if vazamentos:
        print(f"❌ PERIGO! Essa senha já apareceu em {vazamentos} vazamentos de dados!")
    else:
        print("✅ Boa notícia! Essa senha não consta nos bancos de dados de vazamentos públicos.")

if __name__ == "__main__":
    main()

Instalar: pip install requests