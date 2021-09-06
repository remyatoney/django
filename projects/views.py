from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': "Fully functional ecommerce website"
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': "My own portfolio maker app"
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': "An awesome place to connect with people"
    },
    {
        'id': '4',
        'title': 'Email Platform',
        'description': "Best way to send emails"
    },
]

def projects(request):
    msg = 'Hello, you are on the projects page'
    number = 1
    context = {'message': msg, 'number': number, 'projects': projectsList }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})

