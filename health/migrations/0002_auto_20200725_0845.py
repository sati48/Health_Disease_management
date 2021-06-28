# Generated by Django 3.0 on 2020-07-25 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('symptom', models.TextField(null=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.Type')),
            ],
        ),
    ]
