# 🛡️ DIO Agent — Especialização em Cibersegurança e AppSec

Projeto desenvolvido para o desafio **DIO Agent**, especializando o agente de IA para atuar como um **Mentor de Cibersegurança Defensiva e Application Security (AppSec)** utilizando o harness **Hermes Agent** em ambiente Ubuntu Linux.

---

## 🎯 O que o agente aprendeu

1. **Análise e Remediação de Código Vulnerável (`app.py`):**
   - Identificação de **SQL Injection** por concatenação direta de strings (`f-string` em consulta SQLite).
   - Mapeamento com o framework **MITRE ATT&CK (`T1190` – Exploit Public-Facing Application)**.
   - Refatoração segura com **consultas parametrizadas (`?`)** e gerenciamento de conexão (`contextlib.closing`), além de recomendação de hashing seguro (**Argon2 / bcrypt**).

2. **Nova Skill Defensiva (`skills/vulnerability-analysis/SKILL.md`):**
   - **Triagem antes da ação:** O agente recusa dar comandos genéricos sem antes fazer de 3 a 5 perguntas de contexto sobre exposição de rede, versões, autenticação, criticidade dos dados e controles ativos.
   - **Diagnóstico Padronizado de Risco:** Classificação estruturada por **Impacto**, **Probabilidade**, **Severidade Final**, pilares da **Tríade CIA** afetados, referências **CWE / MITRE ATT&CK** e plano de mitigação priorizado.

3. **Base de Conhecimento e Persona:**
   - `agent/knowledge/security-basics.md`: Definições de vulnerabilidade, ameaça, risco, Tríade CIA e boas práticas defensivas.
   - `agent/persona.md` & `AGENTS.md`: Incorporação da postura sênior de AppSec e registro oficial da skill `vulnerability-analysis`.

---

## 📂 Estrutura do Projeto

```text
dio-agente-appsec/
├── AGENTS.md                              # Regras centrais e tabela de skills registradas
├── app.py                                 # Código de laboratório corrigido contra SQL Injection
├── agent/
│   ├── persona.md                         # Identidade e postura defensiva do mentor
│   └── knowledge/
│       └── security-basics.md             # Fundamentos de segurança, Tríade CIA e boas práticas
├── skills/
│   └── vulnerability-analysis/
│       ├── SKILL.md                       # Roteiro operacional da skill de análise de vulnerabilidades
│       └── README.md                      # Documentação e exemplos de uso da skill
└── docs/
    └── evidencias/                        # Capturas de tela dos testes e validações
```

---

## 🧪 Evidências de Execução

1. **Análise inicial do `app.py` vulnerável:** Detecção de SQL Injection e mapeamento MITRE ATT&CK `T1190`.
2. **Remediação e validação automatizada:** Aplicação de consulta parametrizada (`?`) e teste com payload `' OR '1'='1 --` bloqueado.
3. **Ativação da skill `vulnerability-analysis` (Triagem):** Perguntas de contexto antes de sugerir comandos para um servidor Ubuntu exposto.
4. **Diagnóstico estruturado final:** Matriz de risco com **Impacto**, **Probabilidade**, **Severidade**, **Tríade CIA** e plano defensivo priorizado.

> *Nota ética: Todos os testes e cenários deste repositório foram conduzidos exclusivamente em ambiente controlado de laboratório para fins educacionais e defensivos.*
