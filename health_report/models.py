# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Discover(models.Model):
    cname = models.OneToOneField(Country, models.DO_NOTHING, db_column='cname', primary_key=True)  # The composite primary key (cname, disease_code) found, that is not supported. The first column is selected.
    disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='disease_code')
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)


class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    id = models.ForeignKey('Diseasetype', models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class Diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseasetype'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctor(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Patientdisease(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)  # The composite primary key (email, disease_code) found, that is not supported. The first column is selected.
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')

    class Meta:
        managed = False
        db_table = 'patientdisease'
        unique_together = (('email', 'disease_code'),)


class Patients(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'patients'


class PatientsDisease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patients_disease'


class PatientsPatients(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.ForeignKey('PatientsUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patients_patients'


class PatientsUsers(models.Model):
    email = models.CharField(primary_key=True, max_length=254)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'patients_users'


class Publicservant(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicservant'


class Record(models.Model):
    email = models.OneToOneField(Publicservant, models.DO_NOTHING, db_column='email', primary_key=True)  # The composite primary key (email, cname, disease_code) found, that is not supported. The first column is selected.
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)


class Specialize(models.Model):
    id = models.OneToOneField(Diseasetype, models.DO_NOTHING, db_column='id', primary_key=True)  # The composite primary key (id, email) found, that is not supported. The first column is selected.
    email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'specialize'
        unique_together = (('id', 'email'),)


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
