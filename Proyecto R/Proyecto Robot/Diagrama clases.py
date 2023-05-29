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
