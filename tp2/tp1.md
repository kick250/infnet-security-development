# Desenvolvimento Seguro de Aplicações Web TP1

Este TP avalia a competência de construir APIs REST com FastAPI aplicando fundamentos de segurança de software, cobrindo a estruturação modular de rotas com APIRouter, o controle de exposição de dados com response models Pydantic, a integração segura de templates Jinja2 e a aplicação da tríade CIA e de frameworks de referência (OWASP, NIST SSDF, MITRE) para mapear controles de segurança e construir um DFD com trust boundaries.

## Exercício 1

### Contexto

Você acabou de ser alocado como desenvolvedor backend júnior em uma startup que está migrando seu MVP de um sistema em Java Spring para Python. Sua primeira tarefa é montar a estrutura inicial de uma nova API REST chamada eventos-api, que futuramente gerenciará inscrições de usuários em eventos. O time de plataforma exige que todo novo serviço Python siga o padrão de isolamento de dependências da empresa, para evitar conflitos de versão entre projetos que compartilham a mesma máquina de desenvolvimento. Além disso, o serviço precisa expor pelo menos um endpoint funcional antes da reunião de daily de amanhã, para validar que o ambiente está corretamente configurado e acessível via navegador.

### Tarefa

1. Crie um ambiente virtual Python isolado para o projeto eventos-api usando virtualenv e instale o FastAPI e o uvicorn via pip, registrando as dependências em um arquivo requirements.txt.
2. Estruture uma aplicação FastAPI mínima em main.py, com uma rota GET / que retorna uma mensagem de status do serviço.
3. Suba o servidor com uvicorn em modo de hot-reload e capture, em texto ou print, a resposta da rota acessada via navegador ou httpie.


## Exercício 2

### Contexto

Com o ambiente validado, o time pede que a estrutura de rotas do eventos-api já nasça organizada, pensando na escala do serviço. Como o projeto crescerá para incluir múltiplos recursos (eventos, inscrições, usuários), o tech lead recusou a ideia de colocar todas as rotas em um único arquivo main.py, prática que já causou dificuldades de manutenção em outro projeto da empresa, onde um simples ajuste em uma rota de pagamentos quebrou silenciosamente uma rota não relacionada de notificações por estarem misturadas no mesmo arquivo. Você precisa demonstrar, com um recorte do domínio de eventos, como a aplicação vai crescer de forma modular desde o início, sem misturar responsabilidades de roteamento entre diferentes recursos do sistema, de modo que cada novo desenvolvedor consiga adicionar um recurso sem tocar em código de outro domínio.

### Tarefa

1. Implemente um APIRouter dedicado ao recurso eventos, com pelo menos três operações RESTful (por exemplo, listar eventos, criar evento, obter evento por id).
2. Registre esse router na aplicação principal usando include_router, mantendo o arquivo main.py livre de definições de rota específicas do domínio de eventos.
3. Justifique, em um parágrafo curto, por que separar routers por recurso facilita a manutenção de uma API que crescerá para múltiplos domínios.


## Exercício 3

### Contexto

O endpoint de criação de evento agora precisa retornar os dados do evento recém-criado, incluindo campos internos usados pelo time de operações, como o identificador do organizador responsável e um token de auditoria interno. Um colega do time revisando o código do endpoint alertou que, sem controle explícito do que é retornado, esses campos internos podem vazar para o cliente da API sem que ninguém perceba, especialmente à medida que o modelo de dados evolui e novos campos internos são adicionados por outros desenvolvedores sem revisão cuidadosa da resposta pública. Esse tipo de vazamento silencioso já expôs, em outro serviço da empresa, identificadores internos que facilitaram um ataque de enumeração. Você precisa decidir exatamente o que a API expõe na resposta e demonstrar por que a ausência desse controle é um risco real, não apenas teórico.

### Tarefa

1. Construa um response_model Pydantic para o endpoint de criação de evento, incluindo apenas os campos que devem ser visíveis ao cliente da API (excluindo campos internos como token de auditoria).
2. Escreva uma versão alternativa do mesmo endpoint sem response_model definido e compare, em texto, a resposta JSON retornada nos dois casos.
3. Explique, em até cinco linhas, qual dado sensível seria exposto na versão sem response_model e qual seria o impacto prático dessa exposição para o organizador do evento.


## Exercício 4

### Contexto

O eventos-api cresceu além do escopo inicial: agora existem rotas, modelos Pydantic e lógica de acesso a dados, todos ainda concentrados em poucos arquivos. O tech lead pediu que, antes de integrar o próximo desenvolvedor ao time, o projeto seja reorganizado em módulos claros, seguindo o mesmo padrão de estruturação usado em outros serviços FastAPI da empresa, padrão que reduziu em outros projetos o tempo de onboarding de novos desenvolvedores de semanas para poucos dias. A reorganização precisa deixar evidente onde um novo desenvolvedor deve procurar rotas, modelos de dados e lógica de acesso ao banco, sem depender de explicações verbais ou de perguntar diretamente a quem escreveu o código original.

### Tarefa

1. Reorganize o eventos-api em pelo menos três módulos separados: routes, models e database (ou nomes equivalentes), movendo o código existente para os arquivos corretos.
2. Garanta que a aplicação continue funcional após a reorganização, testando as rotas implementadas nos exercícios anteriores.
3. Documente, em um arquivo README.md curto, a responsabilidade de cada módulo criado.


##  Exercício 5

### Contexto

O time de produto solicitou uma página HTML simples para exibir a lista de eventos aos organizadores, sem exigir um frontend em JavaScript separado neste momento, já que a equipe de frontend só entra no projeto no próximo trimestre. Como o eventos-api já está estruturado, você precisa integrar uma camada de renderização de templates ao serviço existente, reaproveitando os dados que já são retornados pela API, sem duplicar lógica de acesso a dados entre a rota JSON e a rota HTML. Essa página será usada internamente pela equipe de operações, então precisa funcionar de forma simples e direta, sem complicar a arquitetura da API já construída nos exercícios anteriores.

### Tarefa

1. Integre o Jinja2 à aplicação FastAPI, criando uma rota que renderiza um template HTML listando os eventos cadastrados.
2. Utilize o motor de templates para exibir dinamicamente pelo menos três campos de cada evento (nome, data, organizador).
3. Confirme que a rota original em JSON (GET /eventos) continua funcionando normalmente, sem interferência da nova rota HTML.


## Exercício 6

### Contexto

Um colega do time de QA testou a página de eventos cadastrando um evento cujo nome incluía uma tag `<script>`, e percebeu que o conteúdo era refletido na página sem qualquer tratamento. Ele perguntou se isso é um problema real ou apenas um caso extremo pouco provável, já que nenhum usuário legítimo cadastraria um evento com esse tipo de nome. Ao mesmo tempo, o time de produto pediu que a página de detalhes do evento reutilize o mesmo cabeçalho e rodapé da página de listagem, para manter consistência visual sem duplicar código HTML entre as páginas, já que a duplicação de layout entre páginas já causou inconsistências visuais em uma entrega anterior do time.

### Tarefa

1. Reproduza o comportamento relatado pelo QA cadastrando um evento com um payload contendo uma tag `<script>` no campo nome e observe como o Jinja2 trata esse conteúdo por padrão.
2. Explique, em até seis linhas, por que a renderização de input do usuário sem escape adequado representa um risco de XSS, e o que o auto-escape do Jinja2 faz para mitigar isso.
3. Implemente herança de templates com um template base contendo cabeçalho e rodapé, e faça a página de listagem e a página de detalhes de evento herdarem dele.


## Exercício 7

### Contexto

Antes da apresentação do MVP ao time de segurança da empresa, seu tech lead pediu uma análise rápida da API construída até aqui usando a tríade CIA (confidencialidade, integridade e disponibilidade), framework padrão usado nas revisões de arquitetura da empresa em todo novo serviço antes de ir para produção. A ideia é identificar, de forma objetiva, onde a API eventos-api já oferece alguma garantia em cada um dos três pilares e onde ainda existem lacunas, para que a equipe priorize correções antes de expor o serviço a usuários externos, já que revisões anteriores de outros times mostraram que lacunas de disponibilidade costumam ser subestimadas quando a análise foca apenas em confidencialidade.

### Tarefa

1. Para a aplicação eventos-api construída nos exercícios anteriores, avalie um exemplo concreto de confidencialidade, um de integridade e um de disponibilidade, apontando o que já está implementado e o que ainda está em aberto.
2. Aponte pelo menos uma lacuna real observável no código atual para cada um dos três pilares da tríade CIA.
3. Registre essa avaliação em uma tabela simples com as colunas Pilar, Situação atual e Lacuna.


## Exercício 8

### Contexto

Como parte da preparação para as próximas etapas da disciplina, o time de segurança pediu um diagrama de fluxo de dados (DFD) básico da aplicação eventos-api, relacionando os frameworks de referência (OWASP, NIST SSDF e MITRE) às áreas onde eles se aplicam. Esse diagrama servirá de base para a modelagem de ameaças formal que a equipe fará nas próximas semanas, então precisa identificar claramente onde os dados sensíveis entram, são processados e saem da aplicação, além de onde ficam as fronteiras entre componentes confiáveis e não confiáveis, informação que, sem um DFD registrado, normalmente fica apenas na memória de quem escreveu o código original e se perde quando a pessoa sai do time.

### Tarefa

1. Construa um DFD básico do eventos-api, representando pelo menos: entrada de dados do usuário, processamento na API e armazenamento (mesmo que simulado), destacando as trust boundaries entre eles.
2. Associe, em uma tabela, os frameworks OWASP, NIST SSDF e MITRE a um controle de segurança concreto já discutido nos exercícios anteriores (por exemplo, response_model, escape de templates, virtualenv).
3. Aponte no DFD pelo menos um fluxo de dados sensível (por exemplo, dados do organizador) e a trust boundary que ele atravessa.


### Formato de entrega
- Todos os arquivos gerados (código-fonte, README, DFD, tabelas) devem ser compactados e entregues em um único arquivo .ZIP.
- Um relatório técnico curto deve ser entregue junto ao código, explicando as decisões tomadas em cada exercício.
- O código deve estar organizado nos módulos definidos no Exercício 4 e completo, sem trechos comentados como placeholder.
- Evidências como prints de tela ou capturas em texto da resposta do servidor FastAPI em execução (Exercício 1), das rotas testadas e do template HTML renderizado devem ser incluídas onde solicitado.
- Assim que terminar, salve seu trabalho em um arquivo ZIP, nomeando-o conforme a regra “nome_sobrenome_DR2_TP1.ZIP” e envie como resposta a este TP.