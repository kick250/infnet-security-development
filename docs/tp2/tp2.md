# Desenvolvimento Seguro de Aplicações Web TP2

Você chegou à segunda etapa de avaliação da disciplina. Este TP é formativo, serve para praticar threat modeling e autenticação sobre a API que você já construiu e para receber feedback específico sobre cada competência exercitada. Os resultados aqui não geram nota, mas ajudam a preparar o terreno para o Assessment.

Este TP avalia a competência de implementar threat modeling STRIDE e autenticação JWT em APIs FastAPI, cobrindo a elaboração de misuse cases, a categorização de ameaças com o framework STRIDE, a construção de um threat model completo com ativos e mitigações rastreáveis, o mapeamento de fronteiras de segurança e fluxo de dados entre partições, a implementação de autenticação OAuth2PasswordBearer com hashing bcrypt e verificação de ownership, e a implementação de JWT com MFA e escolha entre RBAC, ABAC e autorização por recurso, incluindo a seleção do fluxo OAuth 2.0 adequado para usuários finais e comunicação máquina-a-máquina. Os exercícios assumem que o eventos-api do TP1 já está construído e modularizado.

## Exercício 1

### Contexto

Antes de qualquer modelagem formal de ameaças, o time de segurança da empresa pede que cada squad pense como um atacante pensaria: quais ações mal-intencionadas alguém tentaria contra o eventos-api? Essa prática, chamada de misuse cases, precede o threat modeling formal e ajuda a equipe a enxergar o sistema pela perspectiva de quem quer explorá-lo, e não apenas pela perspectiva de quem quer que ele funcione. Em uma retrospectiva recente, o time identificou que pular essa etapa em outro projeto levou a um threat model incompleto, que só cobria ameaças óbvias e deixou de fora vetores relacionados a dados de terceiros. Você foi designado para produzir a primeira rodada de misuse cases do eventos-api, cobrindo os principais vetores de ataque relevantes para uma API de gestão de eventos e inscrições, antes de a equipe avançar para a categorização formal com STRIDE.

### Tarefa
- Elabore pelo menos quatro misuse cases para o eventos-api, cada um descrevendo um ator malicioso, uma ação indesejada e o impacto potencial.
- Relacione cada misuse case a um vetor de ataque concreto observável na aplicação construída no TP1 (por exemplo, ausência de autenticação nas rotas de criação de evento).
- Priorize os misuse cases listados por impacto, justificando a ordem escolhida.


## Exercício 2

### Contexto

Com os misuse cases levantados, o próximo passo pedido pelo tech lead é categorizar as ameaças de forma sistemática usando o framework STRIDE, padrão adotado pela empresa para toda modelagem de ameaças de novos serviços antes de qualquer deploy em produção. A ideia é que cada componente da API (autenticação, rotas de eventos, banco de dados simulado) seja avaliado individualmente contra as seis categorias do STRIDE, para que nenhuma classe de ameaça relevante seja esquecida na análise, já que uma análise informal anterior, feita sem framework, deixou passar uma ameaça de elevação de privilégio que só foi descoberta em produção.

### Tarefa
- Aplique o framework STRIDE a pelo menos três componentes do eventos-api (por exemplo, rota de criação de evento, camada de autenticação futura, armazenamento de dados).
- Para cada componente, identifique pelo menos uma ameaça correspondente a uma das seis categorias STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).
- Registre os resultados em uma tabela com as colunas Componente, Categoria STRIDE, Ameaça identificada.


##  Exercício 3

### Contexto

O time de segurança quer consolidar o trabalho dos dois exercícios anteriores em um artefato único e formal: o threat model do eventos-api. Esse documento será usado como referência oficial nas próximas etapas da disciplina e também pelo time de operações para priorizar correções antes de qualquer exposição do serviço a usuários externos. Um threat model incompleto, sem mapeamento claro de ativos e superfícies de ataque, foi rejeitado recentemente em outro projeto da empresa por não permitir rastrear quais mitigações cobrem quais ameaças, o que obrigou a equipe a refazer o documento inteiro sob pressão de prazo. Você precisa evitar esse retrabalho entregando um artefato completo desde a primeira versão.

### Tarefa
- Construa o threat model do eventos-api, mapeando os ativos principais (dados de usuários, dados de eventos, credenciais futuras), as superfícies de ataque identificadas e as mitigações propostas para cada ameaça do Exercício 2.
- Garanta que cada ameaça do STRIDE mapeado no Exercício 2 apareça no threat model com pelo menos uma mitigação associada.
- Apresente o threat model em um documento único e legível, adequado para ser consultado por outro desenvolvedor sem contexto prévio.


## Exercício 4

### Contexto

Um arquiteto sênior revisando o eventos-api apontou que a modelagem de ameaças feita até aqui carece de uma visão formal da arquitetura do sistema: quais são os componentes reais, onde ficam as fronteiras de confiança entre eles e como os dados fluem de um componente a outro. Segundo ele, threat models construídos sem essa visão de partições tendem a ficar genéricos demais, cobrindo ameaças óbvias e deixando passar riscos específicos das fronteiras reais do sistema. Ele pediu que a equipe formalize essa visão, complementando o threat model já construído, antes de avançar para a implementação de autenticação na próxima etapa da disciplina.

### Tarefa
- Identifique as fronteiras de segurança do eventos-api, particionando o sistema em pelo menos três componentes distintos (por exemplo, cliente, camada de API, armazenamento de dados).
- Mapeie o fluxo de dados entre essas partições, indicando explicitamente onde uma requisição cruza uma fronteira de confiança.
- Relacione, em um parágrafo curto, como essa visão de partições confirma ou refina as ameaças já identificadas no threat model do Exercício 3.


## Exercício 5

### Contexto

A empresa está avaliando abrir parte do eventos-api para parceiros externos consumirem via integração automatizada, além dos usuários finais que acessam pelo navegador. Antes de decidir o modelo de autenticação, o tech lead pede uma análise dos vetores de ataque possíveis segundo os três eixos de segurança de APIs (design, implementação, infraestrutura), para garantir que a decisão de arquitetura considere riscos além da simples validação de senha. Em uma discussão recente com o time de infraestrutura, ficou claro que decisões de autenticação tomadas sem olhar para o eixo de infraestrutura já causaram exposição indevida de endpoints internos em outro serviço da empresa, então essa análise precisa ser levada a sério antes da implementação.

### Tarefa
- Para cada um dos três eixos de segurança de APIs (design, implementação, infraestrutura), identifique pelo menos um vetor de ataque relevante para o cenário de abertura do eventos-api a parceiros externos.
- Indique, para cada vetor identificado, se ele já está coberto pelo threat model construído anteriormente ou se representa uma lacuna nova.
- Justifique por que considerar os três eixos, e não apenas o eixo de implementação, é necessário antes de expor a API a consumidores externos.


## Exercício 6

### Contexto

Com a modelagem de ameaças consolidada, chegou a hora de implementar a primeira camada real de autenticação do eventos-api. O produto exige que apenas usuários cadastrados possam criar e gerenciar eventos, e que senhas nunca sejam armazenadas em texto plano, requisito não negociável levantado pelo time de segurança na revisão do threat model, depois de um incidente em outro projeto da empresa em que senhas ficaram expostas em um vazamento de banco de dados por estarem salvas sem hashing. Além disso, rotas de edição de evento precisam garantir que apenas o organizador dono do evento possa modificá-lo, fechando a lacuna de autorização que o threat model já havia identificado.

### Tarefa
- Implemente autenticação com OAuth2PasswordBearer no eventos-api, aplicando hashing de senha com bcrypt via passlib.
- Proteja a rota de edição de evento usando dependency injection do FastAPI, garantindo que apenas o organizador dono do evento (verificação de ownership) possa executá-la.
- Demonstre, com um teste manual via httpie ou similar, o comportamento da rota de edição para um usuário autenticado dono do evento e para um usuário autenticado que não é dono.


## Exercício 7

### Contexto

O time de compliance exige que sessões de usuário sigam boas práticas de segurança, incluindo expiração de token e suporte a múltiplos fatores de autenticação em contas administrativas, já que contas de administrador têm acesso a dados de todos os organizadores e participantes da plataforma. Ao mesmo tempo, o tech lead está decidindo entre RBAC e ABAC para controlar quem pode acessar quais recursos do eventos-api, já que o sistema terá papéis distintos (organizador, participante, administrador) com regras de acesso que podem variar por contexto, e uma escolha malfeita agora seria custosa de reverter depois que a base de usuários crescer.

### Tarefa
- Implemente JWT com OAuth2 no eventos-api, incluindo expiração de token e um fluxo simulado de segundo fator de autenticação (MFA) para o papel de administrador.
- Compare RBAC, ABAC e autorização por recurso, explicando qual modelo você recomendaria para o eventos-api e por quê, considerando os papéis organizador, participante e administrador.
- Documente a decisão de modelo de autorização em um parágrafo técnico, citando pelo menos um cenário concreto do domínio de eventos em que o modelo escolhido se aplica.


## Exercício 8

### Contexto

A empresa parceira que vai integrar via API pediu suporte a comunicação máquina-a-máquina (M2M), sem intervenção de um usuário humano no fluxo de autenticação, além do fluxo já existente para usuários finais autenticados pelo navegador. O contrato comercial assinado com o parceiro especifica exatamente quais operações ele pode executar, e o time jurídico da empresa exige que essa limitação seja tecnicamente garantida, não apenas descrita em papel. O time de segurança pede que os escopos de acesso sejam explícitos, para que o parceiro externo só consiga executar exatamente as operações autorizadas em contrato, nada além disso, mesmo que o token seja comprometido.

### Tarefa
- Selecione o fluxo OAuth 2.0 mais adequado para o cenário M2M do parceiro externo, justificando a escolha frente ao fluxo já usado para usuários finais.
- Configure escopos OAuth e claims JWT específicos para RBAC, distinguindo o escopo de um usuário organizador do escopo do parceiro M2M.
- Demonstre, com um exemplo de payload de token decodificado, quais claims e escopos diferenciam os dois tipos de cliente.


## Formato de entrega

- Todos os arquivos gerados (código-fonte, threat model, tabelas, documentos de decisão) devem ser compactados e entregues em um único arquivo .ZIP.
- Um relatório técnico curto deve ser entregue junto ao código, explicando as decisões tomadas em cada exercício.
- O código deve estar completo e organizado nos módulos já definidos no TP1.
- Evidências como prints de tela dos testes de autenticação e autorização devem ser incluídas onde solicitado.
- O prazo e o formato de entrega serão definidos pelo professor da disciplina.
- Assim que terminar, salve seu trabalho em PDF, nomeando
- O arquivo conforme a regra “nome_sobrenome_DR2_TP2.PDF” e poste como resposta a este TP.

Mãos à obra e bons estudos!