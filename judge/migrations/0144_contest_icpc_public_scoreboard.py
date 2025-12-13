# Generated manually for adding ICPC public scoreboard flag
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0143_auto_20250923_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='icpc_public_scoreboard',
            field=models.BooleanField(
                default=False,
                help_text='Allow the ICPC-specific scoreboard page to be accessed publicly once the scoreboard itself is visible.',
                verbose_name='public ICPC scoreboard',
            ),
        ),
    ]
