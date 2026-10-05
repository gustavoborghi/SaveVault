# SaveVault

> Gerenciador automático de backups para saves de jogos.

## Sobre o projeto

O **SaveVault** é uma aplicação desenvolvida em Python para realizar **backups automáticos e versionados de saves de jogos armazenados localmente**.

O projeto será desenvolvido inicialmente para **SteamOS**, com foco em jogos executados localmente ou através do Proton. Nesses casos, os arquivos de save podem estar espalhados por diferentes diretórios e nem sempre contam com sincronização em nuvem.

O objetivo é monitorar os diretórios dos jogos e criar versões dos saves automaticamente sempre que houver alterações.

## Problema

Saves podem ser perdidos durante:

- formatação ou reinstalação do sistema;
- falhas de armazenamento;
- corrupção de arquivos;
- exclusão acidental;
- troca de computador;
- jogos sem suporte adequado a cloud save.

Além disso, em sistemas como SteamOS e Proton, a localização dos arquivos de save nem sempre é evidente.

O SaveVault busca automatizar o processo de backup, evitando que o usuário precise copiar os arquivos manualmente.

## Como funciona

O usuário cadastra um jogo e o diretório onde seus saves estão armazenados.

```text
Jogo: The Blood of Dawnwalker

Save:
/home/deck/.var/app/.../Dawnwalker
```

O SaveVault monitora o diretório e, quando identifica uma alteração, verifica se o conteúdo realmente mudou e cria uma nova versão do backup.

```text
Alteração detectada
        ↓
Verificação do conteúdo
        ↓
Criação do backup
        ↓
Registro no histórico
```

Os backups serão organizados por jogo e data:

```text
SaveVault/
└── backups/
    └── The Blood of Dawnwalker/
        ├── 2026-10-05_14-32-10/
        ├── 2026-10-05_15-17-42/
        └── 2026-10-05_16-04-21/
```

Posteriormente, o usuário poderá consultar o histórico e restaurar uma versão anterior.

## MVP

A primeira versão terá como foco:

- [ ] Cadastro manual de jogos
- [ ] Cadastro do diretório de save
- [ ] Monitoramento dos diretórios
- [ ] Detecção de alterações
- [ ] Criação automática de backups
- [ ] Verificação por hash para evitar duplicados
- [ ] Histórico de backups
- [ ] Restauração de versões anteriores
- [ ] Armazenamento das informações em SQLite

O MVP será desenvolvido e testado inicialmente em **SteamOS**.

## Arquitetura

O projeto será dividido em componentes independentes para permitir a adição de outras plataformas futuramente sem alterar o núcleo do sistema.

```text
              ┌──────────────────┐
              │    Interface     │
              └────────┬─────────┘
                       │
              ┌────────▼─────────┐
              │   Game Manager   │
              └────────┬─────────┘
                       │
              ┌────────▼─────────┐
              │   Save Monitor   │
              └────────┬─────────┘
                       │
              ┌────────▼─────────┐
              │  Backup Engine   │
              └────────┬─────────┘
                       │
             ┌─────────┴─────────┐
             │                   │
      ┌──────▼──────┐     ┌──────▼──────┐
      │    SQLite   │     │   Backups   │
      └─────────────┘     └─────────────┘
```

A plataforma inicial será o SteamOS. Futuramente, o projeto poderá receber suporte a outros ambientes, como:

- outras distribuições Linux;
- Windows;
- Nintendo Switch;
- outras fontes de saves.

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Watchdog](https://img.shields.io/badge/Watchdog-File%20Monitoring-informational?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![SteamOS](https://img.shields.io/badge/SteamOS-1A9FFF?style=for-the-badge&logo=steam&logoColor=white)

| Tecnologia | Utilização |
|---|---|
| Python | Desenvolvimento da aplicação |
| SQLite | Persistência dos dados |
| Watchdog | Monitoramento do sistema de arquivos |
| Git | Controle de versão |
| GitHub | Hospedagem e gerenciamento do projeto |
| SteamOS | Plataforma inicial |

## Roadmap

### Fase 1 — Fundação

- [ ] Estrutura inicial do projeto
- [ ] Ambiente Python
- [ ] Banco SQLite
- [ ] Modelo de jogos

### Fase 2 — Monitoramento

- [ ] Monitorar diretórios
- [ ] Detectar criação e modificação de arquivos
- [ ] Registrar eventos

### Fase 3 — Backup

- [ ] Criar backups versionados
- [ ] Implementar hash
- [ ] Evitar backups duplicados
- [ ] Registrar histórico

### Fase 4 — Restauração

- [ ] Listar versões disponíveis
- [ ] Selecionar backup
- [ ] Restaurar save
- [ ] Criar backup de segurança antes da restauração

### Fase 5 — Interface

- [ ] Interface gráfica
- [ ] Gerenciamento de jogos
- [ ] Histórico de backups
- [ ] Configurações

### Futuro

- [ ] Backup por intervalo de tempo
- [ ] Detecção automática de jogos
- [ ] Suporte a outras plataformas
- [ ] Integração com outras fontes de saves

## Objetivo acadêmico

O projeto será desenvolvido como trabalho individual de **Engenharia de Software**, aplicando conceitos de:

- levantamento de requisitos;
- casos de uso;
- arquitetura de software;
- modularização;
- persistência de dados;
- testes;
- controle de versão;
- documentação;
- manutenção e evolução de software.

## Status

**Em desenvolvimento — planejamento do MVP**

## Licença

A definir.
