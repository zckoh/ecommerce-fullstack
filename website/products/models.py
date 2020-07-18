from djongo import models
from django.utils.html import mark_safe
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_details = models.TextField()
    slug = models.SlugField(verbose_name="URL link", null=True, unique=True)
    updated_date = models.DateTimeField('Last Updated', auto_now=True)

    main_product_image = models.ImageField(
        upload_to='products')

    addtional_image_1 = models.ImageField(null=True, blank=True,
                                          upload_to='products')

    addtional_image_2 = models.ImageField(null=True, blank=True,
                                          upload_to='products')

    addtional_image_3 = models.ImageField(null=True, blank=True,
                                          upload_to='products')

    addtional_image_4 = models.ImageField(null=True, blank=True,
                                          upload_to='products')

    addtional_image_5 = models.ImageField(null=True, blank=True,
                                          upload_to='products')

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.main_product_image.url)

    image_tag.short_description = 'Product Image'

    def __str__(self):
        return self.product_name

    objects = models.DjongoManager()
