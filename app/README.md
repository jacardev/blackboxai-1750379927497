# Gerenciador de Senhas (Password Manager)

Um gerenciador de senhas seguro desenvolvido em Django com interface moderna e criptografia de dados.

## Características

- **Interface Moderna**: Design limpo com cores off-white e terracotta
- **Autenticação Segura**: Sistema de login/logout com proteção de sessão
- **Criptografia**: Senhas são criptografadas antes de serem armazenadas
- **CRUD Completo**: Criar, visualizar, editar e excluir registros de senhas
- **Responsivo**: Interface adaptável para diferentes tamanhos de tela
- **Aplicação Desktop**: Pode ser executada como aplicação desktop usando PyWebView

## Funcionalidades

### Autenticação
- Login seguro com validação de credenciais
- Registro de novos usuários
- Logout com redirecionamento automático

### Gerenciamento de Senhas
- **Adicionar**: Criar novos registros com email, celular, senha e observações
- **Visualizar**: Dashboard com todos os registros salvos (senhas ocultas por segurança)
- **Editar**: Modificar registros existentes
- **Excluir**: Remover registros com confirmação

### Segurança
- Senhas são criptografadas usando a biblioteca `cryptography`
- Proteção CSRF em todos os formulários
- Autenticação obrigatória para acessar funcionalidades
- Senhas nunca são exibidas em texto plano na interface

## Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

1. **Clone o repositório**:
```bash
git clone <repository-url>
cd django_password_manager
```

2. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

3. **Configure o banco de dados**:
```bash
python manage.py migrate
```

4. **Crie um superusuário**:
```bash
python manage.py setup_admin
```
Ou manualmente:
```bash
python manage.py createsuperuser
```

## Como Usar

### Executar como Aplicação Web

1. **Inicie o servidor de desenvolvimento**:
```bash
python manage.py runserver 8000
```

2. **Acesse a aplicação**:
Abra seu navegador e vá para `http://127.0.0.1:8000`

3. **Faça login**:
- Usuário: `admin`
- Senha: `admin123` (se usou o comando setup_admin)

### Executar como Aplicação Desktop

1. **Instale dependências adicionais** (se necessário):
```bash
pip install pywebview
```

2. **Execute a aplicação desktop**:
```bash
python desktop_app.py
```

## Estrutura do Projeto

```
django_password_manager/
├── django_password_manager/          # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── password_manager/                 # App principal
│   ├── templates/                    # Templates HTML
│   │   ├── auth/                     # Templates de autenticação
│   │   └── manager/                  # Templates do gerenciador
│   ├── management/commands/          # Comandos personalizados
│   ├── forms.py                      # Formulários Django
│   ├── models.py                     # Modelos (não usado - dados em JSON)
│   ├── views.py                      # Views/Controllers
│   ├── urls.py                       # URLs do app
│   └── utils.py                      # Utilitários (criptografia)
├── static/css/                       # Arquivos CSS
├── data/                            # Dados criptografados (criado automaticamente)
├── desktop_app.py                   # Launcher para aplicação desktop
├── requirements.txt                 # Dependências Python
└── README.md                        # Este arquivo
```

## Tecnologias Utilizadas

- **Backend**: Django 5.2.3
- **Frontend**: HTML5, CSS3 (design customizado)
- **Criptografia**: Python `cryptography` library
- **Desktop**: PyWebView (opcional)
- **Banco de Dados**: SQLite (para autenticação), JSON criptografado (para senhas)

## Segurança

### Criptografia
- As senhas são criptografadas usando Fernet (criptografia simétrica)
- Chave de criptografia é gerada automaticamente e armazenada de forma segura
- Dados são salvos em formato JSON criptografado

### Autenticação
- Sistema de autenticação do Django
- Proteção CSRF em todos os formulários
- Sessões seguras
- Redirecionamento automático para login se não autenticado

## Personalização

### Cores e Estilo
As cores principais podem ser modificadas no arquivo `static/css/styles.css`:
- `--color-offwhite`: Cor de fundo principal
- `--color-terracotta`: Cor de destaque
- `--color-gray`: Cor do texto

### Funcionalidades
Para adicionar novos campos aos registros de senha, modifique:
1. `password_manager/forms.py` - Adicione campos ao `PasswordEntryForm`
2. Templates em `password_manager/templates/manager/` - Atualize a interface
3. `password_manager/utils.py` - Se necessário, ajuste a criptografia

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Suporte

Para suporte ou dúvidas, abra uma issue no repositório do projeto.
