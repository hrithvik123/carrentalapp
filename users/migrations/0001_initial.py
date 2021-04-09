# Generated by Django 3.2 on 2021-04-09 19:08

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField(blank=True, default='21', max_length=2)),
                ('contactNo', models.PositiveIntegerField(blank=True, default='0', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Rental_Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_day_rent', models.IntegerField(default=0)),
                ('per_month_rent', models.IntegerField(default=0)),
                ('touring_package', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_no', models.CharField(default=None, max_length=20)),
                ('price', models.IntegerField()),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('seating_cap', models.IntegerField()),
                ('transmission', models.CharField(choices=[('A', 'Automatic'), ('M', 'Manual')], max_length=1)),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('drivers_license', models.IntegerField(default=0, unique=True)),
            ],
            options={
                'verbose_name': 'Customer',
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('manager_ssn', models.IntegerField(default=0, unique=True)),
            ],
            options={
                'verbose_name': 'Manager',
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Associate',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('Ssn', models.IntegerField(default=0, unique=True)),
            ],
            options={
                'verbose_name': 'Sales Associate',
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='Login', max_length=255)),
                ('email_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_prov', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Manager_creates_pack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.rental_package')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_testdrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=datetime.datetime(2021, 4, 9, 19, 13, 32, 725413))),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.vehicle')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=5)),
                ('feedback', models.CharField(max_length=255)),
                ('bot_chat', models.BooleanField()),
                ('customer_question', models.CharField(max_length=255)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
                ('sales_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.sales_associate')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=datetime.datetime(2021, 4, 10, 19, 8, 32, 722924))),
                ('end_time', models.DateTimeField(default=datetime.datetime(2021, 4, 11, 19, 8, 32, 722948))),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.rental_package')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
                ('sales_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.sales_associate')),
            ],
        ),
    ]
