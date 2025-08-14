from django.shortcuts import render

def add_view(request):
    template_name=''
    context={}
    return render(request, template_name, context)