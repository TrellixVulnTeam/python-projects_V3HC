# Generated by Django 2.2.6 on 2019-10-11 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='edescription',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterModelTable(
            name='employee',
            table=None,
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
    ]
