class TV:
    _numTV=0
    def __init__(self,marca,estado=False):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._precio=500
        self._volumen=1
        self._Control=None
        TV.numTV +=1
   
    def get_marca(self):
        return self._marca
    
    def self_canal(self,marca):
        self._marca=marca

    def get_canal(self):
        return self._canal
    
    def self_nombre(self,canal):
        self._canal=canal
    def get_precio(self):
        return self._precio
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
    @classmethod
    def setnumTV(cls,numTV):
        cls._numTV=numTV
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    @classmethod
    def getnumTV(cls):
        return cls._numTV
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

    
    

    

       
    

 