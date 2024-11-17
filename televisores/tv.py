class TV:

    _numTV=0

    def __init__(self, marca: Marca,estado:bool):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self._Control=None

        TV._numTV +=1

    @classmethod
    def getnumTV(cls)-> int :
        return cls._numTV
    
    @classmethod
    def setnumTV(cls,numTV:int):
        cls._numTV=numTV

    def turnOn(self):
        self._estado=True

    def turnOff(self):
        self._estado=False
    
    def canalUp(self):
        if (self._canal>=1 and self._canal<=120 and self._estado==True):
            self._canal +=1

    def canalDown(self):
         if (self._canal>=1 and self._canal<=120 and self._estado==True):
            self._canal -=1
    def volumenUp(self):
        if (self._volumen>=0 and self._volumen<=7 and self._estado==True):
            self._volumen +=1

    def volumenDown(self):
         if (self._volumen>=0 and self._volumen<=7 and self._estado==True):
            self._volumen -=1

   
    def getMmarca(self)-> Marca :
        return self._marca
    
    def getCanal(self)->int:
        return self._canal
    
    def getPrecio(self)->int:
        return self._precio
    
    def getVolumen(self)->int:
        return self._volumen
    
    def getControl(self)->Control:
        return self._Control
    def getEstado(self) -> bool:
        return self._estado
    
    def selfCanal(self,marca):
        self._marca=marca

    def getCanal(self):
        return self._canal
    
    def selfNombre(self,canal):
        self._canal=canal

   
    
    def set_precio(self,precio):
        self._precio=precio

    def get_volumen(self):
        return self._volumen
    
    def set_volumen(self,volumen):
        self._volumen=volumen

    def get_Control(self):
        return self._Control
    
    def set_Control(self,control):
      self._control=control

    

    

    def volumenUp(self):
        if (self._volumen>=0 and self._volumen<=7 and self._estado==True):
            self._volumen +=1

    def volumenDown(self):
         if (self._volumen>=0 and self._volumen<=7 and self._estado==True):
            self._volumen -=1

    
    

    

       
    

 