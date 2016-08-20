from django.shortcuts import render

def index(request):
	if 'number' in request.GET:
		number = int(request.GET['number'])
		if(number<1):
			return render(request, 'index.html',{"output":"Term should be greater than zero","number":number})
		for i in range(number+1):
			term=fun(i)
		output = str(number) + "th term is " + str(term)
		return render(request, 'index.html',{"output":output,"number":number})
	return render(request, 'index.html',{"output":""})

def fun(n):
	if(n<=1):
		return n
	else:
		return(fun(n-1)+fun(n-2))