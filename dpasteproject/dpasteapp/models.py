from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from  datetime import datetime

# Create your models here.

class dPasteList(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    project_name = models.CharField(max_length = 256)
    date_created = models.DateField(default = now().date())

    intervals = (
        ("one day", "one day"),
        ("one week", "one week"),
        ("one month", "one month"),
        ("one year","one year"),
        ("never", "never")
    )
    expiry_date = models.CharField(
        max_length = 10,
        choices = intervals,
        default = "never"
    )

    def __str__(self):
        return "dPaste List: " + self.project_name


class dPasteListItem(models.Model):

    dpastelist = models.ForeignKey(dPasteList,on_delete = models.CASCADE)
    languages = (
        ("ActionScript","ActionScript"),
        ("Bash","Bash"),
        ("C","C"),
        ("C#","C#"),
        ("C++","C++"),
        ("CSS","CSS"),
        ("GO","GO"),
        ("HTML","HTML"),
        ("Java","Java"),
        ("JavaScript","JavaScript"),
        ("JSON","JSON"),
        ("Perl","Perl"),
        ("PHP","PHP"),
        ("Plain Text","Plain Text"),
        ("Python 2","Python 2"),
        ("Python 3","Python 3"),
        ("RHTML","RHTML"),
        ("Ruby","Ruby"),
        ("Scala","Scala"),
        ("SQL","SQL"),
        ("Swift","Swift"),
        ("Tcl","Tcl"),
        ("XML","XML")
    )
    syntax = models.CharField(
        max_length = 20,
        choices = languages,
        default = "Plain Text"
    )
    file_name = models.CharField(max_length = 50)
    code_snippet = models.TextField()
    version = models.CharField(max_length = 20)