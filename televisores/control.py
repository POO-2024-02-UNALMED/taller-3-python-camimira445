class Control:
    def __init__(self):
        self._tv = None  

    def enlazar(self, tv):
        self._tv = tv
        tv.control = self

    def turnOn(self):
        self.tv.turnOn()

    def turn_off(self):
        self.tv.turnOff()
    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()
    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.canalDown()
    def gettv(self):
        return self._tv

    def settv(self, tv):
        self._tv = tv