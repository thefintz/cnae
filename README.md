# CNAE

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Dump of all CNAE codes from [IBGE][1]

## Table of Contents

- [About](#about)
- [Install](#install)
- [Usage](#usage)

## About

Script that downloads all available data from IBGE's [API][2]. The API has
endpoints that return all data available. I am not sure if that is intended,
but makes our life easier ¯\\\_(ツ)\_/¯

The hierarchy of data is defined like so:

```
1. Seção
  2. Divisão
    3. Grupo
      4. Classe
        5. Subclasse
          6. Atividade econômica
```

However, if we fetch data from the last item of the hierarchy, using the
`/subclasse` endpoint, it will return all data from its parents. Which means,
it will return data from its `classe`, `grupo`, `divisao` and `secao`. See one
of the returned objects below:

<details>
<summary>Example JSON</summary>

```json
{
  "id": "4929902",
  "descricao": "TRANSPORTE RODOVIÁRIO COLETIVO DE PASSAGEIROS, SOB REGIME DE FRETAMENTO, INTERMUNICIPAL, INTERESTADUAL E INTERNACIONAL",
  "classe": {
    "id": "49299",
    "descricao": "TRANSPORTE RODOVIÁRIO COLETIVO DE PASSAGEIROS, SOB REGIME DE FRETAMENTO, E OUTROS TRANSPORTES RODOVIÁRIOS NÃO ESPECIFICADOS ANTERIORMENTE",
    "grupo": {
      "id": "492",
      "descricao": "TRANSPORTE RODOVIÁRIO DE PASSAGEIROS",
      "divisao": {
        "id": "49",
        "descricao": "TRANSPORTE TERRESTRE",
        "secao": {
          "id": "H",
          "descricao": "TRANSPORTE, ARMAZENAGEM E CORREIO"
        }
      }
    },
    "observacoes": [
      "Esta classe compreende - o transporte rodoviário coletivo de passageiros, sob o regime de fretamento\r\n- a organização de excursões em veículos rodoviários próprios\r\n- o transporte de empregados para terceiros\r\n- outros transportes rodoviários de passageiros, sem itinerário fixo, não especificados anteriormente",
      "Esta classe NÃO compreende - os serviços de ambulâncias (86.22-4)\r\n- o transporte escolar (49.24-8)\r\n- a locação de automóveis com motorista ou condutor (49.23-0)\r\n- a locação de automóveis sem motorista ou condutor (77.11-0)\r\n- o transporte turístico em veículos de tração animal (93.29-8)"
    ]
  },
  "atividades": [
    "ÔNIBUS COM MOTORISTA (CONDUTOR), INTERMUNICIPAL, INTERESTADUAL, INTERNACIONAL; LOCAÇÃO DE"
  ],
  "observacoes": [
    "Esta subclasse compreende - o transporte rodoviário coletivo de passageiros, sob regime de fretamento no âmbito intermunicipal, fora da região metropolitana, interestadual e internacional",
    "Esta subclasse NÃO compreende - a locação de automóveis com motorista ou condutor (4923-0/02)\r\n- o transporte especializado na locomoção de estudantes da rede pública ou privada (4924-8/00)\r\n- a locação de automóveis sem motorista ou condutor (7711-0/00)"
  ]
}
```

</details>

In order to convert the returned JSON into a CSV, we use CSV because it is
easier to import to a SQL database, we've created a python script that
generates it for us.

:warning: The script only works with the `subclasses.json` file.

## Install

The `makefile` uses [curl][3] and [jq][4].

For the python script, there is no dependencies. Just plain python.

## Usage

```
make download csv
```

Have fun!


[1]: https://www.ibge.gov.br/
[2]: https://servicodados.ibge.gov.br/api/docs/cnae?versao=2
[3]: https://curl.se/
[4]: https://stedolan.github.io/jq/
