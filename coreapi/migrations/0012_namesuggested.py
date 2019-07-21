# Generated by Django 2.2.1 on 2019-07-09 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0011_auto_20190626_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameSuggested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestedName', models.CharField(max_length=80)),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
                ('feedBackId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapi.InputEmbed')),
            ],
        ),
    ]
