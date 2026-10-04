import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Automações Hispanos")
        self.geometry("800x500")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Barra lateral
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

        # Janela principal
        self.janela_abas = ctk.CTkFrame(
            self,
            corner_radius=0
        )
        self.janela_abas.grid(
            row=0,
            column=1,
            sticky="nswe",
            padx=20,
            pady=20
        )

        # Cria os elementos da barra lateral
        self.criar_barra_lateral()

    def criar_barra_lateral(self):

        self.titulo = ctk.CTkLabel(
            self.barra_lateral,
            text="Automações Meli",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        self.titulo.pack(
            pady=(30, 10),
            padx=20
        )

        self.botao_principal = ctk.CTkButton(
            self.barra_lateral,
            text="Automações"
        )

        self.botao_principal.pack(
            pady=(30, 30),
            padx=10
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()