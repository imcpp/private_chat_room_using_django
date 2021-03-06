# Generated by Django 2.1.3 on 2019-02-20 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='author1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message1', to='chat.Room'),
        ),
    ]
