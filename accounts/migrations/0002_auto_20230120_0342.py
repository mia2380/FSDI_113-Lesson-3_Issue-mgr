# Generated by Django 4.1.5 on 2023-01-20 03:42

from django.db import migrations


def populate_roles(apps, schemaeditor):
    roles = {
        'Developer': 'Someone who develops software',
        'Scrum Master': 'The coach',
        'Product Owner': 'The person responsible for managing requirements'
    }

    Role = apps.get_model('accounts', 'Role')
    for name, desc in roles.items():
        role_obj = Role(name=name, description=desc)
        role_obj.save()


def populate_teams(apps, schemaeditor):
    teams = {
        'Alpha': 'The A team',
        'Bravo': 'The B team',
        'Charlie': 'The C team',
        'Delta': 'The D team'
    }
    Team = apps.get_model('accounts', 'Team')
    for name, desc in teams.items():
        team_obj = Team(name=name, description=desc)
        team_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_roles),
        migrations.RunPython(populate_teams),
    ]
