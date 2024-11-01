import pyodbc

# informar nas variáveis abaixo os dados para conexão.
server = '127.0.0.1'
database = 'nome_da_base'
user = 'usuario'
password = '1234abcd'
driver = 'SQL Server'

# Autenticação SQL Server
connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}'

# Autenticação SQL Server sem usuário e senha
#connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes'

try:
    conn = pyodbc.connect(connectionString)
    print("Conexão bem-sucedida.")
    conn.close()
    print("Desconectado com sucesso! Apenas para testes.")
except Exception as e:
    print(f"Erro de conexão: {str(e)}")