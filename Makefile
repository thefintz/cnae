.PHONY: download

URL?=https://servicodados.ibge.gov.br/api/v2/cnae

download:
	curl $(URL)/secoes | jq . > secoes.json
	curl $(URL)/divisoes | jq . > divisoes.json
	curl $(URL)/grupos | jq . > grupos.json
	curl $(URL)/classes | jq . > classes.json
	curl $(URL)/subclasses | jq . > subclasses.json
