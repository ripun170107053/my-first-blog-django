from django.db import models
from django.conf import settings
from django.utils import timezone
#I know I have wasted too much time but God..Please..i need a good job. Else I will become faceless..30/1/20
class Post(models.Model): #defines our model..Post is just a name..like Blog Post
    #models.Model means its a django model so django stores it in the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #lhs of above 5 are properties, foreignkey is a link to another model

    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title