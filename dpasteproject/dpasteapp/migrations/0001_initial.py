# Generated by Django 2.0.5 on 2018-08-05 18:41

import datetime
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
            name='dPasteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=256)),
                ('date_created', models.DateField(default=datetime.date(2018, 8, 5))),
                ('expiry_date', models.CharField(choices=[('one day', 'one day'), ('one week', 'one week'), ('one month', 'one month'), ('one year', 'one year'), ('never', 'never')], default='never', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='dPasteListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syntax', models.CharField(choices=[('ActionScript', 'ActionScript'), ('Bash', 'Bash'), ('C', 'C'), ('C#', 'C#'), ('C++', 'C++'), ('CSS', 'CSS'), ('GO', 'GO'), ('HTML', 'HTML'), ('Java', 'Java'), ('JavaScript', 'JavaScript'), ('JSON', 'JSON'), ('Perl', 'Perl'), ('PHP', 'PHP'), ('Plain Text', 'Plain Text'), ('Python 2', 'Python 2'), ('Python 3', 'Python 3'), ('RHTML', 'RHTML'), ('Ruby', 'Ruby'), ('Scala', 'Scala'), ('SQL', 'SQL'), ('Swift', 'Swift'), ('Tcl', 'Tcl'), ('XML', 'XML')], default='Plain Text', max_length=20)),
                ('file_name', models.CharField(max_length=50)),
                ('code_snippet', models.TextField()),
                ('version', models.CharField(max_length=20)),
                ('dpastelist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpasteapp.dPasteList')),
            ],
        ),
    ]
