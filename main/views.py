from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request = request, template_name="home.html")

def products(request):
    return render(request = request, template_name="products.html")

def reports(request):
    return render(request = request, template_name="Reports.html")

def messages(request):
    return render(request = request, template_name="Messages.html")

def calendar(request):
    return render(request = request, template_name="Calendar.html")

def table(request):
    return render(request = request, template_name="Table.html")

def components(request):
    return render(request = request, template_name="UIComponents.html")

def users(request):
    return render(request = request, template_name="Users.html")