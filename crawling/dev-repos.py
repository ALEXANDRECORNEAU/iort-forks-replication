import requests
import json
import time
import sqlite3
import csv
import math

def get_repo_data(url, developer):

    # Requisicao
    response = requests.get(url, headers=headers)

    # Verificar se a requisição foi bem sucedida
    if response.status_code == 200:
        # Converter a resposta JSON em um objeto Python
        repo_info = json.loads(response.content)

        # Obter informações sobre o repositório
        repo_name = repo_info['name']
        print("Repo name: ", repo_name)
        repo_description = repo_info['description']
        repo_commits_url = repo_info['commits_url'].split('{')[0]
        repo_watchers = repo_info['watchers_count']
        repo_forks = repo_info['forks']
        repo_is_fork = repo_info['fork']
        repo_created_at = repo_info['created_at']
        repo_updated_at = repo_info['updated_at']

        # Criar uma tabela para armazenar as informações do repositório
        c.execute('''CREATE TABLE IF NOT EXISTS repos
                        (name TEXT, description TEXT, developer TEXT, commits_url TEXT, watchers INTEGER, forks INTEGER, is_fork TEXT, created_at TEXT, updated_at TEXT)''')

        # Inserir as informações do repositório no banco de dados
        c.execute("INSERT INTO repos VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)", (repo_name, repo_description, developer, repo_commits_url, repo_watchers, repo_forks, repo_is_fork, repo_created_at,repo_updated_at))

        # Confirmar a transação e fechar a conexão
        conn.commit()
        
    else:
        # Exibir uma mensagem de erro se a requisição falhar
        print(f'Não foi possível buscar informações do usuário/repositório {developer}')
    # Pausar por 40 segundos antes de fazer a próxima requisição
    time.sleep(2)

def get_repositories(developer, page):
    url = f"https://api.github.com/users/{developer}/repos?page={page}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            repository = repo["name"]
            # print("Getting data: ", repository)
            url = f'https://api.github.com/repos/{developer}/{repository}'
            get_repo_data(url, developer)
    else:
        print(f"Error: {response.status_code}")

with open('config.json') as config_file:
    config = json.load(config_file)
    token = config['token']
    # Adicionar o token de autenticação no cabeçalho da requisição
    headers = {'Authorization': f'Token {token}'}

# Criar uma conexão com o banco de dados SQL
conn = sqlite3.connect('git.db')
c = conn.cursor()

with open('dev_qtde_repos.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
        
    for row in reader:
        developer = row['username']
        print("--- Developer: ", developer)
        qtde_repos = row['public_repos']
        pages = math.ceil(int(qtde_repos) / 30)
        print(developer," - pages: ", pages)
        for i in range(pages):
            get_repositories(developer, str(i))

# Fecha conexao com o banco
conn.close()