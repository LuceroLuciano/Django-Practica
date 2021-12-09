from django.db import models

#login y permisos
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):

    def create_superuser(self, email, password = None):
        user = self.model(
            email = self.normalize_email(email),
            #is_active = True
            is_staff = True
        )

        user.set_password(password)
        user.save()
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 120, verbose_name = 'Correo', unique = True)
    photo = models.ImageField(verbose_name = 'Avatar', blank = True)
    addres = models.CharField(max_length = 512, verbose_name = 'direccion')
    status = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRE_FIELDS = []

    class Meta:
        db_table = 'users'
        ordering = ['email']

# Create your models here.

# First table
class Person(models.Model):
    fisrt_name = models.CharField(max_length=32, verbose_name='Nombre')
    last_name = models.CharField(max_length=32, verbose_name='Apellido')
    age = models.IntegerField(default=0, verbose_name='Edad')
    height = models.FloatField(default=0.0, verbose_name='Altura')
    status = models.BooleanField(default=True, verbose_name='Estatus')

    #propiedades de la tabla
    class Meta:
        db_table = 'persons' #nombre de la tabla en plural 
        ordering = ['id', '-age'] #el - indica que el orden va a ser inverso (de mayor a menor)

# Second table
class Job(models.Model):
    #llave secundaria relacionada con job y Person
    person = models.ForeignKey(Person, on_delete = models.CASCADE, related_name ='job', verbose_name = 'Persona')
    name = models.CharField(max_length = 32, verbose_name = 'Nombre trabajo')
    status = models.BooleanField(default = True, verbose_name = 'Estatus')
    
    class Meta:
        db_table = 'jobs'
        ordering =['-id'] #organizados de menor a mayor

