from abc import ABC, abstractmethod

class Zviera(ABC):
    @abstractmethod
    def zvuk(self):
        pass

class Pes(Zviera):
    def zvuk(self):
        return "Haf"
class Macka(Zviera):
    def zvuk(self):
        return "Mnau"

moje_zviera = Pes()

moj_pes = Pes()
moja_macka = Macka()
print(moj_pes.zvuk())
print(moja_macka.zvuk())

