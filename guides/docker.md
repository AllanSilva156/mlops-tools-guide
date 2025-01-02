# Introdução

O Docker é uma ferramenta indispensável em MLOps por sua capacidade de criar ambientes isolados e reproduzíveis para desenvolvimento, teste e produção de modelos de aprendizado de máquina. Com Docker, os engenheiros podem empacotar aplicações e suas dependências em contêineres, garantindo que os modelos funcionem de forma consistente em qualquer ambiente. Isso é particularmente importante ao mover modelos entre diferentes fases do pipeline de MLOps, desde o desenvolvimento local até a produção em escala. Docker também facilita o escalonamento de aplicações, permitindo a implantação rápida e eficiente de múltiplos contêineres em ambientes de nuvem ou on-premises.

## Instalação do Docker

No Windows, basta acessar o [link](https://www.docker.com/products/docker-desktop/) para baixar o Docker Desktop. Após o download, execute o instalador e siga as instruções na tela. Certifique-se de que a virtualização está habilitada no BIOS do seu computador, pois isso é necessário para o funcionamento do Docker.

No Linux, você pode acessar o [link](https://docs.docker.com/engine/install/) e seguir o tutorial correspondente à distribuição que você utiliza, como Ubuntu, CentOS ou Fedora. Geralmente, a instalação envolve os seguintes passos:

1. Atualizar os pacotes do sistema:
```bash
sudo apt update && sudo apt upgrade -y
```

2. Instalar dependências necessárias:
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

3. Adicionar a chave GPG oficial do Docker:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

4. Adicionar o repositório Docker:
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

5. Instalar o Docker:
```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```

6. Verificar a instalação:
```bash
docker --version
```

Certifique-se de adicionar seu usuário ao grupo Docker para evitar usar `sudo` em cada comando:
```bash
sudo usermod -aG docker $USER
```

Após isso, reinicie sua sessão ou o sistema para que as mudanças tenham efeito.

No macOS, você pode acessar o [link](https://www.docker.com/products/docker-desktop/) para baixar o Docker Desktop. Assim como no Windows, basta executar o instalador e seguir as instruções na tela.

## Comandos Docker

1. Realizar o download de uma imagem específica:

```bash
docker image pull nome_da_imagem
```

2. Verifica todas as imagens que foram baixadas:

```bash
docker images
``` 

3. Cria o contêiner de uma imagem específica:

```bash
docker container create -i -t --name nome_do_container nome_da_imagem
```

4. Lista todos os contêineres existentes:

```bash
docker container ls -a
```

5. Inicia o contêiner criado:

```bash
docker container start -i -a nome_do_conteiner
```

6. Encerra a execução de um contêiner:

```bash
docker container stop nome_do_conteiner
```

7. Exclui um contêiner:

```bash
docker container rm nome_do_conteiner
``` 

8. Realiza os passos 1, 3 e 5 de uma vez só:

```bash
docker run -ti --name nome_do_conteiner nome_da_imagem /bin/bash
``` 

9. Executa um contêiner e, em seguida, remove ele

```bash
docker run -ti --rm --name nome_do_conteiner nome_da_imagem /bin/bash
``` 

10. Executa um contêiner em segundo plano (em outro terminal):

```bash
docker run -d -ti --name nome_do_conteiner nome_da_imagem /bin/bash
``` 

11. Vincular novamente a execução do contêiner ao terminal principal:

```bash
docker attach nome_do_conteiner
```

12. Copia um volume (conjunto de dados) de um diretório da máquina host (/home/user/dados) para um diretório do contêiner (/home/container/dados):

```bash
docker run -ti -v /home/user/dados:/home/container/dados --name nome_do_conteiner nome_da_imagem /bin/bash
```

13. Sobe um servidor da porta 80 da máquina host para a porta 8080 do contêiner:

```bash
docker run -ti --rm -p 8080:80 nome_da_imagem
``` 

14. Limita o uso de memória de um contêiner (500 MB no exemplo):

```bash
docker run -ti -m 500M --name nome_do_conteiner nome_da_imagem /bin/bash
``` 

15. Limita o uso de CPU de um contêiner (2 cores no exemplo):

```bash
docker run -ti -c 2 --name nome_do_conteiner nome_da_imagem /bin/bash
``` 

16. Constrói uma imagem de acordo com o que foi especificado no Dockerfile existente no diretório ./

```bash
docker build --name nome_da_imagem ./
``` 

17. Realiza o commit (Docker Hub) de alguma modificação em uma imagem existente:

```bash
docker commit nome_da_imagem_original nome_da_imagem_alterada
``` 

18. Salva um arquivo compactado de imagens:

```bash
docker save -o minhas_imagens.zip <imagem_1> <imagem_2> ... <imagem_n>
```  

19. Faz o upload de um arquivo compactado de imagens:

```bash
docker load -i minhas_imagens.zip
```  

20. Exclui uma imagem baixada:

```bash
docker rmi nome_da_imagem
``` 