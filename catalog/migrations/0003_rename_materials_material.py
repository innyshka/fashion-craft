from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_clothing_image"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Materials",
            new_name="Material",
        ),
    ]
