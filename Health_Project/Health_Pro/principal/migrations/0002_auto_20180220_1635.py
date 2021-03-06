# Generated by Django 2.0.2 on 2018-02-20 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamentos_Pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_expedicion', models.DateField()),
                ('resurtir', models.BooleanField(default=False)),
                ('id_medicamento', models.ManyToManyField(to='principal.Medicamentos')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Pacientes')),
            ],
        ),
        migrations.DeleteModel(
            name='Medicamentos_Paciente',
        ),
    ]
