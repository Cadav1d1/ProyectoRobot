import tkinter as tk
import random

class RobotUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz de Usuario del Robot")
        self.geometry("500x500")

        # Variables de estado y contadores
        self.estado_actual = "Robot Apagado"
        self.camino = []
        self.basura_reciclable = {"Cartón": 0, "Plástico": 0, "Metal": 0}
        self.basura_no_reciclable = 0
        self.objetos_recogidos = 0

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

    def iniciar_robot(self):
        # Acción para iniciar el robot
        if self.estado_actual == "Robot Apagado":
            self.estado_actual = "Robot Encendido"
            self.actualizar_estado("Robot encendido")
        else:
            self.actualizar_estado("El robot ya está encendido")

    def recolectar_objeto(self):
        # Acción para recolectar un objeto
        if self.objetos_recogidos < 3:
            objeto_reciclable = random.choice(["Reciclable", "No Reciclable"])
            if objeto_reciclable == "No Reciclable":
                self.basura_no_reciclable += 1
                self.actualizar_estado("Objeto no reciclable recolectado")
            else:
                tipo_basura_reciclable = random.choice(list(self.basura_reciclable.keys()))
                self.basura_reciclable[tipo_basura_reciclable] += 1
                self.actualizar_estado("Objeto reciclable recolectado: {}".format(tipo_basura_reciclable))

            self.objetos_recogidos += 1
            self.actualizar_etiquetas_basura()
            self.actualizar_etiqueta_objetos_recogidos()
        else:
            self.actualizar_estado("Límite de objetos recogidos alcanzado")

    def navegar_camino(self):
        # Acción para navegar por el camino
        if len(self.camino) > 0:
            self.actualizar_estado("Navegando por el camino...")
            for paso in self.camino:
                self.actualizar_estado("Paso: {}".format(paso))
                # Simulación de movimiento del robot
                # Realizar acciones correspondientes en cada paso (giros, desplazamientos, etc.)

            self.actualizar_estado("Llegada al destino")
            self.camino = []  # Reiniciar el camino después de llegar al destino
        else:
            self.actualizar_estado("No hay camino definido")

    def botar_reciclable(self):
        # Acción para botar la basura reciclable en el bote adecuado
        if self.estado_actual == "Bote de Reciclables":
            if any(self.basura_reciclable.values()):
                self.basura_reciclable = {"Cartón": 0, "Plástico": 0, "Metal": 0}
                self.objetos_recogidos = 0  # Reiniciar el conteo de objetos recolectados
                self.actualizar_etiquetas_basura()
                self.actualizar_etiqueta_objetos_recogidos()
                self.actualizar_estado("Basura reciclable botada correctamente")
            else:
                self.actualizar_estado("No hay basura reciclable para botar")
        else:
            self.actualizar_estado("Error: No estás en el lugar correcto para botar basura reciclable. Corrigiendo...")
            self.basura_reciclable = {"Cartón": 0, "Plástico": 0, "Metal": 0}
            self.objetos_recogidos = self.basura_no_reciclable # Reiniciar el conteo de objetos recolectados
            self.actualizar_etiquetas_basura()
            self.actualizar_etiqueta_objetos_recogidos()
            self.actualizar_estado("Basura reciclable botada correctamente")
    def botar_no_reciclable(self):
        # Acción para botar la basura reciclable en el bote adecuado
        if self.estado_actual == "Bote No Reciclables":
            if any(self.basura_no_reciclable.values()):
                self.basura_no_reciclable = 0
                self.objetos_recogidos = 0  # Reiniciar el conteo de objetos recolectados
                self.actualizar_etiquetas_basura()
                self.actualizar_etiqueta_objetos_recogidos()
                self.actualizar_estado("Basura No reciclable botada correctamente")
            else:
                self.actualizar_estado("No hay basura no reciclable para botar")
        else:
            self.actualizar_estado("Error: No estás en el lugar correcto para botar basura no reciclable. Corrigiendo...")
            self.objetos_recogidos = self.objetos_recogidos-self.basura_no_reciclable# Reiniciar el conteo de objetos recolectados
            self.basura_no_reciclable = 0
            self.actualizar_etiquetas_basura()
            self.actualizar_etiqueta_objetos_recogidos()
            self.actualizar_estado("Basura no reciclable botada correctamente")

    def soltar_objetos(self):
        # Acción para soltar los objetos recolectados
        if self.objetos_recogidos > 0:
            self.basura_reciclable = {"Cartón": 0, "Plástico": 0, "Metal": 0}
            self.basura_no_reciclable = 0
            self.objetos_recogidos = 0
            self.actualizar_etiquetas_basura()
            self.actualizar_etiqueta_objetos_recogidos()
            self.actualizar_estado("Objetos soltados correctamente")
        else:
            self.actualizar_estado("No hay objetos para soltar")

    def parado_de_emergencia(self):
        # Acción para realizar un parado de emergencia
        if self.estado_actual != "Robot Apagado":
            self.camino = []  # Reiniciar el camino en caso de parado de emergencia
            self.estado_actual = "Robot Apagado"
            self.actualizar_estado("Parado de emergencia. Robot apagado")
        else:
            self.actualizar_estado("El robot ya está apagado")

    def continuar(self):
        # Acción para continuar las operaciones del robot
        if self.estado_actual == "Robot Apagado":
            self.estado_actual = "Robot Encendido"
            self.actualizar_estado("Continuando operaciones")
        else:
            self.actualizar_estado("El robot ya está encendido")

    def actualizar_estado(self, nuevo_estado):
        # Actualizar el estado actual del robot en la interfaz
        self.estado_actual = nuevo_estado
        self.label_estado.config(text="Estado actual: {}".format(self.estado_actual))

    def actualizar_etiquetas_basura(self):
        # Actualizar las etiquetas que muestran la cantidad de basura reciclable y no reciclable
        self.label_basura_reciclable.config(text="Basura reciclable: {}".format(self.basura_reciclable))
        self.label_basura_no_reciclable.config(text="Basura no reciclable: {}".format(self.basura_no_reciclable))

    def actualizar_etiqueta_objetos_recogidos(self):
        # Actualizar la etiqueta que muestra la cantidad de objetos recolectados
        self.label_objetos_recogidos.config(text="Objetos recogidos: {}".format(self.objetos_recogidos))


if __name__ == "__main__":
    app = RobotUI()
    app.mainloop()
    
