# Generated by Django 4.0.2 on 2022-07-17 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eveonline', '0016_character_names_are_not_unique'),
        ('blacklist', '0003_alter_evenote_eve_catagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackListSearchCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eveonline.evecharacter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
