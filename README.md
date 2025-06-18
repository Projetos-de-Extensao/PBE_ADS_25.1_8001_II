# Ilha Primeira G2

**Número do Grupo**: 02<br>
**Código da Disciplina**: FGA0208-T01<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 202208385087  | Gabriel Perrota |
| 202301165784  | Guilherme Maranhão |
| 202302174264  | Pedro Caravellos |
| 202307539741  | Thiago Neves |

## Sobre 
Nosso objetivo é desenvolver um aplicativo voltado para os moradores da Ilha Primeira, proporcionando uma ferramenta eficiente para o preenchimento do censo demográfico da região. Acreditamos que, ao coletar e organizar essas informações de forma estruturada, será possível dar maior visibilidade aos desafios enfrentados pela comunidade, especialmente no que diz respeito à infraestrutura e às necessidades básicas da população.

Com esses dados, pretendemos não apenas evidenciar as carências da ilha, mas também fomentar iniciativas e soluções que possam contribuir para a melhoria da qualidade de vida dos moradores, promovendo mudanças significativas e duradouras. 

## Screenshots
<img src="https://github.com/Projetos-de-Extensao/PBE_ADS_25.1_8001_II/blob/main/docs/Ilha_primeira.jpeg" width="200"/>

## Tecnologias e Linguagens 
**Python + Django:** O backend da aplicação foi desenvolvido com Django, framework web robusto baseado em Python, que fornece ORM nativo, segurança, sistema de administração e excelente integração com bancos relacionais.

**MkDocs:** Ferramenta utilizada para a documentação do projeto, permitindo uma apresentação clara, navegável e responsiva do conteúdo.

**PlantUML:** Usado para geração de diagramas de classes com base nos modelos definidos no Django, facilitando o entendimento da estrutura de dados.

**Git + GitHub:** Para controle de versão, rastreamento de alterações e colaboração entre os membros da equipe.

**SQLite:** Para armazenamento local dos dados durante o desenvolvimento e testes.

## Uso 
Preenchimento e exportação de dados por meio de um formulário digital

## Tutorial de instalação das ferramentas

1. Clonar o Repositório
Abra o terminal e execute:

```bash
git clone https://github.com/Projetos-de-Extensao/PBE_ADS_25.1_8001_II
```
```bash
cd src 
```

2. Criar e Ativar o Ambiente Virtual
bash

```bash
python -m venv venv
```

3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

4. Aplicar as Migrações
bash

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

5. Criar um Superusuário (opcional, para acesso ao painel admin)

```bash
python manage.py createsuperuser
```

6. Executar o Servidor

```bash
python manage.py runserver
```
Acesse o projeto no navegador:
http://127.0.0.1:8000

7. Acessar o Painel de Administração
http://127.0.0.1:8000/admin/

8. Documentação Interativa (Swagger)
Se configurado corretamente, a documentação da API estará disponível em:
http://127.0.0.1:8000/swagger/
