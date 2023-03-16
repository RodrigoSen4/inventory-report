# :chart_with_downwards_trend: Inventory Reports :chart_with_upwards_trend:

Bem vindo ao repositório do projeto Inventory Reports. Projeto que foi desenvolvido um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados. 

Esses dados de estoque poderão ser obtidos de diversas fontes:

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

<strong>Habilidades utilizadas no Projeto:</strong>

  <ul>
    <li>Orientação a Objetos em Python;</li>
    <li>Padrões de projeto;</li>
    <li>Leitura e escrita de arquivos (XML, CSV, JSON).</li>
  </ul>

<strong>Executando o Projeto:</strong>

<details>
  <summary><strong>Ambiente Virtual</strong></summary><br />

  O Python oferece um recurso de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>Executando Projeto</strong></summary><br />
  
  O comando a ser executado será `inventory_report`. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip:

  <code>pip install .</code>

  Agora você poderá chamar o comando `inventory_report` passando seus argumentos:
  
  <code>inventory_report `argumento1` `argumento2`</code>

  - **argumento1** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

  - **argumento2** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.
  
  Outra opção é invocar o comando assim:

  <code>python3 -m inventory_report.main argumento1 argumento2</code>

  Exemplo:

    ```bash
  inventory_report inventory_report/data/inventory.csv simples
  ```

    ```bash
  inventory_report inventory_report/data/inventory.json simples
  ```

    ```bash
  inventory_report inventory_report/data/inventory.xml simples
  ```

  Desta forma você conseguirá interagir gerar o relatório com o comando.

</details>

