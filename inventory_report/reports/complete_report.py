from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    # Usei a collection counter para facilitar,
    # a montagem da string do retorno pedido
    # https://www.digitalocean.com/community/tutorials/python-counter-python-collections-counter
    # https://www.youtube.com/watch?v=fBk8BtSQQoA

    @classmethod
    def generate(cls, item):
        complete_report = super().generate(item) + '\n' + cls.empresa(item)
        return complete_report

    @staticmethod
    def empresa(list):
        empresa = Counter(item['nome_da_empresa'] for item in list)
        empresa_e_itens = ''

        for name, qtd in empresa.items():
            empresa_e_itens += f'- {name}: {qtd}\n'

        return f'Produtos estocados por empresa:\n{empresa_e_itens}'
