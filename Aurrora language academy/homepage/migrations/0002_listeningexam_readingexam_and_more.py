# Generated by Django 5.0.2 on 2024-02-26 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReadingExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='multiplechoicequestion',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='fillintheblankquestion',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='option',
            name='question',
        ),
        migrations.CreateModel(
            name='ListeningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.listeningexam')),
            ],
        ),
        migrations.CreateModel(
            name='ListeningOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.listeningquestion')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.readingexam')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingBlank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blank_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.readingquestion')),
            ],
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='FillInTheBlankQuestion',
        ),
        migrations.DeleteModel(
            name='MultipleChoiceQuestion',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]
