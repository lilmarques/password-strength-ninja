# Credential Breach Auditor (Powered by HIBP)
Ferramenta de Cibersegurança desenvolvida em Python para análise avançada de credenciais. Diferente de validadores comuns, este script não apenas verifica a sintaxe (tamanho/caracteres), mas utiliza **Hashing SHA-1** e a API **"Have I Been Pwned"** para verificar se a senha já foi exposta em vazamentos reais de dados (Data Breaches).
# Credential Breach Auditor (Powered by HIBP)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-SHA1-red?style=for-the-badge)

## 🚀 Funcionalidades
- **Análise de Entropia:** Verifica comprimento, uso de caracteres especiais, números e letras.
- **Detecção de Vazamento (Real-Time):** Consulta bancos de dados de senhas vazadas sem expor a senha original (K-Anonymity model).
- **Feedback Educativo:** Instrui o usuário sobre como melhorar a segurança da credencial.

## 🛠️ Tecnologias
- Python 3
- Requests (API Consumption)
- Hashlib (Criptografia)
- RegEx (Expressões Regulares)

## ⚙️ Como Rodar
```bash
# Clone o repositório
git clone [https://github.com/SEU-USUARIO/password-strength-ninja.git](https://github.com/SEU-USUARIO/password-strength-ninja.git)

# Instale as dependências
pip install requests

# Execute
python app.py
