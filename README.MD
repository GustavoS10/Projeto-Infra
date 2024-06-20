### Documentação do projeot ###
O presente projeto é composto pelos seguintes itens:
1) Front-end: Feito com HTML, CSS e JavaScript;
2) API: Feita em Python contendo os métodos de get_user(), add_user() e create_table();
3) Banco de Dados: PostgreSql feito para receber, nome, email e função;
4) Computador auxiliar para automação com Ansible

### Implementações ###
Os contêineres feitos em Docker são iniciados pelo arquivo docker-compose.yml onde há a maioria das configurações dos contêineres, todos dependendo do Banco de Dados subir por primeiro, logo após os demais são executados, a lógica padrão é: Front-end fazer requisições para a API e a API consultar no banco, todas as redes separadas;

### Uso do Ansible ###
O uso do Ansible nesse projeto, ocorre em duas circunstancias, uma ainda não implementada 100%, a primeira ocorre no playbook "backup.yml" onde o intuito é criar um backup do banco de dados em caso de ataques cibernéticos. A segunda abordagem trata de uma checagem de status e saúde dos contêineres, porém ainda incompleto.

### Docker ###
Para o Docker, foi criada há duas subredes: rede_front (10.0.1.0/24) e rede_banco (10.0.2.0/24).
Cada contêinere sobe em suas respectivas portas: Frontend (80:80), Automacao (5001:5001), Backend (5000:5000) e Banco de Dados (22:22, 5432:5432) Sendo o banco de dados o único que está liberado o acesso SSH para o computador automacao para fazer o backup.
