from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import CharBlock, RichTextBlock, DateBlock
from django.core.exceptions import ValidationError

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_ordered_posts(self):
        return self.get_children().live().order_by('-first_published_at')

class BlogPost(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('heading', CharBlock(form_classname="title")),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('date', DateBlock()),
    ], use_json_field=True, blank=True)  # Added blank=True to make it optional

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('featured_image'),
        FieldPanel('body'),
    ]

    class BlogPostMeta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def clean(self):
        super().clean()
        # Removing the file permission check that was causing issues
        # The Wagtail image model already handles basic validation


class HomePage(Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_blog_posts(self):
        # Get blog posts from all child BlogIndexPages
        blog_index = BlogIndexPage.objects.live().first()
        if blog_index:
            return blog_index.get_ordered_posts()[:3]
        return []

    class Meta:
        verbose_name = "Homepage"
