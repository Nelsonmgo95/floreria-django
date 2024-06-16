from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UsuarioAdmin(BaseUserManager):
    def create_user(self, nombre, apellido, email, username, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')
        
        if not username:
            raise ValueError('El usuario debe tener un username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            nombre = nombre,
            apellido = apellido,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            nombre = nombre,
            apellido = apellido,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user





class Usuarios(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=50)
    telefono = models.CharField(max_length=50)

    #fecha de creacion
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    #refgistro de login del usuario
    ultimo_login = models.DateTimeField(auto_now_add=True)

    #es admin?
    is_admin = models.BooleanField(default=False)

    #es staff?
    is_staff = models.BooleanField(default=False)

    #esta activo?
    is_active = models.BooleanField(default=False)

    #es superadmin?
    is_superadmin = models.BooleanField(default=False)

    #Cada usuario utilizara el email para la validacion de datos
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido']

    objects = UsuarioAdmin()

    def __str__(self):
        return self.email
    

    #Permisos de usuarios
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True