from django.http import HttpResponse
from django.shortcuts import render

def plantillaCV(request):
	return render(request, 'plantillaCV.html',{})