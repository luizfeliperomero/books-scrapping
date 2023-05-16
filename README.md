# Web Scraping do site https://books.toscrape.com

## Descrição

Este Web Scraping tem como objetivo extrair informações sobre os preços dos livros de 3 a 5 estrelas em 5 requisições e mostrar para o usuário as variações.
(Como o site não possui variação de preço, essa variação é simulada pelo programa)

### Output

- **Terminal**\
No terminal é possível visualizar as variações de preço a cada atualização
  - Caso o preço tenha aumentado em relação a última atualização o valor será exibido na cor verde seguido de uma seta para cima
  - Caso o preço tenha diminuído em relação a última atualização o valor será exibido na cor vermelha seguido de uma seta para baixo
  - Caso o preço não tenha mudado em relação a última atualização o valor será exibido em amarelo  
  
- **Arquivo de texto**\
Um arquivo txt será gerado na pasta "output_files" contendo o nome seguido do preço do livro em cada atualização

- **Html**\
Um arquivo html será gerado na pasta "output_files" contendo o preço inicial e o preço final de cada livro, juntamente com a variação do preço desde a primeira até a última atualização

### Instalação

#### Docker Compose

1. git clone https://github.com/luizfeliperomero/books-scrapping.git
2. No diretório raíz: docker-compose up

#### Manualmente

Para instalar manualmente é necessário possuir Python instalado em sua máquina

1. git clone https://github.com/luizfeliperomero/books-scrapping.git
2. No diretório raíz: pip install beautifulsoup4
3. No diretório raíz: pip install colorama
4. No diretório raíz: python3 main.py

