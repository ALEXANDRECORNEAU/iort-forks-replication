import requests
import json
import time
import sqlite3

# Ler o arquivo de configuração com o token de autenticação
with open('config.json') as config_file:
    config = json.load(config_file)
    token = config['token']

# Ler o arquivo de texto com os nomes de usuário e repositórios
with open('usuarios.txt') as f:
    for line in f:
        # Separar o nome de usuário e nome do repositório
        username, repository = line.strip().split()

        # Definir o URL da API do Github
        url = f'https://api.github.com/repos/{username}/{repository}'

        # Adicionar o token de autenticação no cabeçalho da requisição
        headers = {'Authorization': f'Token {token}'}

        # Fazer a requisição
        response = requests.get(url, headers=headers)

        # Verificar se a requisição foi bem sucedida
        if response.status_code == 200:
            # Converter a resposta JSON em um objeto Python
            repo_info = json.loads(response.content)

            # Obter informações sobre o repositório
            repo_name = repo_info['name']
            repo_description = repo_info['description']
            repo_commits_url = repo_info['commits_url'].split('{')[0]
            repo_watchers = repo_info['watchers_count']
            repo_forks = repo_info['forks']
            repo_is_fork = repo_info['fork']
            repo_created_at = repo_info['created_at']
            repo_updated_at = repo_info['updated_at']
            
            # Criar uma conexão com o banco de dados SQL
            conn = sqlite3.connect('git.db')
            c = conn.cursor()

            # Criar uma tabela para armazenar as informações do repositório
            c.execute('''CREATE TABLE IF NOT EXISTS repos
                         (name TEXT, description TEXT, commits_url TEXT, watchers INTEGER, forks INTEGER, is_fork TEXT, created_at TEXT, updated_at TEXT)''')

            # Inserir as informações do repositório no banco de dados
            c.execute("INSERT INTO repos VALUES (?, ?, ?, ?, ?, ?, ?,?)", (repo_name, repo_description, repo_commits_url, repo_watchers, repo_forks, repo_is_fork, repo_created_at,repo_updated_at))

            # Confirmar a transação e fechar a conexão
            conn.commit()
            conn.close()

        else:
            # Exibir uma mensagem de erro se a requisição falhar
            print(f'Não foi possível buscar informações do usuário/repositório {username}/{repository}')
 # Pausar por 40 segundos antes de fazer a próxima requisição
        time.sleep(2)
