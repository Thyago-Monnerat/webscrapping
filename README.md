# 🚀 WebScrapping com Python + PlacesAPI(new)

### Objetivo do projeto é simples: retornar lugares de interesse (lojas, restaurantes, etc) com base na região informada (cidade, estado, bairro).

#### *🚨 Aviso Rápido: Antes de usar, recomendo fortemente que você se informe sobre o custo e o uso geral da Places API e do Google Cloud.*
---
### 📖 Documentação
**1. Chaves da API**  

Você vai precisar de uma chave API válida da **PlacesAPI**  
[Veja como pegar a sua](https://developers.google.com/maps/documentation/places/web-service/get-api-key?hl=pt-br)

O sistema usa o modo de busca TextSearch

**2. Stack utilizada**  

O projeto é feito em Python 3.14, e utiliza as seguintes bibliotecas:  

- **Pandas** para montagem e manipulação de DataFrames com os dados extraídos.

- **Openpyxl** para exportação do DataFrame em arquivo .xlsx (Excel). *(ela não é importada explicitamente, mas o pandas a usa para exportar como xlsx)*

- **Datetime** para salvar o arquivo com um nome único, integrando a data e hora atual ao nome do arquivo.

- **Requests** para requisições Http.

**3. Como Funciona**  
- Você adiciona os lugares desejados (os termos de busca/regiões) em um array no código.

- O programa itera sobre essa lista, fazendo uma requisição à Places API para cada item.

- A API retorna os dados desejados (Nome, Telefone, Bairro, etc.) e o programa os organiza em um único arquivo Excel.
---  
📄 O arquivo final ficou nesse modelo: [modelo_arquivo.pdf  ](./arquivo-20251020_2243351.pdf)  

---  
### ⚠️ Observações Importantes

**Atenção ao Custo**: Cada requisição à Places API tem um custo. Verifique o limite gratuito disponível e monitore seu consumo no Google Cloud para evitar surpresas na fatura!

**Limite de Resultados**: Atualmente, a requisição utilizada (Nearby Search/Text Search) não ultrapassa o limite de 20 resultados por busca, por regras de design da API (a versão New não possui paginação).

**Uso Prático**: Esta lógica foi criada para resolver um problema real de um cliente, transformando um desafio de scrapping manual em uma solução robusta via API. Sinta-se livre para adaptar e brincar com o programa!


