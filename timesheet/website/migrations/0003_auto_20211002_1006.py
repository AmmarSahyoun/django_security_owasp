# Generated by Django 2.2.5 on 2021-10-02 08:06

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_userdetails_chargetoclientrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totp',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='totp',
            name='secret',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=32)),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='chargeToClientRate',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=6),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]