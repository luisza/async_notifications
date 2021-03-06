# Generated by Django 3.0.3 on 2020-05-18 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('async_notifications', '0004_auto_20200228_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=500, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('recipient', models.TextField(verbose_name='Recipient list')),
                ('bcc', models.TextField(blank=True, null=True, verbose_name='Bcc Blind carbon copy list')),
                ('cc', models.TextField(blank=True, null=True, verbose_name='Cc Carbon Copy list')),
                ('file', models.FileField(blank=True, null=True, upload_to='email/%Y/%M', verbose_name='File')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Create datetime')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'verbose_name': 'News Letter template',
                'verbose_name_plural': 'News Letter templates',
            },
        ),
        migrations.CreateModel(
            name='NewsLetterTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Template title')),
                ('name', models.SlugField(help_text='Name used to save template in template system, used to extends', max_length=250, unique=True, verbose_name='Template name')),
                ('message', models.TextField(help_text='<a target="_blank" href="https://docs.djangoproject.com/en/3.0/ref/templates/language/">Referencia a lenguaje de plantillas</a>\n                               <br> Puede hacer uso de otras plantillas usando herencia de la forma {% extends \'async_notifications/newslettertemplate name.html\' %}\n                               <br> Osea el name de este modelo es usado para crear plantillas en disco, por lo que pueden usarse para extender.\n                               <br> Recuerde que extends solo puede usarse al inicio de message\n                               <br><strong>Nota: </strong> al usar ASYNC_TEMPLATES_NOTIFICATION en settings se modifica el prefijo de la plantilla (posiblemente eliminando async_notifications/)', verbose_name='Message')),
                ('file_path', models.TextField(blank=True, null=True, verbose_name='Template file path')),
                ('model_base', models.CharField(help_text='Use this model as base for news', max_length=150, verbose_name='Model base')),
            ],
            options={
                'verbose_name': 'News Letter base template',
                'verbose_name_plural': 'News Letter base templates',
            },
        ),
        migrations.RemoveField(
            model_name='emailnotification',
            name='sended',
        ),
        migrations.AddField(
            model_name='emailnotification',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='Sent'),
        ),
        migrations.CreateModel(
            name='NewsLetterTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateTimeField(verbose_name='Send date')),
                ('sent', models.BooleanField(default=False, verbose_name='Sent')),
                ('total_sent', models.SmallIntegerField(default=0)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='async_notifications.NewsLetter')),
            ],
            options={
                'verbose_name': 'News Letter template',
                'verbose_name_plural': 'News Letter templates',
            },
        ),
        migrations.AddField(
            model_name='newsletter',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='async_notifications.NewsLetterTemplate'),
        ),
    ]
