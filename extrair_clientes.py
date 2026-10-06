import requests
from bs4 import BeautifulSoup

# Página de clientes
url = "https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n"

# Busca a página
response = requests.get(url)
response.raise_for_status()

# Analisa o HTML
soup = BeautifulSoup(response.text, "html.parser")

# Lista de clientes
clientes = []

# Percorre as linhas da tabela
for row in soup.select("#clientes tbody tr"):
    cliente = {
        "nome": row.select_one(".nome").get_text(strip=True),
        "email": row.select_one(".email").get_text(strip=True),
        "saldo": row.select_one(".saldo").get_text(strip=True),
        "perfil": row.select_one(".perfil").get_text(strip=True)
    }

    clientes.append(cliente)

# Mostra os clientes encontrados
print("Clientes encontrados:")

for cliente in clientes:
    print(cliente)


# ==========================================
# ENVIO PARA O WEBHOOK DO N8N
# ==========================================

webhook_url = "http://localhost:5678/webhook-test/clientes"

response = requests.post(
    webhook_url,
    json=clientes
)

print("\nStatus do Webhook:", response.status_code)
print("Resposta do n8n:", response.text)