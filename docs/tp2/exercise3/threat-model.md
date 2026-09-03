## Threat Model - eventos-api

### Ativos principais

- **Dados de usuários:** Informações relacionadas aos organizadores e participantes.
- **Dados de eventos:** Informações dos eventos cadastrados.
- **Credenciais futuras:** Dados utilizados para autenticação dos usuários.

### Superfícies de ataque

- Rotas HTTP da API, principalmente criação e consulta de eventos.
- Entrada de dados fornecida pelo usuário.
- Armazenamento dos dados da aplicação.

### Propostas de mitigações

| Componente | Categoria STRIDE | Ameaça | Mitigação |
|---|---|---|---|
| ```EventsRouter#cr
eate_handler``` | Spoofing | Um atacante pode criar um evento sem autenticação, se passando por outro organizador. | Implementar autenticação obrigatória para criação de eventos. |
| `EventsRouter#get_a
ll_handler` | Information Disclosure | Um atacante pode consultar eventos sem checagem de permissão de acesso, obtendo informações que deveriam ser privadas. | Implementar autenticação obrigatória e verificar a permissão do usuário antes de retornar os dados. |
| `EventsReposit
ory#save` | Denial of Service | O armazenamento em memória pode consumir recursos além do esperado caso sejam enviados muitos eventos para a aplicação. | Implementar limites de requisições e utilizar armazenamento adequado. |