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

<img src="../assets/git-workflow.jpeg" width="712" height="584"/>

**Fonte:** [https://docs.ionos.space/blog/git-intro/#the-git-workflow](https://docs.ionos.space/blog/git-intro/#the-git-workflow)

## Comandos e operações do Git

Cada estágio do fluxo de trabalho do Git está associado a um conjunto de operações específicas.

### No Working Directory

Para verificar quais arquivos foram alterados.
```bash
git status
```

Para ver as diferenças específicas nas modificações dos arquivos.
```bash
git diff
```

### Na Staging Area

Para adicionar arquivos específicos à staging area.
```bash
git add <nome-arquivo>
```

Para adicionar todas as mudanças ao próximo commit.
```bash
git add .
```

Para ver as diferenças existentes nos arquivos contidos na staging area.
```bash
git diff --stagged
```

Para remover arquivos da staging area mantendo o conteúdo.
```bash
git reset <nome-arquivo>
```

Para restaurar versões de arquivos que estão na staging area.
```bash
git restore <nome-arquivo>
```

Para remover um arquivo e evitar que ele seja rastreado.
```bash
git rm <nome-arquivo>
```

Para remover um diretório inteiro e evitar que ele seja rastreado.
```bash
git rm -r <nome-diretorio>
```

Para manter o arquivo no repositório mas evitar o rastreio.
```bash
git rm --cached <nome-arquivo>
```

Para manter o diretório completo no repositório mas evitar o rastreio.
```bash
git rm --cached -r <nome-arquivo>
```

### No Local Repository

Para criar um novo commit com uma mensagem descritiva.
```bash
git commit -m "mensagem de commit"
```

Para criar o commit e já enviar os arquivos para a staging area.
```bash
git commit -a -m "mensagem de commit"
```

Para ajustar o último commit sem criar um novo.
```bash
git commit --amend -m "nova mensagem de commit"
```

Para criar um novo commit que desfaz as alterações do commit especificado.
```bash
git revert <hash-commit>
```

Para visualizar o histórico de commits.
```bash
git log
```

Para visualizar as branches existentes.
```bash
git branch
```

Para criar uma nova branch.
```bash
git branch <nome-branch>
```

Para remover uma branch local.
```bash
git branch -D <nome-branch>
```

Para mudar de branch.
```bash
git checkout <nome-branch>
```

Para criar e mudar para um nova branch.
```bash
git checkout -b <nome-branch>
```

Para descartar as alterações no diretório de trabalho.
```bash
git checkout -- <nome-arquivo>
```

### No Central Repository (Remote)

Para conectar o repositório local a um repositório remoto (a autenticação pode ser necessária em alguns casos).
```bash
git remote add origin <url-repositorio-remoto>
```

**OBS:** Este passo não é necessário quando o repositório remoto foi clonado em um repositório local.

Para enviar commits do repositório local para o repositório remoto.
```bash
git push -u origin <nome-branch>
```

**OBS:** A flag `-u` configura a branch local `<branch>` para reastrear a branch remota `<branch>` no repositório remoto. Depois que essa configuração é feita uma vez não é necessário realizar novamente.

Para atualizar o repositório local com a versão mais recente do repositório remoto.
```bash
git pull origin <nome-branch>
```

Para remover uma branch remota.
```bash
git push origin --delete <nome-branch>
```

Para remover um repositório remoto.
```bash
git remote remove origin
```

Para baixar somente as novas referências (commits, branches, tags) do repositório remoto sem integrá-las ao seu código local.
```bash
git fetch origin
```

Para mesclar as alterações de uma outra branch com a branch atual.
```bash
git merge <nome-outra-branch>
```

**OBS:** Em caso de conflitos de versões, é possível resolvê-las diretamente nos editores de código, como o Visual Studio Code.