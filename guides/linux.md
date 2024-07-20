# Introdução

No campo de MLOps (Machine Learning Operations), o conhecimento dos comandos do terminal Linux é essencial para a eficiência e automação dos processos de desenvolvimento e implementação de modelos de aprendizado de máquina. O terminal oferece um controle direto e poderoso sobre o sistema operacional, permitindo a execução de tarefas complexas com rapidez e precisão. Profissionais de MLOps frequentemente utilizam comandos do terminal para manipular arquivos, gerenciar permissões, automatizar pipelines de treinamento e implantação, monitorar recursos do sistema e muito mais. Seja configurando um ambiente de desenvolvimento, manipulando grandes volumes de dados ou integrando soluções de CI/CD, a proficiência no terminal Linux capacita os engenheiros de machine learning a otimizar suas operações e garantir que os modelos sejam implementados de maneira confiável e escalável.

## Atalhos úteis
* `CTRL` + `ALT` + `T`: atalho para abrir o terminal
* `SHIFT` + `CTRL` + `C`: copia informações do terminal
* `SHIFT` + `CTRL` + `V`: cola informações no terminal
* `CTRL` + `C`: força a interrupção da execução no terminal
* `CTRL` + `L`: atalho para limpar o terminal
* `TAB`: autocompleta o nome do diretório
* `UP`/`DOWN`: navega pelo histórico de comandos digitados

## Gerenciamento de usuários e permissões

Retorna o nome do usuário atual.
```bash
whoami
```

Troca para o usuário `root` (admin).
```bash
sudo su
```

Sai do modo `root`.
```bash
exit
```

Limpa a tela do terminal.
```bash
clear
```

Dá permissões de `root` para o que vem a seguir (só é necessário em tarefas administrativas).
```bash
sudo <comando>
```

## Listagem e navegação de diretórios

Lista os arquivos de um diretório.
```bash
ls
```

Lista os arquivos e a estrutura de permissões.
```bash
ls -l
```

Lista todos os arquivos ocultos.
```bash
ls -A
```

Mostra o caminho completo do diretório atual.
```bash
pwd
```

Vai para o diretório especificado.
```bash
cd <nome-diretorio>
```

Vai para o diretório `home`.
```bash
cd ~
```

Volta para o diretório anterior (pai).
```bash
cd ..
```

Uso de aspas simples para acessar diretórios com nomes compostos separados por espaços.
```bash
cd '<nome do diretorio>'
```

## Criação e remoção de arquivos e diretórios

Cria o diretório com o nome especificado.
```bash
mkdir <nome-diretorio>
```

Uso de aspas simples para criar diretórios com nomes compostos separados por espaços.
```bash
mkdir '<nome do diretorio>'
```

Remove o diretório com o nome especificado (remove somente diretórios vazios).
```bash
rmdir <nome-diretorio>
```

Cria o arquivo com o nome especificado.
```bash
touch <nome-arquivo>
```

Remove o diretório recursivamente (remove todos os arquivos que estão dentro).
```bash
rm -r <nome-diretorio>
```

Remove o arquivo com o nome especificado.
```bash
rm <nome-arquivo>
```

## Manipulação de arquivos

Copia o arquivo especificado para o diretório especificado.
```bash
cp <nome-arquivo> <nome-diretorio>
```

Copia todos os arquivos com a extensão especificada do diretório atual para o diretório especificado.
```bash
cp *.<extensão> <nome-diretorio>
```

Copia todo o conteúdo do diretório atual para o diretório especificado.
```bash
cp ** <nome-diretorio>
```

Renomeia o arquivo especificado.
```bash
mv <nome-antigo-arquivo> <nome-novo-arquivo>
```

Move o arquivo especificado para o diretório especificado.
```bash
mv <nome-arquivo> <nome-diretorio>
```

Move todos os arquivos com a extensão especificada do diretório atual para o diretório especificado.
```bash
mv *.<extensão> <nome-diretorio>
```

Move todo o conteúdo do diretório atual para o diretório especificado.
```bash
mv ** <nome-diretorio>
```

## Edição de arquivos com vi

Mostra o que está escrito no arquivo.
```bash
cat <nome-arquivo>
```

Adiciona um texto no arquivo sobrescrevendo caso já exista algo.
```bash
echo <texto> > <nome-arquivo>
```

Adiciona um texto no arquivo acrescentando na próxima linha caso já exista algo.
```bash
echo <texto> >> <nome-arquivo>
```

Abre o editor de arquivo `vi` (já instalado por padrão).
```bash
vi
```
Abre o arquivo especificado com o editor de arquivo `vi`.
```bash
vi <nome-arquivo>
```

Com o `vi` aberto, pressione `I` para ativar o modo de edição.

Pressione `ESC` para sair do modo de edição.

Digite `:w <nome-arquivo>` para salvar o conteúdo escrito com o nome especificado.

Digite `:w` salvar as alterações no arquivo com o nome atribuído anteriormente.

Digite `:q` para fechar o editor.

Digite `:q!` para fechar o editor sem salvar as alterações.

Digite `:x` para salvar as alterações e fecha o editor.

Pressione `A` para posicionar o cursor ao final da última linha existente no arquivo.

Pressione `O` para inserir uma linha abaixo da linha atual.

Digite `yy` para copiar o conteúdo da linha aonde o cursor está.

Digite `p` para colar o conteúdo copiado.

Digite `dd` para recortar o conteúdo da linha aonde o cursor está.

Digite `:/<conteudo>` para localizar e posicionar o cursor na primeira ocorrência do conteúdo especificado.

Digite `:s/<conteudo-antigo>/<conteudo-novo>` para localizar e substituir a primeira ocorrência do conteúdo especificado pelo novo conteúdo.

## Edição de arquivos com nano

Abre o arquivo especificado com o editor de arquivo `nano` (caso já esteja instalado).
```bash
nano <nome-arquivo>
```

No `nano`, pressione `CTRL` + `U` para colar o texto cortado ou copiado.

Pressione `ALT` + `6` para copiar o conteúdo da linha selecionada.

Pressione `CTRL` + `K` para recortar o conteúdo selecionado.

Pressione `CTRL` + `O` para salvar as alterações.

Pressione `CTRL` + `X` para fechar o editor.


## Obtenção de informações sobre arquivos

Mostra número de linhas, número de palavras e número de caracteres do arquivo.
```bash
wc <nome-arquivo>
```

Mostra somente as linhas com conteúdos únicos.
```bash
uniq <nome-arquivo>
```

Mostra todas as ocorrências de linhas com conteúdos duplicados.
```bash
uniq -D <nome-arquivo>
```

Mostra a quantidade de ocorrências de cada conteúdo.
```bash
uniq -c
```

Mostra o conteúdo do arquivo em ordem alfabética.
```bash
sort <nome-arquivo>
```

Retorna os **n** primeiros caracteres do arquivo especificado.
```bash
head -c n <nome=arquivo>
```

Retorna os **n** últimos caracteres do arquivo especificado.
```bash
tail -c n <nome=arquivo>
```

Retorna as **n** primeiras linhas do arquivo especificado.
```bash
head -n n <nome=arquivo>
```

Retorna os **n** últimos caracteres do arquivo especificado.
```bash
tail -n n <nome=arquivo>
```

## Compactação e descompactação de arquivos

Cria um diretório compactado a partir de um diretório existente.
```bash
zip -r <nome-diretorio>.zip <nome-diretorio>
```

Verifica o conteúdo do diretório compactado.
```bash
less <nome-diretorio>.zip
```

Descompacta o diretório especificado.
```bash
unzip <nome-diretorio>.zip
```

Descompacta o diretório especificado de forma silenciosa (sem logs).
```bash
unzip -q <nome-diretorio>.zip
```

Cria um diretório compactado usando o `tar` (create zip file).
```bash
tar -czf <nome-diretorio>.tar.gz <nome-diretorio>
```

Descompacta um diretório compactado usando o `tar` (extract zip file).
```bash
tar -xzf <nome-diretorio>.tar.gz
```

## Criação e execução de scripts

Criando um arquivo de script.
```bash
nano
```

Dentro do `nano`, escreva o conteúdo do script.
```bash
cp /home/user/logs/*.txt /home/user/backup
```

Para salvar o arquivo criado como um script exectável, salve com a extensão `.sh`. Para isso, pressione `CTRL` + `O` e digite, por exemplo, `script.sh`.

Antes de executar o script, é necessário alterar as permissões de usuário. Para isso, é utilizado o `chmod` (change mode) acompanhado das flags `+` (para adicionar permissões) e `x` (permissão de execução).
```bash
chmod +x script.sh
```

Executa o script criado.
```bash
./script.sh
```

Alternativamente também é possível utilizar o comando `bash`.
```bash
bash script.sh
```

## Criação de variáveis de ambiente

Consulta o valor armazenado em uma variável de ambiente.
```bash
echo $<nome-variavel>
```

Consulta todas as variáveis de ambiente existentes e seus respectivos valores.
```bash
printenv
```

Cria e atribui um valor a um nova variável de ambiente.
```bash
export <nome-variavel>=<valor>
```

Possibilita que um script criado possa ser executado estando em qualquer diretório.
```bash
export PATH=$PATH:<diretorio-script>
```

Assim, o script pode ser executado sem nenhum comando antes e em qualquer diretório.
```bash
script.sh
```

## Instalação de pacotes

A instalação de pacotes é feita utilizando o `apt` (Advanced Packaging Tool).

Mostra a lista de repositórios que podem ser atualizados.
```bash
apt list --upgradable
```

Mostra se um pacote está instalado e em qual versão.
```bash
apt list <nome-pacote>
```

Busca nas descrições do pacote.
```bash
apt search <nome-pacote>
```

Mostra informações detalhadas do pacote.
```bash
apt show <nome-pacote>
```

Mostra as dependências do pacote.
```bash
apt-cache depends <nome-pacote>
```

Atualiza a lista de repositórios do sistema.
```bash
sudo apt update
```

Instala novos pacotes e atualiza os existentes.
```bash
sudo apt upgrade
```

Remove, instala e atualiza pacotes.
```bash
sudo apt full-upgrade
```

Instala o pacote especificado.
```bash
sudo apt install <nome-pacote>
```

Remove o pacote especificado.
```bash
sudo apt remove <nome-pacote>
```

Instala pacotes a partir de um arquivo `.deb`.
```bash
sudo dpkg -i <nome-arquivo>.deb
```

## Outros comandos úteis

Mostra o manual do comando.
```bash
man <nome-comando>
```

Mostra o menu de ajuda do comando.
```bash
<nome-comando> --help
```

Completa o espaço seguinte com a informação do comando anterior.
```bash
<comando> !!
```

Completa o espaço anterior com a informação do comando anterior.
```bash
!! <comando>
```