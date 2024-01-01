from django import forms


from manage_club.models import Member, Event, Attendance, Task



class MemberForm(forms.ModelForm):


    class Meta:
        model = Member
        fields = "__all__"



class EventForm(forms.ModelForm):


    class Meta:
        model = Event
        fields = "__all__"
        


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member', 'grade']



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'member']
