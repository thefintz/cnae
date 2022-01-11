import csv
import json
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('data')
parser.add_argument('out')
args = parser.parse_args()


with open(args.data, 'rt') as f:
    data = json.load(f)


def rows(data: dict) -> list:
    for item in data:
        yield (
            # subclasse
            item['id'],
            item['descricao'],
            '; '.join(item['observacoes']).replace('\r\n', ''),
            '; '.join(item['atividades']).replace('\r\n', ''),

            # classe
            item['classe']['id'],
            item['classe']['descricao'],
            '; '.join(item['classe']['observacoes']).replace('\r\n', ''),

            # grupo
            item['classe']['grupo']['id'],
            item['classe']['grupo']['descricao'],

            # divisao
            item['classe']['grupo']['divisao']['id'],
            item['classe']['grupo']['divisao']['descricao'],

            # secao
            item['classe']['grupo']['divisao']['secao']['id'],
            item['classe']['grupo']['divisao']['secao']['descricao'],
        )


header = [
    'subclasse_id',
    'subclasse_descricao',
    'subclasse_observacoes',
    'subclasse_atividades',
    'classe_id',
    'classe_descricao',
    'classe_observacoes',
    'grupo_id',
    'grupo_descricao',
    'divisao_id',
    'divisao_descricao',
    'secao_id',
    'secao_descricao',
]

with open(args.out, 'wt', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows(data))
