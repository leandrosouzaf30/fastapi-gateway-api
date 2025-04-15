# FastAPI Gateway API

API Gateway para gerenciamento de contas, faturas e cartões de crédito.

## Descrição

Esta API Gateway foi desenvolvida usando FastAPI e fornece endpoints para gerenciar:
- Contas de usuários
- Faturas
- Cartões de crédito

A aplicação está containerizada com Docker e pode ser implantada em um cluster Kubernetes.

## Tecnologias Utilizadas

- Python 3.12
- FastAPI
- Poetry (gerenciamento de dependências)
- Docker
- Kubernetes
- Uvicorn (servidor ASGI)

## Estrutura do Projeto

```
.
├── src/
│   ├── app.py              # Aplicação principal FastAPI
│   ├── routers/            # Rotas da API
│   ├── schemas/            # Modelos Pydantic
│   ├── repositories/       # Camada de acesso a dados
│   └── domain/             # Regras de negócio
├── tests/                  # Testes automatizados
├── k8s/                    # Manifestos Kubernetes
│   └── manifests/
│       ├── 2-deployment.yaml
│       ├── 3-service.yaml
│       └── 4-ingress.yaml
├── Dockerfile              # Configuração do container
├── pyproject.toml          # Dependências do projeto
└── poetry.lock            # Versões fixas das dependências
```

## Requisitos

- Python 3.12 ou superior
- Docker
- Kubernetes (opcional, para implantação)
- Poetry (opcional, para desenvolvimento)

## Instalação

### Usando Docker

1. Construa a imagem:
```bash
docker build -t fastapi-gateway-api:latest .
```

2. Execute o container:
```bash
docker run -p 8000:8000 fastapi-gateway-api:latest
```

### Desenvolvimento Local

1. Instale o Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Instale as dependências:
```bash
poetry install
```

3. Execute a aplicação:
```bash
poetry run uvicorn src.app:app --reload
```

## Implantação no Kubernetes

1. Certifique-se de que o cluster Kubernetes está configurado:
```bash
kind get clusters
```

2. Carregue a imagem Docker no cluster:
```bash
kind load docker-image fastapi-gateway-api:latest
```

3. Aplique os manifestos Kubernetes:
```bash
kubectl apply -f k8s/manifests/
```

## Endpoints da API

### Health Check
- `GET /health`: Verifica o status da aplicação
  - Resposta: `{"status": "healthy"}`

### Contas
- `GET /accounts`: Lista todas as contas
- `POST /accounts`: Cria uma nova conta
- `GET /accounts/{id}`: Obtém detalhes de uma conta
- `PUT /accounts/{id}`: Atualiza uma conta
- `DELETE /accounts/{id}`: Remove uma conta

### Faturas
- `GET /invoices`: Lista todas as faturas
- `POST /invoices`: Cria uma nova fatura
- `GET /invoices/{id}`: Obtém detalhes de uma fatura
- `PUT /invoices/{id}`: Atualiza uma fatura
- `DELETE /invoices/{id}`: Remove uma fatura

## Documentação da API

A documentação interativa da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Configuração

A aplicação pode ser configurada através de variáveis de ambiente:

- `PORT`: Porta em que a aplicação irá escutar (padrão: 8000)

## Testes

Execute os testes com:
```bash
poetry run pytest
```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.
