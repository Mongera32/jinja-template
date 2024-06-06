from jinja2 import Template
import logging
import os, json, sys, pathlib
import pandas as pd

severity_level = logging.DEBUG
logger = logging.getLogger(__name__)
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(severity_level)

def dir_modulo() -> str:
    """obtém o caminho absoluto do diretório raiz do módulo"""

    abs_path = pathlib.Path(__file__).parent.resolve()

    return abs_path

def buscar_dados():
    """Retorna os argumentos necessários para instanciar a classe TemplateRender"""

    # define nome do template
    template_nome = sys.argv[1]

    if "--json" in sys.argv:
        template_nome, variaveis_valores = _buscar_dados_json(template_nome)

    else:
        template_nome, variaveis_valores = _buscar_dados_csv(template_nome)

    # retorna o nome do template e dados de variaveis
    return template_nome, variaveis_valores

def _buscar_dados_json(template_nome:str):
    """Busca dados contidos em um arquivo json"""

    variaveis_path = f"{dir_modulo()}/variaveis/{template_nome}.json"

    # busca os dados na pasta /variaveis e cria o dict variaveis_valores
    with open(variaveis_path, mode="r") as f:
        variaveis = f.read()
        variaveis_valores = json.loads(variaveis)

    # retorna o nome do template e dados de variaveis
    return template_nome, variaveis_valores

def _buscar_dados_csv(template_nome:str):
    """Busca dados contidos no arquivo `.csv`"""

    df = pd.read_csv(f"{dir_modulo()}/variaveis/var.csv")

    # filtrando linha correspondente ao template desejado
    # e transformando em dict
    filtro = df["template_nome"] == template_nome
    series = df[filtro]
    variaveis_valores = pd.Series.to_dict(series)

    # retorna o nome do template e dados de variaveis
    return template_nome, variaveis_valores


class TemplateRender():
    """
    Wrapper para renderizar um template de arquivo usando a bilbioteca Jinja.

    Argumentos:

    - template_name (str): Nome do template a ser usado
    - kwargs: variáveis a serem usadas na renderização. Atentar para o nome da variável, 
    que deve ser idêntico ao nome usado no template.

    """

    def __init__(self,
                template_nome:str,
                data:dict
    ) -> None:

        self.template_nome = template_nome
        self.data = data


    def __str__(self) -> str:
        return self._renderizar()


    def _renderizar(self) -> str:
        """
        Pega um template da pasta e renderiza
        """

        # Carrega o template
        with open(f"{dir_modulo()}/template/{self.template_nome}") as f:
            template = Template(f.read())

        # Renderiza o template carregado
        texto_arquivo = template.render(self.data)

        return texto_arquivo
    

    def limpar_cache(self):
        """
        Limpa arquivos na pasta 'Renderizado'
        """

        # Obtém diretório atual
        cwd = os.getcwd()

        # Cria lista de arquivos em /renderizado
        lista_dir = os.listdir(f"{dir_modulo()}/renderizado)")

        # Apaga cada arquivo em /renderizado
        for nome_arquivo in lista_dir:
            os.remove(f"{dir_modulo()}/renderizado/{nome_arquivo}")
    
        

    def criar_arquivo(self):
        """
        Renderiza um template e cria um arquivo novo com o texto renderizado
        """

        # Renderiza o template e retorna string com o texto do arquivo
        texto_arquivo = self._renderizar()

        # if len(sys.argv) > 2:

        #     destino = sys.argv[2]

        # else:

        destino = f"{dir_modulo()}/renderizado/{self.template_nome}"


        # Se arquivo renderizado não existe, cria o arquivo
        if not os.path.isfile(destino):

            with open(destino, mode="x") as f:
                f.write(texto_arquivo)

        # Se arquivo renderizado existe, sobrescreve o arquivo
        else:

            with open(destino, mode="w") as f:
                f.write(texto_arquivo)


if __name__ == "__main__":
    print(dir_modulo())