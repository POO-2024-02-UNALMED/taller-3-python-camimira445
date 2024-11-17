class TV:

    _numTV=0

    def __init__(self, marca,estado=False):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self._Control=None

        TV._numTV +=1

    @classmethod
    def getnumTV(cls):
        return cls._numTV
    
    @classmethod
    def setnumTV(cls,numTV):
        cls._numTV=numTV

    def turnOn(self):
        self._estado=True

    def turnOff(self):
        self._estado=False
    
    def canalUp(self):
        if (self.estado==True and 1<=self._canal<=120):
            self._canal +=1

    def canalDown(self):
        if (self.estado==True and 1<=self._canal<=120):
            self._canal -=1
    def volumenUp(self):
        if (self._estado==True and  0<=self._volumen<=7):
            self._volumen +=1

    def volumenDown(self):
        if (self._estado==True and  0<=self._volumen<=7):
         self._volumen -=1

    def getMmarca(self):
        return self._marca
    def setMarca(self, marca) :
        self._marca = marca
    
    def getCanal(self):
        return self._canal
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self._volumen
    
    def getControl(self):
        return self._Control
    def getEstado(self) :
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
        if (self._estado==True and  0<=self._volumen<=7):
            self._volumen +=1

    def volumenDown(self):
        if (self._estado==True and  0<=self._volumen<=7):
         self._volumen -=1

    
    

    

       
    

 