from django.shortcuts import render
from .forms import RawDataForm

import numpy as np
from RunModel import draw2pr,mypredict
# Create your views here.
def index(request):
	script1,script2,div1,div2 = draw2pr()
	if request.method == 'POST':
		form = RawDataForm(request.POST)
		params = []
		if form.is_valid():
			a = form.cleaned_data['Hatch_Distance'] 
			params.append(a)
			b = form.cleaned_data['Beam_Current'] 
			params.append(b)
			c = form.cleaned_data['Scan_Speed'] 
			params.append(c)

			X_test = np.array([params]).astype(np.float32)
			y_pred = mypredict(X_test)
			return render(request,'mypattern.html',{'form':form,'the_script1':script1,'the_div1':div1,'the_script2':script2,'the_div2':div2,'form':form,'result':str(y_pred)})
	else:
		form = RawDataForm()
	return render(request,'mypattern.html',{'form':form,'the_script1':script1,'the_div1':div1,'the_script2':script2,'the_div2':div2})
def index1(request):
	return render(request,'mypattern0.html')