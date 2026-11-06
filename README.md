# 🛡️Cybersecurity

**Um agente de inteligência artificial preparado para estudar, investigar e ensinar cibersegurança na prática.**

Este projeto nasceu a partir do [DIO Agent original](https://github.com/digitalinnovationone/dio-agent), mas ganhou uma nova direção: transformá-lo em um assistente especializado em **segurança da informação e análise defensiva de vulnerabilidades**.

A proposta é ir além de simplesmente explicar conceitos. Quero que o agente ajude a entender como as vulnerabilidades surgem, como podem ser identificadas, quais riscos representam e, principalmente, como corrigi-las.

## 🎯 O objetivo deste projeto

Desenvolver um agente que funcione como um mentor de cibersegurança, capaz de orientar estudos e análises técnicas de maneira didática, responsável e baseada em evidências.

A especialização contempla três áreas principais:

- **Segurança de aplicações web:** análise de vulnerabilidades em sites, sistemas, APIs, autenticação e aplicações desenvolvidas em PHP, JavaScript e outras tecnologias.
- **Segurança de infraestrutura:** fundamentos de redes, servidores Linux, configurações e serviços.
- **Análise de vulnerabilidades:** identificação de falhas, avaliação de riscos, consulta a referências como CVE e CWE, recomendações de correção e validação dos resultados.

## 🔍 Aprender na prática

Uma das partes deste projeto é um laboratório local de SQL Injection, criado para demonstrar como uma falha de segurança pode comprometer um processo de autenticação.

O laboratório possui duas versões:

- Uma aplicação vulnerável, utilizada para compreender a falha.
- Uma aplicação corrigida, que utiliza consultas parametrizadas e armazenamento seguro de senhas.

A ideia é seguir um ciclo de aprendizado:

**Identificar → Entender → Corrigir → Testar novamente.**

## 🧠 Como o agente trabalha

O agente foi configurado para não sair sugerindo testes sem antes entender o cenário. Ele deve considerar autorização, escopo, evidências e possíveis impactos antes de orientar uma análise.

Mais do que apontar uma falha, deve explicar o problema, demonstrar por que ele importa e apresentar caminhos para sua correção.

Este é um projeto de aprendizado e evolução contínua, desenvolvido com foco em cibersegurança defensiva e uso responsável das ferramentas de análise.

---

## 🚀 Conheça o projeto

Abaixo estão os principais arquivos e recursos desenvolvidos nesta especialização.******Cybersecurity

**Um agente de inteligência artificial preparado para estudar, investigar e ensinar cibersegurança na prática.**

Este projeto nasceu a partir do [DIO Agent original](https://github.com/digitalinnovationone/dio-agent), mas ganhou uma nova direção: transformá-lo em um assistente especializado em **segurança da informação e análise defensiva de vulnerabilidades**.

A proposta é ir além de simplesmente explicar conceitos. Quero que o agente ajude a entender como as vulnerabilidades surgem, como podem ser identificadas, quais riscos representam e, principalmente, como corrigi-las.

## 🎯 O objetivo deste projeto

Desenvolver um agente que funcione como um mentor de cibersegurança, capaz de orientar estudos e análises técnicas de maneira didática, responsável e baseada em evidências.

A especialização contempla três áreas principais:

- **Segurança de aplicações web:** análise de vulnerabilidades em sites, sistemas, APIs, autenticação e aplicações desenvolvidas em PHP, JavaScript e outras tecnologias.
- **Segurança de infraestrutura:** fundamentos de redes, servidores Linux, configurações e serviços.
- **Análise de vulnerabilidades:** identificação de falhas, avaliação de riscos, consulta a referências como CVE e CWE, recomendações de correção e validação dos resultados.

## 🔍 Aprender na prática

Uma das partes deste projeto é um laboratório local de SQL Injection, criado para demonstrar como uma falha de segurança pode comprometer um processo de autenticação.

O laboratório possui duas versões:

- Uma aplicação vulnerável, utilizada para compreender a falha.
- Uma aplicação corrigida, que utiliza consultas parametrizadas e armazenamento seguro de senhas.

A ideia é seguir um ciclo de aprendizado:

**Identificar → Entender → Corrigir → Testar novamente.**

## 🧠 Como o agente trabalha

O agente foi configurado para não sair sugerindo testes sem antes entender o cenário. Ele deve considerar autorização, escopo, evidências e possíveis impactos antes de orientar uma análise.

Mais do que apontar uma falha, deve explicar o problema, demonstrar por que ele importa e apresentar caminhos para sua correção.

Este é um projeto de aprendizado e evolução contínua, desenvolvido com foco em cibersegurança defensiva e uso responsável das ferramentas de análise.

---

## 🚀 Conheça o projeto

Abaixo estão os principais arquivos e recursos desenvolvidos nesta especialização.
## 🛡️ Especialização em Cibersegurança

O DIO Agent possui uma especialização em análise defensiva de vulnerabilidades, com foco em aplicações web, APIs, redes, Linux e infraestrutura.

### Skill vulnerability-analysis

A skill orienta o agente a verificar autorização, analisar evidências, identificar vulnerabilidades, avaliar riscos, recomendar correções e documentar retestes.

### Laboratório de SQL Injection

O projeto inclui um laboratório local com uma versão vulnerável e outra corrigida:

- labs/sql-injection/login_vulneravel.py
- labs/sql-injection/login_corrigido.py

Para executar os laboratórios:

    python .\labs\sql-injection\login_vulneravel.py
    python .\labs\sql-injection\login_corrigido.py

As credenciais fictícias são admin e senha123. O laboratório demonstra a exploração de SQL Injection e a proteção por consultas parametrizadas.

**Aviso:** utilize o laboratório exclusivamente em ambiente local e autorizado.
