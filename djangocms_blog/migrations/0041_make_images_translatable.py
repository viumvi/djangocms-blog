import django.db.models.deletion
import filer.fields.image
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('filer', '0011_auto_20190418_0137'),
        ('djangocms_blog', '0040_make_categories_sortable'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttranslation',
            name='main_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_image', to=settings.FILER_IMAGE_MODEL, verbose_name='main image'),
        ),
        migrations.AddField(
            model_name='posttranslation',
            name='main_image_full',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_full', to='filer.ThumbnailOption', verbose_name='main image full'),
        ),
        migrations.AddField(
            model_name='posttranslation',
            name='main_image_thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_thumbnail', to='filer.ThumbnailOption', verbose_name='main image thumbnail'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='main_image_full',
        ),
        migrations.RemoveField(
            model_name='post',
            name='main_image_thumbnail',
        ),
    ]
