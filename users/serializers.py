from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'password_confirm']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                'password_confirm': 'As senhas não conferem.'
            })
        return attrs
    
    def validate_email(self, value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError('Este email já está cadastrado.')
        return value.lower()
    
    def create(self, validated_data):
        validated_data.pop('password_confirm', None)
        
        user = User.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            email = email.lower()
            
            user = authenticate(username=email, password=password)
            
            if not user:
                raise serializers.ValidationError('Email ou senha incorretos.')
            
            if not user.is_active:
                raise serializers.ValidationError('Conta de usuário desativada.')
            
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError('Email e senha são obrigatórios.')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_email(self, value):
        user = self.instance
        if user and User.objects.filter(email=value.lower()).exclude(id=user.id).exists():
            raise serializers.ValidationError('Este email já está cadastrado.')
        return value.lower()
