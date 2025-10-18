# 📌 Gorgona
Gorgona é uma plataforma de gestão de negócio, organização de recursos e projeção de crescimento. Esse é um plicativo web para gestão de uma loja de cestas de presente, para uso real no negócio, com ferramentas gratuitas e servidor local. A IA do Gorgo pode funcionar como uma conselheira de negócios, analisando dados históricos, prevendo demandas e sugerindo estratégias de marketing ou reposição. Gorgo centraliza todas as operações da loja em um único painel, permitindo controle total sobre produtos, kits, insumos, taxas e vendas.
<br><br>
O escopo geral do sistema inclui:
- cadastro de produtos, kits e insumos,
- cadastro de taxas e impostos,
- geração automática de textos informativos para divulgação em redes sociais,
- cálculo automático de custos por kit,
- geração automática de preço de venda sugerido com margem de lucro configurável,
- análise de custos com sugestão inteligente de otimização e economia
- análise de procura e oferta com base em canais de comunicação e com sugestão inteligente de enganjamento 
- análise de datas de potencial de venda e sugestão inteligente de roteiro de marketing
- deashboard e relatórios de vendas, categorias mais vendidas, tiket médio, entre outros dados
- login seguro e nível de previlégio de acesso
<br><br>

Futuramente será integrado com site da loja para centralização de gestão, com interface gráfica configurável e login seguro. Será integrado com Inteligência artificial para análise de vendas e projeção de crescimento com base nas características em comum dos produtos vendidos, sazonalidades de datas comerciais e levantamento de acessos dos clientes às plataformas da loja por tipo de canal de comunicação, e análise de custos e sugestão do assitente virtual para cortes de gastos, incluindo geração de deashboard com gráficos e relatórios.
<br><br>
## ✨ Escopo atual

Aualmente o projeto é um MVP que abranje o cadastro e controle de produtos, facilitando o processo de criação de kits e divulgação em plataformas sociais e site.

## 🛠️ Acesso

- A documentação da API Autenticação estará disponível no Swagger: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)

## 🛠️ Funcionalidades

1. Cadastro de Insumos

- Form com nome, custo, venda, tamanho e categoria.
- Listagem com busca rápida.

2. Cadastro de Categorias de Insumo

- Lista pré-carregada (comida, bebida, cosmético…)
- Mas com opção de adicionar mais.

3. Cadastro de Kits

- Seleciona categoria do kit.
- Busca insumos por nome → adiciona com quantidade.
- Calcula:
  - Preço de custo = (soma dos custos * quantidades) + impostos.
  - Preço sugerido = custo + margem.
- Permite editar manualmente o preço de venda real.

4. Cadastro de Categorias de Kit

- Café da manhã, maternidade, etc.

5. Cadastro de Taxas

- Apenas 1 registro ativo (margem padrão, imposto padrão).
- Pode atualizar.

6. Listagem de Kits

- Tabela com: nome, preço venda real.
- Botão Ver Descritivo (gera texto pronto).
- Botão Detalhes (abre modal).
- Botão de Editar Kit

7. Geração de Descritivo (automática ao salvar kit)

Exemplo:

"Este é o modelo Kit Café da Manhã Premium, ele contém:

- 1 Café 200g
- 2 Pães de queijo (50g cada)
- 1 Suco natural 500ml

E fica no valor de R$ 129,90."

## 🚀 Tecnologias Utilizadas

- Backend: Python + Node.js
- Frontend: React
- Banco de Dados: PostgreSQL
- Servidor ASGI: Uvicorn
- Containerização: Docker
- Versionamento: GitHub

## 📁 Modelagem de dados

Insumo

- id
- nome
- preço_custo
- preço_venda
- tamanho (ex: unidade, 200g, 1L)
- categoria_insumo_id

Categoria de Insumo

- id
- nome (comida, bebida, cosmético, etc.)

Kit

- id
- nome
- categoria_kit_id
- preco_custo (soma insumos + impostos)
- preco_venda_sugerido (custo + margem de lucro)
- preco_venda_real (editável manualmente)

Categoria de Kit

- id
- nome (café da manhã, maternidade, etc.)

KitInsumo (tabela de ligação Kit ↔ Insumos)

- id
- kit_id
- insumo_id
- quantidade

Taxas

- id
- margem_lucro (%)
- impostos (%)

### Rodando com Docker

- Certifique-se de que Docker e Docker Compose estão instalados e rodando
- Abra o terminal da máquina e navegue até a pasta onde estão os arquivos do projeto
- Construa e rode os contêineres:
  
```
docker-compose up --build
```

- Para parar os containers:
  
```
docker-compose down
```
### Rodando Migrações com Alembic
Através do terminal do VSCode:

1. Entrar no container do microsserviço

```
docker compose exec nomedocontainer bash
```

2. Criar uma nova migration

Substitua "mensagem_da_migration" por algo descritivo, como "criar_tabela_usuario":
```
alembic revision --autogenerate -m "mensagem_da_migration"
```

3. Revisar a migration

Abra o arquivo recém-criado em alembic/versions/ e confira se as operações estão corretas. Ajuste manualmente se necessário.

4. Aplicar a migration no banco

```
alembic upgrade head
```

5. Conferir versão atual do banco

Mostra a versão aplicada mais recentemente:
```
alembic current
```

### Códigos HTTP usados na aplicação

200 - OK - Sucesso genérico <br>
400 - Bad Request - Parâmetros errados, JSON mal formatado, validação falhou
401 - Unauthorized - Usuário não enviou token ou token inválido
404 - Not Found - Recurso inexistente (usuario, produto, etc)
409 - Conflict - Duplicidade (email já existe, por exemplo)


## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
