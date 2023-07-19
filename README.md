# Replication Package - Extração de Forks de Repositórios de IoRT

Aqui você encontra os detalhes de implementação do nosso trabalho "Mineração de Repositórios de Software para Internet das Coisas e Robótica (IoRT): Análise Inicial dos Forks"
Nossa abordagem consiste em 3 etapas principais, conforme mostrado na figura abaixo. Você pode saber mais detalhes sobre cada etapa em nosso artigo.



Lista de repositórios originais.

## Banco de Dados (Dados Extraídos)

Este estudo foi realizado por membros do Grupo de Pesquisa Intel Agir , com o apoio da Fundação Araucária. Esta é a nossa equipe de pesquisadores:
• Michel Albonico (Professor da Universidade Tecnológica Federal do Paraná)
- Alexandre Corneau (Estagiário da Universidade Tecnológica Federal do Paraná)

## Construindo o conjunto de dados
Grande parte do procedimento foi automatizada utilizando scripts de Python e a API REST do GitHub. Os repositórios do GitHub foram acessados através da API REST, como você verá mais tarde. Além disso, disponibilizamos os códigos de Python que identificam os repositórios que foram selecionados do GitHub. Apesar de alguns imprevistos durante a busca por repositórios, mais de 42 mil repositórios foram analisados.
Aqui estão alguns detalhes adicionais sobre o processo de automatização:
• Os scripts de Python foram usados para acessar os repositórios do GitHub e extrair informações sobre eles, como o nome do repositório, a descrição, a quantidade de estrelas e a quantidade de forks.
• A API REST do GitHub foi usada para fazer solicitações aos repositórios do GitHub e obter as informações necessárias.
• Os códigos de Python foram disponibilizados para que outras pessoas possam usá-los para replicar o processo de automatização.

Nossos scripts são organizados da seguinte forma:
./scripts/
    |--- crawling/     		    Pasta aonde fica o código para realizar busca e implementação do banco.
         |--- Buscador.py   código que realiza a busca dos usuários.
         |--- requirements.txt  Python dependência. Tipo "pip install -r requirements.txt".
         |--- keywords          Lista de usuários para gerar a busca.
         |--- config.json	    Script para informar as credencias o token do GitHub.

1. Para iniciar o processo de mineração, informamos os usuários e extraímos todos os forks que eles realizaram.
Python3 Buscador.py

2. Para facilitar as solicitações ao GitHub, usamos um arquivo JSON para passar o token de acesso para as solicitações. Isso nos permite fazer mais de 5.000 solicitações por hora, em vez de sermos bloqueados pela plataforma após fazermos muitas solicitações.

