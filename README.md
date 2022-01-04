# FidelizaMais

## Descrição
O desafio proposto é a criação de uma API para o programa de fidelidade da Juntos Somos Mais, na qual um membro pode indicar outras pessoas para participar do programa e se aceitarem, o indicador recebe pontos para trocar por prêmios.

## Intalação e Dependências

### Requisitos
1. Docker
2. Docker Compose

## Configurar a aplicação para rodar localmente:
Clone o repositório para criar uma cópia local no seu computador

	git clone git@github.com:mairaafreitas/fideliza-mais.git

## Inicialização
1. Abra o diretório clonado no terminal

1. O docker precisa preparar as imagens declaradas no repositório, criando os containers e inicializando-os,
para isso, utilize o comando:

	``docker-compose up``

3. Para que a estrutura do banco de dados seja criada dentro do container, execute o comando:

    ``docker-compose run web python manage.py migrate``

4. Crie o seu usuário para acessar o painel administrativo

	``docker-compose run web python manage.py createsuperuser``

5. Para verificar se está funcionando, acesse o painel administrativo

	``localhost:8000/admin ``


## Documentação da API
Para verificar todos os endpoints da API e seus possíveis erros, acesse:

[*Documentação*](https://documenter.getpostman.com/view/18406496/UVRHi3v6)

Para verificar como as histórias para elaboração da api foram criadas, acesse:

[*Kanban*](https://mairafreitas.notion.site/Desafio-Fideliza-Mais-8c5083b831a947a188ca95ad9c555ea9)
## Autor
* **Maíra Freitas** - [*Junior Backend Developer*](https://github.com/mairaafreitas)
