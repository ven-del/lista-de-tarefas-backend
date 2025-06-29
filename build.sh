#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Você que tá vendo isso, essa senha é apenas para testes. 
# Em produção, use uma senha mais forte e segura. 
# Este é um ambiente controlado de aprendizado, um laboratório.
# Nunca crie um superuser no script de deploy.
python manage.py shell -c "
from users.models import User
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser(
        email='vendel@labce.com',
        password='SenhaAdmin123!',
        name='Vendel Admin'
    )
    print('✅ Superuser criado com sucesso!')
    print('📧 Email: vendel@labce.com')
    print('🔑 Senha: SenhaAdmin123!')
else:
    print('ℹ️ Superuser já existe no banco.')
"
