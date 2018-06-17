from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "index.html")

def rocketplush(request):
	return render(request, "rocketplush.html")
