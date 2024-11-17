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
    def setControl(self, control) :
        self._control = control
   
    def setPrecio(self,precio):
        self._precio=precio
    def setVolumen(self, volumen) :
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self,volumen):
        self._volumen=volumen

    def getControl(self):
        return self._Control
    
    def setControl(self,control):
      self._control=control

    def setCanal(self, canal) :
        if self._estado and 1 <= canal <= 120:
            self._canal = canal

    
    

    

       
    

 