class Persona:
  sueldo = 0
  egreso = 0
  prestamo="Negado"

  def __init__(self, sueldo, egreso):
        self.sueldo = sueldo
        self.egreso = egreso

class Prestamo:
    def validar_prestamo(self,persona):
      if (persona.sueldo >= 1000):
        if (persona.egreso < persona.sueldo):
          persona.prestamo="Aceptado"
	  print("Prestamo aceptado")
          return "Prestamo aceptado"
        else:
          return "Prestamo negado"
      else:
        if (persona.egreso < persona.sueldo):
          persona.prestamo="Aceptado"
          print("Prestamo aceptado")
          return "Prestamo aceptado"
        else:
          return "Prestamo negado"

