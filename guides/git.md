# Introdução

No contexto de MLOps, o Git desempenha um papel crucial na gestão de código-fonte e controle de versões. Ele permite que os engenheiros de machine learning colaborem de forma eficiente, rastreiem mudanças no código, e revertam para versões anteriores quando necessário. O Git é essencial para a implementação de práticas de CI/CD, garantindo que novos modelos e atualizações de código sejam testados e integrados continuamente. Além disso, ele facilita a colaboração em equipes distribuídas, permitindo que múltiplos desenvolvedores trabalhem simultaneamente em diferentes partes de um projeto sem conflitos. Conhecer os comandos e fluxos de trabalho do Git é fundamental para manter a organização e integridade dos projetos de machine learning em produção.

## Instalação do Git

No Windows, basta acessar o [link](https://git-scm.com/downloads) para baixar o arquivo de instalação.

No Linux, basta acessar o [link](https://git-scm.com/download/linux) e seguir o tutorial correspondente a distribuição que você utiliza.

## Configuração inicial

O primeiro passo após a instalação do Git, é realizar a configuração de usuário e, para isso, basta fornecer um nome de usuário e um endereço de e-mail válido.

```bash
git config --global user.name "Seu Nome"
git config --global user.email seuemail@exemplo.br
```

**OBS:** A flag `--global` garante que você precise realizar essa configuração uma única vez pois ela irá valer para qualquer ação que for feita no sistema em que foi instalado.

O comando abaixo lista todas as configurações realizadas no sistema.

```bash
git config --global --list
```

## Conceitos básicos

A seguir estão listados alguns dos conceitos mais importantes para compreender 

* **Repositório Git:** Um repositório contém todos os arquivos do seu projeto e o histórico de suas revisões.
* **Commit:** Um commit é uma gravação de mudanças no repositório. Cada commit tem uma mensagem associada que descreve o que foi alterado.
* **Branch:** Uma branch é uma versão separada do repositório, usada para desenvolver funcionalidades isoladamente.
* **Merge:** Unir mudanças de diferentes branches ao branch principal.

## Criação de um repositório do zero

Para criar um repositório Git local, é necessário escolher um diretório de trabalho existente ou criar um novo. Após isso, basta acessá-lo no terminal e inserir o comando abaixo para inicializar o repositório Git local.

```bash
git init
```

Caso o diretório que você deseja trabalhar já exista em um repositório remoto (no GitHub, por exemplo), é possível clonar toda a sua estrutura e trazer para dentro do seu diretório local.

```bash
git clone https://github.com/usuario/repositorio.git
```

## Fluxo de trabalho do Git

Antes de começar a realizar o gerenciamento de versão com Git, é importante compreender como funciona o fluxo de trabalho da ferramenta. A figura abaixo mostra que existem 4 estágios principais:
* **Working Directory:** É onde os arquivos são editados e modificados. Representa o seu ambiente local de trabalho.
* **Staging Area:** Uma camada intermediária entre o diretório de trabalho e o histórico de commits. Aqui, você decide quais mudanças serão incluídas no próximo commit.
* **Local Repository:** Contém todos os seus commits, permitindo que você mantenha um histórico das alterações e reverta para estados anteriores do código se necessário.
* **Central Repository:** Versão do seu repositório que está hospedada em um servidor remoto, como GitHub, GitLab ou Bitbucket. É utilizado para compartilhar o código com outros colaboradores e armazenar o progresso de forma segura.

<img src="../img/git-workflow.jpeg" width="712" height="584"/>

**Fonte:** [https://docs.ionos.space/blog/git-intro/#the-git-workflow](https://docs.ionos.space/blog/git-intro/#the-git-workflow)

## Comandos e Operações do Git

Cada estágio do fluxo de trabalho do Git está associado a um conjunto de operações específicas:

### No Working Directory

Para verificar quais arquivos foram alterados.

```bash
git status
```

Para ver as diferenças específicas nas modificações dos arquivos

```bash
git diff
```

### Na Staging Area

Para adicionar arquivos específicos à staging area.

```bash
git add <arquivo>
```

Para adicionar todas as mudanças ao próximo commit.

```bash
git add .
```

Para remover arquivos da staging area se necessário.

```bash
git reset <arquivo>
```

### No Local Repository

Para criar um novo commit com uma mensagem descritiva.

```bash
git commit -m "mensagem de commit"
```

Para visualizar o histórico de commits.

```bash
git log
```

Para mudar de branch.

```bash
git checkout <nome_da_branch>
```

Para criar e mudar para um nova branch.

```bash
git checkout -b <nome_da_branch>
```

### No Central Repository

Para conectar o repositório local a um repositório remoto.

```bash
git remote add origin <url_do_repositorio_remoto>
```

**OBS:** Este passo não é necessário quando o repositório remoto foi clonado em um repositório local.

Para enviar commits do repositório local para o repositório central.

```bash
git push -u origin <nome_da_branch>
```

Para atualizar o repositório local com a versão mais recente do repositório central.

```bash
git pull origin <nome_da_branch>
```



