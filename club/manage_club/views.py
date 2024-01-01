from django.shortcuts import render, redirect, get_object_or_404
from manage_club.models import Member, Event, Attendance, Task
from manage_club.forms import MemberForm, EventForm, AttendanceForm, TaskForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'log_in.html')



def loginaction(request):
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Hard-coded email and password for demonstration purposes
        if email == "cao@gmail.com" and password == "cao123":
            # Authentication successful
            return redirect(request,'about.html')  # Replace 'index' with the appropriate URL name or path
        else:
            # Authentication failed
            return render(request, 'log_in.html', {'error_message': 'Invalid login credentials'})
        # If the request method is not POST, render the login page
    return render(request, 'log_in.html')"""
    return render(request,'about.html')

def events(request):
    events = Event.objects.all()
    return render(request, "event.html", {'events':events})


def members(request):
    members = Member.objects.all()
    return render(request, "members.html", {'members':members})


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/members/')
            except:
              
                pass
    else:
        form = MemberForm()
        pass
    return render(request, 'add_member.html',{'form':form})  




def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)  # Add request.FILES for file uploads
        if form.is_valid():
            try:
                form.save()
                return redirect('/events/')
            except Exception as e:
                # Log the exception for debugging
                print(f"Error saving event: {e}")
                # You might want to add a more user-friendly message or redirect to an error page
                pass
        else:
            # Log form errors for debugging
            print(form.errors)
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})


def show(request):
    members = Member.objects.all()
    return render(request, "show.html", {'members':members})


def edit(request, id):
    member = Member.objects.get(id=id)
    return render(request, 'edit.html', {'member':member})

def edit_event(request, id):
    event = Event.objects.get(id=id)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect("/events/")
    else:
        form = EventForm(instance=event)

    return render(request, 'edit_event.html', {'event': event, 'form': form})







def update(request, id):
    employee = Member.objects.get(id=id)
    form = MemberForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/members/")
    return render(request, 'edit.html', {'employee':employee})


def update_event(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(request.POST, request.FILES, instance=event)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/members/")
    return render(request, 'edit_event.html', {'event': event, 'form': form})



def destroy(request, id):
    employee = Member.objects.get(id=id)
    employee.delete()
    return redirect("/members/")

def destroy_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect("/events/")




def event_details(request, id):
    event = get_object_or_404(Event, id=id)
    attendees = event.attendance_set.all()
    tasks = Task.objects.filter(event=event)

        
    return render(request, 'event_details.html', {'event': event, 'attendees': attendees, 'tasks': tasks})

def layout(request):
    return render(request,'layout.html')








def create_task(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.event = event  # Set the event for the attendance record
            task.save()
            return redirect('event_details', id=event_id)  # Redirect to event details page
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'event': event, 'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'event_details.html', {'tasks': tasks})










def take_attendance(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.event = event  
            attendance.save()
            return redirect('event_details', id=event_id)  
    else:
        form = AttendanceForm()

    return render(request, 'take_attendance.html', {'event': event, 'form': form})



def edit_attendance(request, id):
    attendance = get_object_or_404(Attendance, id=id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('/event_details/') 
    else:
        form = AttendanceForm(instance=attendance)

    return render(request, 'edit_attendance.html', {'form': form, 'attendance': attendance})



def update_attendance(request, id):
    attendance = Attendance.objects.get(id=id)
    form = AttendanceForm(request.POST, request.FILES, instance=attendance)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/event_details/")
    return render(request, 'edit_attendance.html', {'attendance': attendance, 'form': form})


    


def destroy(request, id):
    employee = Member.objects.get(id=id)
    employee.delete()
    return redirect("/members/")

def destroy_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect("/events/")



def delete_attendance(request, id):
    attendance = Attendance.objects.get(id=id)
    attendance.delete()
    return redirect("/event_details/")
    attendance = get_object_or_404(Attendance, id=id)
    if request.method == 'POST':
        attendance.delete()
        return redirect('event_details.html') 

    return render(request, 'delete_attendance.html', {'attendance': attendance})






