from django.db import models

# Create your models here.
class Books(models.Model):
    BookID = models.IntegerField(primary_key=True)
    BookName = models.CharField(max_length=200)
    NumberOfCopies = models.IntegerField()


class Members(models.Model):
    MemberID = models.IntegerField(primary_key=True)
    MemberName = models.CharField(max_length=50)


class Circulation(models.Model):

    EVENT_TYPE = (
        ('checkout', 'checkout'),
        ('return', 'return')
    )

    date = models.DateTimeField()
    eventtype = models.CharField(choices=EVENT_TYPE, max_length=30)
    book = models.ForeignKey(to=Books, related_name="circulations", on_delete=models.PROTECT)
    member = models.ForeignKey(
        Members, related_name="circulations", on_delete=models.PROTECT
    )
