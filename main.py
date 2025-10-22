from datetime import datetime
import requests
import pandas as pd

# Lugares nos quais você deseja buscar estabelecimentos
places = [""]

# A sua chave da PlacesAPI
API_KEY = ""

# Informações que você deseja retornar. Veja mais opções: https://developers.google.com/maps/documentation/places/web-service/text-search?hl=pt-br
FIELD_MASKS = ""

# Coloque o que deseja buscar. Por exemplo: restaurantes, estabelecimentos, oficinas.
typeBuild = ""

# Estado desejado. (RJ, Minas Gerais, etc)
state = ""

# Quantos resultados você deseja. O máximo é 20 mesmo que coloque um número maior
resultCount = 0

# Montando o header da requisição
headers = {
    "X-Goog-FieldMask": FIELD_MASKS,
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY
}

# Dados filtrados
filtered_results = []

# Dados brutos retornados por cada requisição
results = {}

# Iteração para cada lugar colocado em 'places'
for place in places:
    try:
        # Iteração para cada tipo de estabelecimento desejado
        req = requests.post("https://places.googleapis.com/v1/places:searchText", headers=headers,
                            json={"textQuery": f"{typeBuild} {place} {state}", "maxResultCount": resultCount})

        # Salvando o resultado por lugar retornado
        results[place] = req.json().get('places', [])
        # Essa parte está bem hardcoded. Você vai precisar tratar por conta própria e colocar os campos desejados.
        for index, place_result in enumerate(results[place]):

            # Exemplo de como tratei o nome dos resultados. obs: veja como tratar os dados. da forma que está, não irá funcionar.
            # Deixei um arquivo para exemplificar como será o retorno da requisição. place_example.json
            name = place_result.get("displayName", "")
            addressComponents = place.get("addressComponents", [])
            number = place.get("number", "")

            # Aqui eu utilizei um laço for, pois utilizei o addressComponents, que retorna um array com várias informações sobre endereço
            address = ""
            for component in addressComponents:
                if "sublocality" in component.get("types", []):
                    address = component.get("longText", "")
                    break

            # Utilizei uma condição if para salvar apenas lugares com telefones disponíveis, já que era o objetivo do projeto
            if number:
                filtered_results.append({
                    "Nome": name,
                })

    except requests.exceptions.RequestException as e:
        print(f"Error ao buscar por {place}. {e}")

# Por fim, monto um DataFrame
table = pd.DataFrame(filtered_results)

# Exporto dem um arquivo xlsx. Utilizo a biblioteca datetime para ter sempre arquivos de nomes diferentes.
table.to_excel(f"arquivo-{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx", index=False)
