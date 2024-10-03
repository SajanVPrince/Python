# ABSTRACTION
# -----------

from abc import ABC,abstractmethod
class syn(ABC):
    @abstractmethod
    def reg(self):
        pass

    def python(self):
        print('notes')

class std(syn):
    def reg(self):
        name=input('enter your name : ')
    def note(self):
        print('notes')
    
class staff(syn):
    def reg(self):
        print('reg')

staff1=staff()
staff1.reg()

sajan=std()
sajan.reg()