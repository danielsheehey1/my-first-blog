from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, ChainedManyToManyField, GroupedForeignKey
JQUERY_URL = False
USE_DJANGO_JQUERY = True

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text   

class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Machine(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)
    serial = models.CharField(max_length=200)
    hours = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.model

class Work_Order(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    allotted = models.TimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)
#    machine = GroupedForeignKey(Machine, "customer")
    machine = ChainedForeignKey(Machine, chained_field = "customer", chained_model_field = "customer", show_all = False, auto_choose = False, sort = False)

    def __str__(self):
        return self.name

class Work_Order_Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    worder = models.ForeignKey(Work_Order, on_delete = models.PROTECT)
    comment = models.TextField()
    complete = models.BooleanField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    assigned = models.ManyToManyField(Work_Order_Item)

    def __str__(self):
        return self.name

#
#test for tables
#

class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name="full name")





