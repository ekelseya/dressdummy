# Generated by Django 3.0.4 on 2020-03-21 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patterns', '0002_auto_20200321_0649'),
        ('stash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patternstash',
            name='pattern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patterns.PatternType'),
        ),
    ]
