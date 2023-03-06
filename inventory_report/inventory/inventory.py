import csv
import json
from xml.etree import ElementTree as ELT
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    @staticmethod
    def read_file(file, file_type):
        if file_type == "csv":
            arquivo = csv.DictReader(file, delimiter=",", quotechar='"')
            info = [row for row in arquivo]
            return info

        if file_type == "json":
            return json.load(file)

        if file_type == "xml":
            xml = ELT.parse(file).getroot()
            info = [
                    {itm.tag: itm.text for itm in product} for product in xml
                ]
            return info

    @staticmethod
    def import_data(path, type):
        path_type = path.split('.')[1]
        with open(path, encoding="utf-8") as file:
            info = Inventory.read_file(file, path_type)

        if type == "simples":
            return SimpleReport.generate(info)
        if type == "completo":
            return CompleteReport.generate(info)
