from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from parler.models import TranslatedFields

blog_category_translations = TranslatedFields(
    name=models.CharField(_('name'), max_length=752),
    slug=models.SlugField(_('slug'), max_length=752, blank=True, db_index=True),
    meta_description=models.TextField(
        verbose_name=_('category meta description'), blank=True, default=''
    ),
    meta={'unique_together': (('language_code', 'slug'),)}
)

post_translations = TranslatedFields(
    title=models.CharField(_('title'), max_length=752),
    slug=models.SlugField(_('slug'), max_length=752, blank=True,
                          db_index=True, allow_unicode=True),
    subtitle=models.CharField(verbose_name=_('subtitle'), max_length=767,
                              blank=True, default=''),
    abstract=HTMLField(_('abstract'), blank=True, default='',
                       configuration='BLOG_ABSTRACT_CKEDITOR'),
    meta_description=models.TextField(verbose_name=_('post meta description'),
                                      blank=True, default=''),
    meta_keywords=models.TextField(verbose_name=_('post meta keywords'),
                                   blank=True, default=''),
    meta_title=models.CharField(verbose_name=_('post meta title'),
                                help_text=_('used in title tag and social sharing'),
                                max_length=2000,
                                blank=True, default=''),
    post_text=HTMLField(_('text'), default='', blank=True,
                        configuration='BLOG_POST_TEXT_CKEDITOR'),
    meta={'unique_together': (('language_code', 'slug'),)}
)

blog_config_translations = TranslatedFields(
    app_title=models.CharField(_('application title'), max_length=234),
    object_name=models.CharField(
        _('object name'), max_length=234, default=get_setting('DEFAULT_OBJECT_NAME')
    ),
)
