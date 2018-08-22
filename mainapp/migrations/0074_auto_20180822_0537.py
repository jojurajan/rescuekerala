# Generated by Django 2.1 on 2018-08-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0073_merge_20180822_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='unique_identifier',
            field=models.CharField(default='', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='checkin_date',
            field=models.DateField(blank=True, null=True, verbose_name='Check-in Date - ചെക്ക്-ഇൻ തീയതി'),
        ),
        migrations.AlterField(
            model_name='person',
            name='checkout_date',
            field=models.DateField(blank=True, null=True, verbose_name='Check-out Date - ചെക്ക്-ഔട്ട് തീയതി'),
        ),
    ]