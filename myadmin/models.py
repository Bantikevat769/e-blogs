from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import User

from django.utils import timezone
# from myadmin.models import send_notification


# Create your models here.
# Add CATEGORY MODEL
class Category(models.Model):
    # Field for storing the name of the category
    category_name = models.CharField(max_length=255, help_text='Category Name')
    # Field for storing an image related to the category, uploaded to the 'upload/' directory
    image = models.ImageField(upload_to='upload/', blank=True)

    class Meta:
        # Specify the database table name
        db_table = "tabcategory"

    def __str__(self):
        # Return the name of the category as the string representation of the object
        return self.category_name

# Add SUBCATEGORY MODEL
class Subcategory(models.Model):
    # Field for storing the foreign key reference to the associated category
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Field for storing the name of the subcategory
    subcategory_name = models.CharField(max_length=255, help_text='Subcategory Name')
    # Field for storing an image related to the subcategory, uploaded to the 'upload/' directory
    image = models.ImageField(upload_to='upload/', blank=True)

    class Meta:
        # Specify the database table name
        db_table = "tabsubcategory"

    def __str__(self):
        # Return the name of the subcategory as the string representation of the object
        return self.subcategory_name



# Add SUBCATEGORY MODEL
class Blog(models.Model):
    views = models.IntegerField(default=0)
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish')
    )

    SECTION =(
        
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editor_Pick','Editor_Pick'),
        ('Tranding','Tranding'),
        ('Inspiration','Inspiration'),
        ('Latest_Posts','Latest_Posts'),
        
    )

    # Field for storing the name of the blog post
    post_name = models.CharField(max_length=255, help_text='Post name')
    # Field for storing the title of the blog post
    post_title = models.CharField(max_length=255, help_text='Post title')
    # Field for storing the ID of the category associated with the blog post
    category_id = models.IntegerField()
    # Field for storing the ID of the subcategory associated with the blog post
    subcategory_id = models.IntegerField()
    # Field for storing the details or content of the blog post
    # details = models.TextField(max_length=10000, help_text='Details')
    details = RichTextField(blank=True,null=True)
    # Field for storing an image related to the blog post, uploaded to the 'upload/' directory
    image = models.ImageField(upload_to='upload/', blank=True)
    # Field for storing an audio file related to the blog post, uploaded to the 'audio/' directory
    audio = models.FileField(upload_to="audio/", blank=True, null=True)

    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)
    status = models.CharField(choices=STATUS, max_length=100, default='Draft')
    section = models.CharField(choices=SECTION, max_length=100, default='Popular')  # Setting default value

    main_post=models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True, default='')

    publish_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    # tags = models.ManyToManyField(Tag,
    #     related_name='tag_blogs',
    #     blank=True)  # Many-to-Many relationship with Tag model

    

    class Meta:
        # Specify the database table name
        db_table = "tabblog"

    def __str__(self):
        # Return the title of the blog post as the string representation of the object
        return self.post_title
    

def create_slug(instance, new_slug=None):
    slug = slugify(instance.post_title)  # Generate slug from post title
    if new_slug is not None:
        slug = new_slug
        qs = Blog.objects.filter(slug=slug).order_by('-id')
        exists = qs.exists()
        if exists:
            new_slug = "%s-%s" % (slug, qs.first().id)
            return create_slug(instance, new_slug=new_slug)
    return slug
    
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Blog)



#contact 
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    query = models.TextField()

    def __str__(self):
        return self.first_name
 




class Subscriber(models.Model):
    email = models.EmailField(unique=True)


class Ebook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to='ebooks/')
    users = models.ManyToManyField(User, related_name='purchased_ebooks', blank=True)
    download_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

