# Lista de Tarefas - Backend API

API REST desenvolvida com Django REST Framework para gerenciamento de tarefas com autenticação JWT.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+** - Linguagem de programação
- **Django 5.0.7** - Framework web robusto e escalável
- **Django REST Framework** - Toolkit para criação de APIs REST
- **djangorestframework-simplejwt** - Autenticação JWT para Django REST
- **django-cors-headers** - Gerenciamento de CORS para requests cross-origin
- **SQLite** - Banco de dados para desenvolvimento (fácil configuração)

## 📁 Estrutura do Projeto

```bash
lista-de-tarefas-backend/
├── core/                         # Configurações principais do Django
│   ├── __init__.py
│   ├── settings.py              # Configurações do projeto
│   ├── urls.py                  # URLs principais
│   ├── wsgi.py                  # WSGI para deploy
│   └── asgi.py                  # ASGI para deploy
├── users/                       # App de usuários personalizados
│   ├── models.py                # Modelo User personalizado
│   ├── serializers.py           # Serializers para autenticação
│   ├── views.py                 # Views de registro, login, logout
│   ├── urls.py                  # URLs do app users
│   └── admin.py                 # Configuração do Django Admin
├── tasks/                       # App de gerenciamento de tarefas
│   ├── models.py                # Modelo Task
│   ├── serializers.py           # Serializers para CRUD de tarefas
│   ├── views.py                 # ViewSet para operações CRUD
│   ├── urls.py                  # URLs do app tasks
│   └── admin.py                 # Configuração do Django Admin
├── db.sqlite3                   # Banco de dados SQLite
├── manage.py                    # Utilitário de linha de comando Django
└── requirements.txt             # Dependências Python
```

## ✨ Funcionalidades da API

### 🔐 Autenticação JWT

- **Registro de usuários** com validação completa
- **Login** com retorno de tokens JWT (access + refresh)
- **Logout** com blacklist de tokens
- **Refresh de tokens** automático
- **Perfil do usuário** logado

### 📝 Gerenciamento de Tarefas

- **CRUD completo** de tarefas
- **Filtragem automática** por usuário autenticado
- **Validações** de dados no backend
- **Permissões** - usuários só acessam suas próprias tarefas

## 📡 Endpoints da API

### Autenticação

```bash
POST /api/auth/register/          # Registro de novo usuário
POST /api/auth/login/             # Login (retorna access + refresh tokens)
POST /api/auth/logout/            # Logout (adiciona token ao blacklist)
GET  /api/auth/profile/           # Dados do usuário logado
POST /api/auth/token/refresh/     # Refresh do access token
```

### Tarefas

```bash
GET    /api/tasks/                # Listar todas as tarefas do usuário
POST   /api/tasks/                # Criar nova tarefa
GET    /api/tasks/{id}/           # Detalhes de uma tarefa específica
PUT    /api/tasks/{id}/           # Atualizar tarefa completa
PATCH  /api/tasks/{id}/           # Atualizar tarefa parcialmente
DELETE /api/tasks/{id}/           # Excluir tarefa
```

## 🛠️ Como Rodar Localmente

### Pré-requisitos

- **Python 3.12+** instalado
- **pip** (gerenciador de pacotes Python)
- **Git** (opcional, para clonar o repositório)

### 📦 Instalação e Configuração

1. **Clone o repositório** (se ainda não tiver):

   ```bash
   git clone <url-do-repositorio>
   cd lista-de-tarefas-backend
   ```

2. **Crie um ambiente virtual Python**:

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados**:

   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário** (opcional, para acessar o admin):

   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver
   ```

7. **Verifique se está funcionando**:

   - API Base: `http://127.0.0.1:8000/api/`
   - Django Admin: `http://127.0.0.1:8000/admin/`
   - Documentação da API: `http://127.0.0.1:8000/api/` (se configurada, ainda não é o caso)

### 🧪 Testando a API

Você pode testar os endpoints usando **curl**, **Postman** ou **Insomnia**:

```bash
# Registro de usuário
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "João Silva",
    "email": "joao@exemplo.com", 
    "password": "MinhaSenh@123",
    "password_confirm": "MinhaSenh@123"
  }'

# Login
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "joao@exemplo.com",
    "password": "MinhaSenh@123"
  }'

# Listar tarefas (necessário token JWT)
curl -X GET http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Bearer SEU_ACCESS_TOKEN_AQUI"
```

## ⚙️ Configurações Importantes

### CORS

Configurado para aceitar requests de:

- `http://localhost:5173` (Vite dev server)
- `http://127.0.0.1:5173`
- `http://localhost:3000` (Create React App)
- `http://127.0.0.1:3000`

### JWT Tokens

- **Access Token**: 60 minutos de duração
- **Refresh Token**: 7 dias de duração
- **Rotação de tokens**: Habilitada
- **Blacklist**: Habilitada para logout seguro

### Banco de Dados

- **Desenvolvimento**: SQLite (arquivo `db.sqlite3`)
- **Produção**: Configurar PostgreSQL ou MySQL nas variáveis de ambiente

## 🔒 Segurança

- **Validação de senhas** com critérios do Django
- **Criptografia de senhas** com algoritmo PBKDF2
- **Validação de entrada** em todos os endpoints
- **Autenticação obrigatória** para endpoints de tarefas
- **Filtragem automática** - usuários só veem suas tarefas

## 🚀 Deploy para Produção

### Variáveis de Ambiente

```bash
DEBUG=False
SECRET_KEY=sua-chave-secreta-super-segura
DATABASE_URL=postgresql://user:pass@host:port/dbname
ALLOWED_HOSTS=seudominio.com,www.seudominio.com
CORS_ALLOWED_ORIGINS=https://seudominio.com
```

### Comandos de Deploy

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput  # se usando variáveis de ambiente
```

## 🛠️ Comandos Úteis

```bash
# Criar migrações após mudanças nos models
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Acessar shell do Django
python manage.py shell

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos (produção)
python manage.py collectstatic

# Verificar configuração do projeto
python manage.py check
```

## 📝 Modelos de Dados

### User (Usuário)

```python
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@exemplo.com",
  "created_at": "2025-06-28T10:00:00Z",
  "updated_at": "2025-06-28T10:00:00Z"
}
```

### Task (Tarefa)

```python
{
  "id": 1,
  "title": "Finalizar projeto",
  "description": "Implementar últimas funcionalidades",
  "completed": false,
  "user": "João Silva (joao@exemplo.com)",
  "created_at": "2025-06-28T10:00:00Z",
  "updated_at": "2025-06-28T10:00:00Z"
}
```

---

## **API desenvolvida com ❤️ usando Django REST Framework | Documentação criada por Copilot**
