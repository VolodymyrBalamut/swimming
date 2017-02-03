from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = 'article'
    article_title = models.CharField(max_length=200)
    article_image = models.ImageField(null=True,blank=True,
                                      width_field='width_field',
                                      height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    article_text = models.TextField()
    article_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    article_like = models.IntegerField(default=0)
    def __unicode__(self):
        return self.article_title
    def __str__(self):
        return self.article_title
class Comments(models.Model):
    class Meta:
        db_table = 'comments'
    comments_text = models.TextField(verbose_name='Comments text')
    comments_date = models.DateTimeField(auto_now=False,auto_now_add=True,null=True, blank=True)
    comments_article = models.ForeignKey(Article)

class Country(models.Model):
    class Meta:
        db_table = 'countries'
    country_name = models.CharField(max_length=20)
    country_text = models.TextField(default='')

    country_image = models.ImageField(null=True,blank=True,
                                      width_field='country_image_width_field',
                                      height_field='country_image_height_field')
    country_image_width_field = models.IntegerField(default=0)
    country_image_height_field = models.IntegerField(default=0)


    country_icon = models.ImageField(null=True,blank=True,
                                      width_field='country_icon_width_field',
                                      height_field='country_icon_height_field')
    country_icon_width_field = models.IntegerField(default=0)
    country_icon_height_field = models.IntegerField(default=0)

    def __unicode__(self):
        return self.country_name
    def __str__(self):
        return self.country_name
class Distance(models.Model):
    class Meta:
        db_table = 'distances'
    distance = models.CharField(max_length=10)
    def __unicode__(self):
        return self.distance
    def __str__(self):
        return self.distance
class Style(models.Model):
    class Meta:
        db_table = 'styles'
    style = models.CharField(max_length=20)
    info = models.TextField(default='Info about')
    image = models.FileField(null=True,blank=True)
    def __unicode__(self):
        return self.style
    def __str__(self):
        return self.style
class Swimmer(models.Model):
    class Meta:
        db_table = 'swimmers'
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    male = models.BooleanField(default = True)
    nationality = models.ForeignKey(Country)
    swimmer_image = models.ImageField(null=True, blank=True,
                                      width_field='swimmer_image_width_field',
                                      height_field='swimmer_image_height_field')
    swimmer_image_width_field = models.IntegerField(default=0)
    swimmer_image_height_field = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
class Record(models.Model):
    class Meta:
        db_table = 'records'
    record_time = models.CharField(max_length=20)
    competition = models.CharField(max_length=50)
    date = models.DateField()
    distance = models.ForeignKey(Distance)
    style = models.ForeignKey(Style)
    swimmer = models.ForeignKey(Swimmer)
    location_city = models.CharField(max_length=20)
    location_country = models.ForeignKey(Country)
    def __unicode__(self):
        if self.swimmer.male:
            text = str(self.distance) + " " + str(self.style.style) + ' male'
        else:
            text = str(self.distance) + " " + str(self.style.style) + ' female'
        return text
    def __str__(self):
        temp_style = str(self.style.style)
        temp_style = temp_style.lower()
        if self.swimmer.male:
            text = str(self.distance) + " " + temp_style + ' male'
        else:
            text = str(self.distance) + " " + temp_style + ' female'
        return text