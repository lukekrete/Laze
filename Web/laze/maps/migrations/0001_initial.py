# Generated by Django 2.1.3 on 2018-11-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('num_votes', models.IntegerField(default=0)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('FOOD', 'Food'), ('Entertainment', (('T', 'Theater'), ('M', 'Mall'))), ('VEHP', 'Parking'), ('STY', 'Study'), ('Recreational', (('GYM', 'Gym'), ('POOL', 'Swimming Pool'), ('SQUA', 'Squash Court'), ('BSKT', 'Basketball Court'), ('PARK', 'Parks')))], max_length=4)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
    ]
