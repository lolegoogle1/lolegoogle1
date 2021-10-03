import os


class FileReader:
    """Class FileReader helps to read from the file"""

    def __init__(self, name):
        self._path = os.getcwd()
        self.name = name

    @staticmethod
    def find_file(path, name):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
            raise FileNotFoundError

    def read(self):
        try:
            path_to_file = self.find_file(self._path, self.name)
        except FileNotFoundError:
            print('There is no such file. Please, try again!')
            return ""
        else:
            with open(self.name, 'r') as file:
                return file.read()



