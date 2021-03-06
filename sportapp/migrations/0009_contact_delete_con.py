# Generated by Django 4.0.1 on 2022-04-07 06:47

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0008_rename_contact_con'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
                ('email', models.CharField(default='', max_length=120)),
                ('phone', models.CharField(default='', max_length=120)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], default='test', max_length=120)),
                ('sport', multiselectfield.db.fields.MultiSelectField(choices=[('Cricket', 'Cricket'), ('Kabaddi', 'Kabbaddi'), ('Badmintion', 'Badmintion'), ('Chess', 'Chess'), ('Volleyball', 'volleyball')], default='test', max_length=120)),
                ('address', models.CharField(default='', max_length=120)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='con',
        ),
    ]
