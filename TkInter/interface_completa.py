import customtkinter as ctk


# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# ==========================================================
# APLICAÇÃO
# ==========================================================

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ==================================================
        # CONFIGURAÇÕES DA JANELA
        # ==================================================

        self.title("Automações Meli")
        self.state("zoomed")
        self.minsize(800, 500)

        # Configuração do Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==================================================
        # BARRA LATERAL
        # ==================================================

        self.barra_lateral = ctk.CTkFrame(
            self,
            width=200,
            corner_radius=0
        )

        self.barra_lateral.grid(
            row=0,
            column=0,
            sticky="nswe"
        )

        self.barra_lateral.grid_propagate(False)

        self.criar_barra_lateral()

        # ==================================================
        # ÁREA PRINCIPAL
        # ==================================================

        self.janela_principal = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.janela_principal.grid(
            row=0,
            column=1,
            sticky="nswe"
        )

        self.janela_principal.grid_rowconfigure(
            0,
            weight=1
        )

        self.janela_principal.grid_columnconfigure(
            0,
            weight=1
        )

        self.criar_abas()

    # ======================================================
    # BARRA LATERAL
    # ======================================================

    def criar_barra_lateral(self):

        self.titulo = ctk.CTkLabel(
            self.barra_lateral,
            text="Automações Meli",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        )

        self.titulo.pack(
            pady=(35, 30),
            padx=20
        )

        # Botão Automação
        self.botao_automacao = ctk.CTkButton(
            self.barra_lateral,
            text="Automação",
            height=40,
            command=lambda: self.mostrar_aba("automacao")
        )

        self.botao_automacao.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        # Botão Instruções
        self.botao_instrucoes = ctk.CTkButton(
            self.barra_lateral,
            text="Instruções de uso",
            height=40,
            command=lambda: self.mostrar_aba("instrucoes")
        )

        self.botao_instrucoes.pack(
            pady=10,
            padx=20,
            fill="x"
        )

    # ======================================================
    # ABAS
    # ======================================================

    def criar_abas(self):

        self.frame_automacao = ctk.CTkFrame(
            self.janela_principal,
            fg_color="transparent"
        )

        self.frame_instrucoes = ctk.CTkFrame(
            self.janela_principal,
            fg_color="transparent"
        )

        self.criar_aba_automacao()
        self.criar_aba_instrucoes()

        self.mostrar_aba("automacao")

    # ======================================================
    # ABA AUTOMAÇÃO
    # ======================================================

    def criar_aba_automacao(self):

        self.frame_automacao.grid_columnconfigure(
            0,
            weight=1
        )

        # ==================================================
        # TÍTULO
        # ==================================================

        titulo = ctk.CTkLabel(
            self.frame_automacao,
            text="Automação de Comprovantes",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

        titulo.grid(
            row=0,
            column=0,
            padx=40,
            pady=(40, 10),
            sticky="w"
        )

        # ==================================================
        # DESCRIÇÃO
        # ==================================================

        descricao = ctk.CTkLabel(
            self.frame_automacao,
            text="Selecione o texto que será utilizado como parâmetro de busca.",
            font=ctk.CTkFont(
                size=15
            )
        )

        descricao.grid(
            row=1,
            column=0,
            padx=40,
            pady=(0, 30),
            sticky="w"
        )

        # ==================================================
        # SELEÇÃO DO PARÂMETRO
        # ==================================================

        label_parametro = ctk.CTkLabel(
            self.frame_automacao,
            text="Parâmetro de busca:",
            font=ctk.CTkFont(
                size=16,
                weight="bold"
            )
        )

        label_parametro.grid(
            row=2,
            column=0,
            padx=40,
            pady=(0, 10),
            sticky="w"
        )

        self.parametro = ctk.StringVar(
            value=""
        )

        self.menu_parametro = ctk.CTkOptionMenu(
            self.frame_automacao,
            variable=self.parametro,
            values=[
                "Cashback Mercado Pago",
                "Recibiste una acreditación en tu cuenta."
            ],
            command=self.parametro_selecionado,
            width=500,
            height=40
        )

        self.menu_parametro.grid(
            row=3,
            column=0,
            padx=40,
            pady=(0, 30),
            sticky="w"
        )

        # ==================================================
        # ÁREA PARA COLAR OS TEXTOS
        # ==================================================

        self.frame_textos = ctk.CTkFrame(
            self.frame_automacao,
            corner_radius=10
        )

        self.frame_textos.grid(
            row=4,
            column=0,
            padx=40,
            pady=10,
            sticky="ew"
        )

        self.frame_textos.grid_columnconfigure(
            0,
            weight=1
        )

        # Inicialmente escondemos essa área
        self.frame_textos.grid_remove()

        # ==================================================
        # TÍTULO DO CAMPO
        # ==================================================

        self.label_textos = ctk.CTkLabel(
            self.frame_textos,
            text="Cole os textos abaixo:",
            font=ctk.CTkFont(
                size=16,
                weight="bold"
            )
        )

        self.label_textos.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 10),
            sticky="w"
        )

        # ==================================================
        # CAMPO DE TEXTO
        # ==================================================

        self.campo_textos = ctk.CTkTextbox(
            self.frame_textos,
            height=180
        )

        self.campo_textos.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 20),
            sticky="ew"
        )

        # ==================================================
        # BOTÃO INICIAR
        # ==================================================

        self.botao_iniciar = ctk.CTkButton(
            self.frame_textos,
            text="Iniciar automação",
            height=40,
            command=self.iniciar_automacao
        )

        self.botao_iniciar.grid(
            row=2,
            column=0,
            padx=20,
            pady=(0, 20),
            sticky="w"
        )

    # ======================================================
    # ABA INSTRUÇÕES
    # ======================================================

    def criar_aba_instrucoes(self):

        self.frame_instrucoes.grid_columnconfigure(
            0,
            weight=1
        )

        self.frame_instrucoes.grid_rowconfigure(
            2,
            weight=1
        )

        # ==================================================
        # TÍTULO
        # ==================================================

        titulo = ctk.CTkLabel(
            self.frame_instrucoes,
            text="Instruções de uso",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

        titulo.grid(
            row=0,
            column=0,
            padx=40,
            pady=(40, 10),
            sticky="w"
        )

        # ==================================================
        # SUBTÍTULO
        # ==================================================

        subtitulo = ctk.CTkLabel(
            self.frame_instrucoes,
            text="Siga os passos abaixo para utilizar a automação.",
            font=ctk.CTkFont(
                size=15
            )
        )

        subtitulo.grid(
            row=1,
            column=0,
            padx=40,
            pady=(0, 20),
            sticky="w"
        )

        # ==================================================
        # ÁREA DAS INSTRUÇÕES
        # ==================================================

        instrucoes = ctk.CTkTextbox(
            self.frame_instrucoes,
            font=ctk.CTkFont(
                size=14
            ),
            wrap="word"
        )

        instrucoes.grid(
            row=2,
            column=0,
            padx=40,
            pady=(0, 40),
            sticky="nsew"
        )

        texto_instrucoes = """
1. Selecione o parâmetro de busca

Escolha uma das opções disponíveis:

• Cashback Mercado Pago
• Recibiste una acreditación en tu cuenta.


2. Cole os textos

Após selecionar o parâmetro, cole no campo de texto as informações que serão utilizadas pela automação.


3. Inicie a automação

Clique no botão "Iniciar automação" para começar o processamento.


4. Aguarde a conclusão

Não feche a aplicação enquanto a automação estiver sendo executada.


Observações:

• Verifique se os textos foram copiados corretamente.
• Não altere o conteúdo antes de iniciar a automação.
• Caso ocorra algum erro, verifique se os dados inseridos estão no formato esperado.
"""

        instrucoes.insert(
            "1.0",
            texto_instrucoes
        )

        instrucoes.configure(
            state="disabled"
        )

    # ======================================================
    # MOSTRAR ABA
    # ======================================================

    def mostrar_aba(self, aba):

        # Esconde todas
        self.frame_automacao.grid_remove()
        self.frame_instrucoes.grid_remove()

        # Mostra a selecionada
        if aba == "automacao":

            self.frame_automacao.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        elif aba == "instrucoes":

            self.frame_instrucoes.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

    # ======================================================
    # PARÂMETRO SELECIONADO
    # ======================================================

    def parametro_selecionado(self, valor):

        # Mostra o campo somente depois da seleção
        self.frame_textos.grid()

        # Atualiza o texto do campo
        if valor == "Cashback Mercado Pago":

            self.label_textos.configure(
                text="Cole os textos relacionados ao Cashback Mercado Pago:"
            )

        elif valor == "Recibiste una acreditación en tu cuenta.":

            self.label_textos.configure(
                text="Cole os textos relacionados à acreditação:"
            )

    # ======================================================
    # INICIAR AUTOMAÇÃO
    # ======================================================

    def iniciar_automacao(self):

        parametro = self.parametro.get()

        textos = self.campo_textos.get(
            "1.0",
            "end"
        ).strip()

        if not parametro:

            print("Selecione um parâmetro.")

            return

        if not textos:

            print("Cole os textos antes de iniciar.")

            return

        print("Parâmetro selecionado:")
        print(parametro)

        print("\nTextos:")
        print(textos)

        # ==================================================
        # FUTURAMENTE ENTRA O PLAYWRIGHT
        # ==================================================


# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":

    app = App()
    app.mainloop()