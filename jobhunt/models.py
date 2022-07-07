from django.db import models
from datetime import datetime, date, timedelta
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
INTERVIEW_TYPES = (
    ('virtual', _('virtual')),
    ('in person', _('in person')),
    ('other', _('other')),

)
VERDICT = (
    ('bad', _('bad')),
    ('ok', _('ok')),
    ('good', _('good')),
    ('v.good', _('v.good')),

)

PLATFORM_TYPES = (
    ('google meet', _('google meet')),
    ('zoom', _('zoom')),
    ('microsoft teams', _('microsoft teams')),
    ('other', _('other')),

)

TECH_STACK = (
    ('JavaScript', _('JavaScript')),
    ('TypeScript', _('TypeScript')),
    ('React', _('React')),
    ('Django', _('Django')),
    ('Vue', _('Vue')),
    ('other', _('other')),

)

STATUS_TYPES = (
    ('applied', _('applied')),
    ('first interview', _('first interview')),
    ('second interview', _('second interview')),
    ('third interview', _('third interview')),
    ('final offer', _('final offer')),
)


class Application(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=32, choices=STATUS_TYPES, default='applied')

    def __str__(self) -> str:
        return self.title

    def getTotalApps(self):
        return "to"


class Interview(models.Model):
    application = models.ForeignKey(
        Application, related_name='interviews', null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=30)
    type = models.CharField(
        max_length=32, choices=INTERVIEW_TYPES, default='virtual')
    platform = models.CharField(
        max_length=32, choices=PLATFORM_TYPES, default='google hangout')
    salary_talk = models.BooleanField(default=False)
    salary = models.IntegerField(default=45000)
    verdict = models.CharField(max_length=32, choices=VERDICT, default='good')

    def __str__(self) -> str:
        return self.application.title

    def techstack(self) -> str:
        return "hu"

    def getApp(self) -> str:
        return self.application.title


# class Schedule(models.Model):
#     date=models.DateTimeField(default=timezone.now)
#     application=models.ForeignKey(Application,related_name='schedules',null=True,on_delete=models.CASCADE)

class Techstack(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    application = models.ForeignKey(
        Application, related_name='techstack', null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.application.title


class Summary(models.Model):
    pass
