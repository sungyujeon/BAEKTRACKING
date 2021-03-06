# Generated by Django 3.1.7 on 2021-04-19 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('difficulty', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(default='백준', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SolvedProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solved_code', models.TextField()),
                ('solved_date', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.site'),
        ),
        migrations.AddField(
            model_name='problem',
            name='solvedUsers',
            field=models.ManyToManyField(related_name='solvedProblems', through='problems.SolvedProblem', to=settings.AUTH_USER_MODEL),
        ),
    ]
