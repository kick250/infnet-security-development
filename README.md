# TP2 - API de Eventos
API de eventos implementada com objetivo de cumprir os exercicios exigidos em [Exercicios TP1](./docs/tp2/tp2.md).

## Respostas para perguntas escritas no pdf breno_lobato_DR2_TP2.md

## Módulos do Projeto
### app
#### routes
Aqui ficam os componentes responsáveis pelas rotas da nossa api de eventos, elas são a porta de entrada para os recursos que nossa api proporciona.

#### models
Aqui ficam os componentes responsáveis por encapsular os formatos de entrada e saída dos nossos endpoints.

#### databases
Esse módulo armazena componentes e arquivos relacionados aos bancos de dados que nossa aplicação usar, como configuração de conexões e migrações.

#### repositories
Esse módulo armazena componentes responsáveis pelo logica de armazenamento das entidades(ex: eventos e usuarios), desacoplando a implementação do banco da logica de negócio.

#### static
Esse módulo armazena os arquivos estáticos da nossa aplicação.

#### templates
Esse módulo armazena os templates que servem de base para rendenizar o frontend.

### docs
Nessa pasta ficam a documentação do nosso projeto, assim como prints para cada exercicio proposto no TP1.