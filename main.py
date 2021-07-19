import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8c460650d39aafefe0b5a0bd195bab91"
# Your Auth Token from twilio.com/console
auth_token = "ec5230900fbdb5a7ae4f469ef5e33f41"
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro' , 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho']
# Para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+123456789", # Número de telefone do usuário
            from_="+987654321", # Número gerado pelo twilio
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)



# Verificar se algunm valor na coluna Vendas é maior que 55.000

# Se for maior do que 55.000 --> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior que 55.00 não quero fazer nada