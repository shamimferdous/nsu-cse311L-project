# Generated by Django 4.0 on 2021-12-28 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_nid_alter_user_phone_number'),
        ('services', '0002_servicestatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_subscription', models.DateField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicestatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'subscriptions',
            },
        ),
    ]