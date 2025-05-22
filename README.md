# Raciocínio Algorítmico - Projeto com Git e GitHub
Este repositório foi criado com o objetivo de praticar o uso de Git e GitHub no controle de versões e desenvolvimento colaborativo.

### 1. Instalação do Git
- Acesse: [https://git-scm.com/](https://git-scm.com/)
- Baixe e instale a versão compatível com seu sistema operacional.
- Após a instalação, verifique se está tudo certo executando:
```bash
git --version
```

### 2. Configuração Inicial
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

### 3. Criação do Repositório no GitHub
- Vá até [https://github.com](https://github.com)
- Clique em **"New"** para criar um novo repositório
- Preencha com:
  - Nome: `RaciocinioAlgoritmico`
  - Descrição (opcional)
  - Marque a opção **"Add a README file"**
- Clique em **"Create repository"**

### 4. Clonando o Repositório
```bash
git clone https://github.com/matheusalievi/RaciocnioAlgortmico.git
```

### 5. Trabalhando com o Projeto
Acesse a pasta do projeto e crie/edite seus arquivos:
```bash
cd RaciocnioAlgortmico
# edite arquivos, adicione código etc.
```

### 6. Salvando Alterações com Git
Adicione as mudanças e faça um commit:
```bash
git add .
git commit -m "Descrição das alterações"
```

### 7. Enviando para o GitHub (Push)
```bash
git push origin main
```

### 8. Trabalhando com Branches
Para desenvolver uma nova funcionalidade sem afetar o código principal:
```bash
git checkout -b nova-feature
# faça alterações, commits e push
git push origin nova-feature
```

### 9. Criando um Pull Request
- Vá até o repositório no GitHub
- Clique em **"Pull Requests" > "New Pull Request"**
- Escolha a branch `nova-feature` e compare com `main`
- Escreva um título e comentário explicando as mudanças
- Clique em **"Create Pull Request"**
- Após revisão, clique em **"Merge"** para juntar ao projeto principal

---


##Autor
Matheus Alievi de Paula
