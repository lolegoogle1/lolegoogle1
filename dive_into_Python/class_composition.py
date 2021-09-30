import json


class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed


class PetExport:
    def export(self, dog):
        raise NotImplementedError


class ExportXML(PetExport):
    def export(self, dog):
        return """<xml version="1.0" encoding="utf-8">
<dog>
  <name>{0}</name>
  <breed>{1}</breed>
</dog>""".format(dog.name, dog.breed)


class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed,
        })


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)
        self._exporter = exporter

        if isinstance(exporter, PetExport):
            self._exporter = exporter
        else:
            self._exporter = ExportJSON()

    def export_(self):
        return self._exporter.export(self)


class MyDog(ExDog, Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed, exporter)


####################### CODE TESTING #########################

pug = MyDog("PieDie", "Pug", exporter=ExportXML())
print(pug.export_(), "\n")

dachshund = MyDog("DiePie", "Dachshund", exporter=ExportJSON())
print(dachshund.export_())
