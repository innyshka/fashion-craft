from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_size_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="size",
            options={},
        ),
    ]
