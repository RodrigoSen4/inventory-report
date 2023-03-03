from datetime import datetime


class SimpleReport:

    @staticmethod
    def generate(products):
        dataMaisAntiga = SimpleReport.data_mais_antiga(products)
        dataVencimento = SimpleReport.data_vencimento(products)
        nome_empresa = SimpleReport.nome_empresa(products)

        return "\n".join([
            f"Data de fabricação mais antiga: {dataMaisAntiga}",
            f"Data de validade mais próxima: {dataVencimento}",
            f"Empresa com mais produtos: {nome_empresa}",
        ])

    @staticmethod
    def data_mais_antiga(produtos):
        data = datetime.max
        for item in produtos:
            dateTime = datetime.strptime(
                item["data_de_fabricacao"], "%Y-%m-%d"
            )
            if data > dateTime:
                data = dateTime
        return data.strftime("%Y-%m-%d")

    @staticmethod
    def data_vencimento(produtos):
        data = datetime.max
        data_hoje = datetime.now()
        for item in produtos:
            data_vencimento = datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d"
            )
            if data_hoje < data_vencimento < data:
                data = data_vencimento
        return data.strftime("%Y-%m-%d")

    @staticmethod
    def nome_empresa(products):
        count = {}
        for item in products:
            if item["nome_da_empresa"] in count:
                count[item["nome_da_empresa"]] += 1
            else:
                count[item["nome_da_empresa"]] = 1
        return max(count, key=count.get)
