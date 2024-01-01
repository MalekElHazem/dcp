from django.db import models

class Member(models.Model):
    mFname = models.CharField(max_length=200)
    mLname = models.CharField(max_length=200)
    memail = models.EmailField(max_length=200)
    mphone = models.CharField(max_length=200)
    mdep = models.CharField(max_length=200)

    def __str__(self):
        return self.mFname
    
    class Meta:
        db_table = "member"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='events/')
    dateD = models.DateField()
    dateF = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "event"


class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.member.mFname} {self.member.mLname} - {self.event.title}"

    class Meta:
        db_table = "attendance"




class Task(models.Model):
    title = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task"



