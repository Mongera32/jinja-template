from template_render import buscar_dados, TemplateRender

def main():

    template_nome, variaveis_valores = buscar_dados()

    template_render = TemplateRender(
        template_nome,
        variaveis_valores
    )

    template_render.criar_arquivo()

if __name__ == "__main__":
    main()