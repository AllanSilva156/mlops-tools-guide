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
docker container create -i -t --name nome_do_conteiner nome_da_imagem
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
docker run -it --name nome_do_conteiner nome_da_imagem bash
``` 

9. Executa um contêiner e, em seguida, remove ele
```bash
docker run -it --rm --name nome_do_conteiner nome_da_imagem bash
``` 

10. Executa um contêiner em segundo plano (em outro terminal):
```bash
docker run -d -it --name nome_do_conteiner nome_da_imagem bash
``` 

11. Vincular novamente a execução do contêiner ao terminal principal:
```bash
docker attach nome_do_conteiner
```

12. Copia um volume (conjunto de dados) de um diretório da máquina host (/home/user/dados) para um diretório do contêiner (/home/container/dados):
```bash
docker run -it -v /home/user/dados:/home/container/dados --name nome_do_conteiner nome_da_imagem bash
```

13. Sobe um servidor da porta 80 da máquina host para a porta 8080 do contêiner:
```bash
docker run -it --rm -p 8080:80 nome_da_imagem
```

14. Sobe um servidor realizando um mapeamento automático entre a porta da máquina host e a porta do contêiner:
```bash
docker run -it --rm -P nome_da_imagem
``` 

15. Imprime o mapeamento atual de portas do contêiner especificado:
```bash
docker port nome_do_conteiner
```

16. Limita o uso de memória de um contêiner (500 MB no exemplo):
```bash
docker run -it -m 500M --name nome_do_conteiner nome_da_imagem bash
``` 

17. Limita o uso de CPU de um contêiner (2 cores no exemplo):
```bash
docker run -it -c 2 --name nome_do_conteiner nome_da_imagem bash
```

18. Imprime os logs de execução de um determinado contêiner:
```bash
docker logs nome_do_conteiner
```

19. Constrói uma imagem de acordo com o que foi especificado no Dockerfile existente no diretório atual:
```bash
docker build --name nome_da_imagem .
``` 

20. Interrompe e exclui um determinado contêiner em um único passo:
```bash
docker rm -f nome_do_conteiner
```

21. Interrompe a execução de todos os contêineres em uso:
```bash
docker stop $(docker ps -q)
```

22. Interrompe a execução e exclui os contêineres existentes:
```bash
docker rm -f $(docker ps -q)
```

23. Exclui uma imagem baixada:
```bash
docker rmi nome_da_imagem
```

24. Exclui todas as imagens baixadas:
```bash
docker rmi $(docker images -q)
```

25. Remove todos os contêineres parados:
```bash
docker container prune
```

26. Remove todas as imagens não utilizadas, incluindo as que não estão associadas a contêineres parados:
```bash
docker image prune -a
```

27. Realizar o login do Docker Hub:
```bash
docker login -u nome_do_usuario
```

28. Realizar o envio de uma imagem local para o Docker Hub:
```bash
docker push nome_da_imagem
```

29. Realiza o commit de alguma modificação em uma imagem existente para o Docker Hub:
```bash
docker commit nome_da_imagem_original nome_da_imagem_alterada
```

30. Lista todos os volumes disponíveis:
```bash
docker volume ls
``` 

31. Cria um determinado volume:
```bash
docker volume create nome_do_volume
```

32. Associa o volume criado à execução de um determinado contêiner:
```bash
docker run -it -v nome_do_volume:diretorio_do_conteiner --name nome_do_conteiner nome_da_imagem bash
```

33. Lista todas as redes disponíveis:
```bash
docker network ls
```

34. Cria uma determinada rede:
```bash
docker network create --driver bridge nome_da_rede
```

35. Associa a rede criada à execução de um determinado contêiner:
```bash
docker run -it --network nome_da_rede --name nome_do_conteiner nome_da_imagem bash
```

## Utilizando o Docker Compose para coordenar contêineres

No Windows, o Docker Compose já está incluído na instalação do Docker Desktop. Após instalar o Docker Desktop, você pode usar o comando `docker compose` diretamente no terminal.

No Linux, a instalação ocorre através da execução do comando abaixo:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Em seguida, é necessário aplicar permissões de execução (+x) ao binário que acabou de ser baixado.
```bash
sudo chmod +x /usr/local/bin/docker-compose
```

No macOS, o Docker Compose também está incluído na instalação do Docker Desktop. Basta instalar o Docker Desktop e utilizar o comando `docker compose` no terminal.

Se preferir uma instalação manual, use o Homebrew:
```bash
brew install docker-compose
```

Após a instalação, você pode criar um arquivo `docker-compose.yml` para definir e coordenar seus serviços. Por exemplo:

```yaml
version: '3.8'
services:
  app:
    image: nginx
    ports:
      - "8080:80"
```

**OBS:** Os parâmetros possíveis para o arquivo `docker-compose.yml` podem ser consultados na [documentação oficial](https://docs.docker.com/reference/compose-file/)

Para iniciar os serviços definidos no arquivo, execute dentro do diretório no qual está o arquivo `docker-compose.yml`:
```bash
docker-compose up
``` 

Para iniciar os serviços em segundo plano:
```bash
docker-compose up -d
```

Para verificar os serviços em execução:
```bash
docker-compose ps
```

Para interromper e excluir os serviços:
```bash
docker-compose down
```
