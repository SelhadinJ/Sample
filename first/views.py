from django.shortcuts import render
from .forms import StudentForm


# Create your views here.
def index(request):
    return render(request, 'first/index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            student_form.save()

        registered = True
    else:
        student_form = StudentForm()

    return render(request, 'first/register.html',
                  {'registered': registered,
                   'student_form': student_form})
