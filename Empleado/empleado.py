class Empleado:
    #Aqui va el codigo de empleado
    '''
    #Atributos
    '''
    nombre=''
    apellido=''
    '''
    #1=Masculino y 2 Femenino
    '''
    sexo=0
    salario=0
    '''
    # Metodos
    '''
    def CambiarSalario(self, nuevoSalario):
        #Aqui va el codigo del metodo
        return 0
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        #Aqui va el codigo de nuevo empleado
        return None
    
    def ConsultarSalario(self):
        #Aqui va el codigo del metodo
        return self.salario
    def ConsultarNombreCompleto(self):
        return self.nombre + self.apellido