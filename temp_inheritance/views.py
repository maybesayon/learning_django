from django.shortcuts import render

def main(request):
    people = [
        {"name": "Ram", "age": 30, "address": "KTM"},
        {"name": "Shyam", "age": 23, "address": "PKR"},
        {"name": "Hari", "age": 45, "address": "BRT"},
        {"name": "Sita", "age": 26, "address": "BKT"}
    ]
    context = {"people": people}
    return render(request, template_name='temp_inheritance/home.html', context = context)

def features(request):
    items = [
        {"name": "Laptop", "feature": "Portable computer"},
        {"name": "Mouse", "feature": "Navigation input device"},
        {"name": "Keyboard", "feature": "Input device"}
    ]
    return render(request, template_name='temp_inheritance/features.html', context={"items":items})

def pricing(request):
    pass