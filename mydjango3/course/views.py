from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    cname="Python"
    seats=10
    coursename={'cn':cname,'total_seats':seats}

    return render(request,'course/courseone.html',context=coursename)


def learn_python(request):
    return render(request,'course/coursetwo.html')

