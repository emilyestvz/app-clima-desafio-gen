# App Clima - Desafio Final Gen AI

Este é um aplicativo de previsão do tempo em Python, que utiliza a API Open-Meteo. O projeto é estruturado em classes, com separação de responsabilidades, tratamento de erros, cache e testes automatizados.

## Como usar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o app:
   ```bash
   python main.py
   ```
3. Digite o nome de uma ou mais cidades (separadas por vírgula) para ver a previsão.

## Estrutura do Projeto
- `app/` - Código principal (API, serviço, utilitários, exceções)
- `main.py` - Interface de linha de comando
- `test_weather.py` - Testes automatizados
- `requirements.txt` - Dependências

## Testes
Execute:
```bash
python -m unittest test_weather.py
```

## Segurança e Ética
- Não armazene dados sensíveis.
- Use a API Open-Meteo conforme os termos de uso.
- Código gerado com auxílio de IA, revise antes de uso em produção.
- Licença: MIT

## Licença
MIT
