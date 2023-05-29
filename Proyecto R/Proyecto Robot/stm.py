# Etiquetas para mostrar el estado, la basura reciclable, la basura no reciclable y los objetos recogidos
        self.label_estado = tk.Label(self, text="Estado actual: {}".format(self.estado_actual))
        self.label_estado.pack(pady=10)

        # Botones para realizar acciones
        self.button_iniciar_robot = tk.Button(self, text="Iniciar Robot", command=self.iniciar_robot)
        self.button_iniciar_robot.pack(pady=5)

        self.button_recolectar = tk.Button(self, text="Recolectar objeto", command=self.recolectar_objeto)
        self.button_recolectar.pack(pady=5)

        self.button_navegar = tk.Button(self, text="Navegar por el camino", command=self.navegar_camino)
        self.button_navegar.pack(pady=5)

        self.button_bote_reciclable = tk.Button(self, text="Bote de Reciclables", command=self.botar_reciclable)
        self.button_bote_reciclable.pack(pady=5)

        self.button_bote_no_reciclable = tk.Button(self, text="Bote de No Reciclables", command=self.botar_no_reciclable)
        self.button_bote_no_reciclable.pack(pady=5)

        self.button_soltar_objetos = tk.Button(self, text="Soltar Objetos", command=self.soltar_objetos)
        self.button_soltar_objetos.pack(pady=5)

        self.button_parado_emergencia = tk.Button(self, text="Parado de Emergencia", command=self.parado_de_emergencia)
        self.button_parado_emergencia.pack(pady=5)

        self.button_continuar = tk.Button(self, text="Continuar", command=self.continuar)
        self.button_continuar.pack(pady=5)

        # Etiquetas para mostrar la basura reciclable, la basura no reciclable y los objetos recogidos
        self.label_basura_reciclable = tk.Label(self, text="Basura reciclable: {}".format(self.basura_reciclable))
        self.label_basura_reciclable.pack(pady=5)

        self.label_basura_no_reciclable = tk.Label(self, text="Basura no reciclable: {}".format(self.basura_no_reciclable))
        self.label_basura_no_reciclable.pack(pady=5)

        self.label_objetos_recogidos = tk.Label(self, text="Objetos recogidos: {}".format(self.objetos_recogidos))
        self.label_objetos_recogidos.pack(pady=5)