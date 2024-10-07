### Link Shortener

Este é um aplicativo simples de encurtador de URLs construído com Flask. Ele permite que você encurte URLs longas e redirecione para elas usando um identificador curto.

## Funcionalidades

- Encurtar URLs longas.
- Redirecionar para URLs encurtadas.
- Verificar se uma URL já foi encurtada.

## Requisitos

- Python 3.x
- Flask
- Redis

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/Mateus-Lacerda/link-shortener.git
    cd link-shortener
    ```

2. Utilizando venv
    2.2. Crie um ambiente virtual e ative-o:

        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

    2.3. Instale as dependências:

        ```sh
        pip install -r requirements.txt
        ```

    2.4. Configure o Redis:

        Certifique-se de que o Redis está instalado e em execução na sua máquina.

3. Utilizando docker
    3.2. Instale o docker:

    3.3. Rode o encurtador:

        ```sh
        docker compose up --build
        ```

## Uso

1. Inicie o servidor Flask:

    ```sh
    flask run
    ```

2. Encurtar uma URL:

    Faça uma requisição POST para `/shorten` com um JSON contendo a URL que você deseja encurtar.

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"url": "http://example.com"}' http://127.0.0.1:5000/shorten
    ```

3. Redirecionar para uma URL encurtada:

    Acesse `/red/<short_id>` onde `<short_id>` é o identificador curto retornado pela requisição de encurtamento.

    ```sh
    curl -X GET http://127.0.0.1:5000/red/<short_id>
    ```

## Estrutura do Projeto

```plaintext
link-shortener/
│
├── src/
│   ├── __init__.py
│   ├── shortener.py
│   └── app.py
│
├── requirements.txt
├── README.md
└── ...
```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---
