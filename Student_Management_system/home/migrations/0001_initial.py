# Generated by Django 3.0 on 2022-12-22 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_fees', models.FloatField()),
                ('course_duration', models.FloatField()),
                ('course_text', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=50)),
                ('t_email', models.EmailField(max_length=254)),
                ('t_mobile', models.IntegerField(verbose_name='')),
                ('t_joining', models.IntegerField(verbose_name='')),
                ('t_education', models.CharField(max_length=50)),
                ('t_id', models.CharField(max_length=50)),
                ('t_experience', models.IntegerField(verbose_name='')),
                ('t_package', models.IntegerField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('college', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('Std_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Course')),
            ],
        ),
    ]
