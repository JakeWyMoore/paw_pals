# Generated by Django 3.0.3 on 2020-10-06 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first_app', '0024_auto_20191122_1957'),
        ('second_app', '0005_auto_20191122_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=225)),
                ('user_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_messages', to='first_app.User')),
            ],
        ),
    ]
