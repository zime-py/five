from django.shortcuts import render


def one(request):
	return render(request,'anisul.html')


def two(request):
	return render(request,'naim.html')


def three(request):
	return render(request,'w3school.html')