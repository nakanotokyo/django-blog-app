# Generated by Django 4.0.2 on 2022-06-30 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='更新日時')),
                ('is_published', models.BooleanField(default=False, verbose_name='公開可能か')),
            ],
        ),
    ]
