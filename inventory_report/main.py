from inventory_report.inventory.inventory import Inventory
import sys


def main():
    pass
    try:
        _, file_path, report_type = sys.argv
        data = Inventory.import_data(file_path, report_type)
        sys.stdout.write(data)
    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")
