# Django CRUD com Autenticação de Usuários

Este projeto é uma aplicação simples em Django que implementa um sistema de CRUD para livros com autenticação de usuários. O projeto permite que os usuários façam login, logout, cadastrem novos usuários, adicionem, editem e excluam livros, além de explorar os recursos disponíveis.

## Funcionalidades

- **Autenticação de usuários:**
  - Login e logout.
  - Cadastro de novos usuários.

- **Gerenciamento de livros:**
  - Listagem de livros.
  - Adicionar novos livros.
  - Editar informações dos livros.
  - Excluir livros.

- **Controle de acesso:**
  - Apenas usuários autenticados podem adicionar, editar ou excluir livros.

## Estrutura dos Arquivos

### Views

- **`home`**: Página inicial que lista todos os livros. Também permite login diretamente.
- **`sobre`**: Página com informações sobre o sistema.
- **`logout_user`**: Efetua o logout do usuário.
- **`create_user`**: Página de cadastro de novos usuários.
- **`deleteBook`**: Exclui um livro com base no ID fornecido (disponível apenas para usuários autenticados).
- **`create_book`**: Adiciona novos livros ao sistema (disponível apenas para usuários autenticados).
- **`update_book`**: Atualiza informações de um livro existente (disponível apenas para usuários autenticados).

### Modelos e Formulários

- **Modelos:** O modelo `Book` representa os livros no sistema.
- **Formulários:**
  - `SingUpForm`: Formulário para registro de usuários.
  - `AddBookForm`: Formulário para adição e edição de livros.

## Pré-requisitos

- Python 3.8+
- Django 4.2+
- Banco de dados configurado (SQLite padrão ou outro suportado pelo Django).

## Configuração e Instalação

1. **Clone o repositório:**
   ```bash
   git clone <URL-do-repositorio>
   cd <nome-do-projeto>
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Realize as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

5. **Acesse o sistema:**
   Abra o navegador e vá para `http://127.0.0.1:8000/`.

## Tecnologias Utilizadas

- **Framework:** Django
- **Frontend:** HTML, CSS (personalizável)
- **Banco de Dados:** SQLite (padrão, pode ser alterado)

## Como Contribuir

1. Faça um fork do projeto.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'Minha nova feature'`
4. Envie para o repositório: `git push origin minha-feature`
5. Crie um Pull Request.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

## Observações

- Certifique-se de que o ambiente está configurado corretamente antes de iniciar.
- Adapte os templates (`.html`) para atender ao design desejado.
- As mensagens exibidas estão em português; podem ser traduzidas conforme necessário.
