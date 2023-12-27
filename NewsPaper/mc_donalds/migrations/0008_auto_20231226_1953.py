# Generated by Django 4.2 on 2023-12-26 19:53

from django.db import migrations


DATA_REPAIR = (
    ("AU", "Australia", "Австралия"),
    ("GB","United Kingdom", "Великобритания (Соединенное Королевство)"),
    ("US","United States", "Соединенные Штаты Америки (США)"),
    ('OA', 'OAPI', 'Африканская ОИС'),
    ('BX', 'BOIP', 'ОИС Бенилюкса'),
    ('EM', 'EUIPO', 'Ведомство ЕС по ИС'),
)

AU = 'AU'


def data_change_au(apps, schema_editor):
    model = apps.get_model('mc_donalds', 'Country')
    obj = model.objects.filter(classifier='AU0').only('id').first()
    if obj:
        obj.classifier = 'AU'
        obj.save()


def data_repair(apps, schema_editor):
    model = apps.get_model('mc_donalds', 'Country')
    for classifier, en, ru in DATA_REPAIR:
        obj = model.objects.filter(classifier=classifier).only('id').first()
        if obj:
            obj.name = en
            obj.name_ru = ru
            obj.name_en = en
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mc_donalds', '0007_country'),
    ]

    operations = [
        migrations.RunPython(data_change_au, migrations.RunPython.noop),
        migrations.RunPython(data_repair, migrations.RunPython.noop),
    ]