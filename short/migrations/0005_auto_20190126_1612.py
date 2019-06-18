# Generated by Django 2.1.4 on 2019-01-26 10:42

from django.db import migrations, models
import short.validators


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0004_auto_20190126_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[short.validators.validate_url, short.validators.validate_dot_com]),
        ),
    ]