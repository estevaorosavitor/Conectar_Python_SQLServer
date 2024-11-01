## Conectar Python com Microsoft SQL Server

Esse projeto é um base para conectar o python com o banco de dados SQL Server.

Com ele é possível fazer a conexão utilizando dois tipos de autenticação:
* SQL Server Autentication: Que são os usuários criados no próprio banco de dados;
* Windows Autenticatinon: Que são os usuários do Windows.

São apenas 4 variaveis que precisa ser informada:
* `database` = nome da base de dados;
* `server` = IP do servidor do banco de dados;
* `user` = usuário do banco de dados;
* `pasword` = senha do usuário do banco.

Para a aplicação funcionar é necessário instalar a biblioteca pyodbc presente no pacote pip.
`pip install pyodbc`
