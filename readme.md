# Sobre

Este módulo é um Wrapper para a biblioteca Jinja

# Uso

## Criando template

Para criar um template, insira um arquivo editável qualquer na pasta *template* e defina os placeholders com chaves duplas (*{{nome_da_variável}}*)

## Variáveis

Para definir os valores das variáveis a serem substituídas em *{{nome_da_variável}}*, insira um arquivo *json* na pasta *variaveis*. Observe que
o arquivo deve ter um nome idêntico ao do template ao qual ele corresponde, seguido da extensão *.json*.

Exemplo: Se há um arquivo na pasta *template* intitulado *docker-compose.yaml*, então o json que guarda as variáveis desse template 
deve ser chamado de *docker-compose.yaml.json*.

## Chamada

Para criar o arquivo, use a CLI do python da seguinte forma:

python3 <caminho/para/o/módulo>/jinja_template/main.py> <nome-do-arquivo-template> [ <caminho/destino> ] [ --json | --csv ]

O arquivo renderizado será salvo em <caminho-destino> caso esse seja explicitado. Se Ele for omitido, então o arquivo será salvo na pasta *renderizado*.
