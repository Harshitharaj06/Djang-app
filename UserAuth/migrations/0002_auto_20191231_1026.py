# Generated by Django 2.2.5 on 2019-12-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
