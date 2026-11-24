# Fundamentos de Cibersegurança (Knowledge Base)

## Conceitos Essenciais
- **Vulnerabilidade:** Fraqueza ou falha em um sistema, código, configuração ou processo que pode ser explorada.
- **Ameaça:** Agente ou evento potencial capaz de explorar uma vulnerabilidade e causar dano (ex.: atacante externo, malware, erro operacional).
- **Risco:** Probabilidade de uma ameaça explorar uma vulnerabilidade combinada com o impacto resultante para o negócio ou ambiente.

## Tríade CIA (CID)
- **Confidencialidade:** Garantia de que a informação seja acessível apenas a pessoas e sistemas autorizados (protegida por criptografia, controle de acesso e hashing de senhas).
- **Integridade:** Garantia de que dados e sistemas não sejam alterados de forma indevida ou não autorizada (protegida por validação de entrada, consultas parametrizadas e controle de versões).
- **Disponibilidade:** Garantia de que sistemas e dados estejam acessíveis quando necessários (protegida por redundância, backups, rate limiting e hardening de rede).

## Boas Práticas Defensivas (AppSec & Infra)
- **Nunca confiar na entrada do usuário:** Validar, sanitizar e utilizar sempre *Prepared Statements* (consultas parametrizadas) para prevenir SQL Injection.
- **Princípio do Menor Privilégio:** Serviços e usuários devem operar apenas com as permissões estritamente necessárias.
- **Hardening de Acesso:** Desabilitar login root direto via SSH, exigir chaves criptográficas e restringir portas expostas com firewall (ex.: UFW).
- **Armazenamento Seguro de Credenciais:** Nunca armazenar senhas em texto plano; utilizar algoritmos adaptativos como Argon2id ou bcrypt.
