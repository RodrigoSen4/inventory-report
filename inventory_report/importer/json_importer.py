from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.split('.')[1] != 'json':
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            return json.load(file)
