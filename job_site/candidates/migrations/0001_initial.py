# Generated by Django 3.2.7 on 2022-04-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'male'), (2, 'not specified'), (1, 'female')])),
                ('mobile', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('expected_salary', models.IntegerField()),
                ('will_relocate', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateJobMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('rejected', 'Rejected'), ('pending', 'Pending'), ('accepted', 'Accepted')], default='pending', max_length=20)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
    ]
