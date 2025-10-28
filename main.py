from datetime import datetime
import requests
import pandas as pd

# Lugares nos quais você deseja buscar estabelecimentos
places = [
  "lugar_placeholder",
  "lugar_placeholder",
  "lugar_placeholder",
]

# A sua chave da PlacesAPI
API_KEY = ""

# Informações que você deseja retornar, nesse caso, estou buscando nome, componentes de endereço e número nacional. Veja mais opções: https://developers.google.com/maps/documentation/places/web-service/text-search?hl=pt-br
FIELD_MASKS = "places.displayName,places.addressComponents,places.nationalPhoneNumber"

# Coloque o que deseja buscar. Por exemplo: restaurantes, estabelecimentos, oficinas.
place_types = ["restaurantes", "estabelecimentos", "oficinas"]

# Estado desejado. (RJ, Minas Gerais, etc)
state = "UF"

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

# Iteração para cada lugar colocado em 'places'
for place in places:
    # Iteração para cada tipo de estabelecimento desejado.
    for place_type in place_types:
        try:
            req = requests.post("https://places.googleapis.com/v1/places:searchText", headers=headers,
                                json={"textQuery": f"{place_type} {place} {state}", "maxResultCount": resultCount})

            # Salvando o resultado por lugar retornado
            # Deixei um arquivo para exemplificar como será o retorno da requisição. place_example.json
            data = req.json().get('places', [])

            # Iteração nos dados brutos vindos da requisição.
            for p in data:
                # Extraindo os dados desejados.
                name = p.get("displayName", {}).get("text", "")
                addressComponents = p.get("addressComponents", [])
                number = p.get("nationalPhoneNumber", "")

                # Aqui eu utilizei um laço for, pois utilizei o addressComponents, que retorna um array com várias informações sobre endereço
                address = ""
                for component in addressComponents:
                    # Sublocality se refere ao bairro. Dado que eu estava buscando
                    if "sublocality" in component.get("types", []):
                        address = component.get("longText", "")
                        break

                # Utilizei uma condição if para salvar apenas lugares com telefones disponíveis, já que era o objetivo do projeto
                if number:
                    filtered_results.append({
                        "Nome": name,
                        "Bairro": address,
                        "Telefone": number,
                        "Tipo": place_type,
                        "Cidade": place
                    })

        except requests.exceptions.RequestException as e:
            print(f"Error ao buscar por {place}. {e}")

# Por fim, monto um DataFrame
table = pd.DataFrame(filtered_results)

# Exporto dem um arquivo xlsx. Utilizo a biblioteca datetime para ter sempre arquivos de nomes diferentes.
table.to_excel(f"arquivo-{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx", index=False)
