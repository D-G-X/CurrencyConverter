from django.http import HttpResponse
from django.shortcuts import render
from forex_python.converter import CurrencyRates

# Create your views here.

def home(request,*args,**kwargs):
	values = {}
	error = 0
	if request.method == 'POST':
		c = CurrencyRates()
		values = request.POST
		fromcur = values['from-cur']
		tocur = values["to-cur"]
		amount = float(values["from-cur-amount"])
		try:
			fromtorate = str(c.get_rate(fromcur,tocur))[:-6]
			fromtovalue = str(c.convert(fromcur,tocur,amount))
			fromtoratestr = "1 {} = {} {}".format(fromcur,fromtorate,tocur)
			print(fromtorate)
			print(fromtovalue)
		except:
			print("error")
			fromtorate = None
			fromtovalue = ""
			fromtoratestr = ""
			error = -1
		# print(values)
		return render(request,"index.html",{"outvalue":fromtovalue,"from":fromcur,"to":tocur,"invalue":amount,"rates":fromtoratestr,"error1":error})
	return render(request,"index.html",{})