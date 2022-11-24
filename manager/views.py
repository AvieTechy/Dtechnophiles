from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

def diary(request):
    return render(request, 'diary.html')

def report(request):
    return render(request, 'report.html')

def worksheet(request):
    return render(request, 'worksheet.html')

def contract(request):
    return render(request, 'contract.html')

def plan(request):
    return render(request, 'plan.html')

def week1(request):
    return render(request, 'week1.html')

def week2(request):
    return render(request, 'week2.html')

def diary(request):
    return render(request, 'diary.html')

def nhi(request):
    return render(request, 'nhi.html')

def khoa(request):
    return render(request, 'khoa.html')

def huyen(request):
    return render(request, 'huyen.html')

def minh(request):
    return render(request, 'minh.html')

def loc(request):
    return render(request, 'loc.html')
