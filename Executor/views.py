from django.shortcuts import render , HttpResponse
from .serializers import StudentSerializers 
from .models import CustomUser 
from .models import CodingProblem
from django.http import JsonResponse
import requests 
import base64
from .models import InputParameter ,OutputParameter 
URL = "https://judge0-ce.p.rapidapi.com/submissions"


querystring = {"base64_encoded":"true","fields":"*"}
headers = {
	"content-type": "application/json",
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "db9e3cdc0amsh826140a7f2f82f3p1dd862jsn12c3bebf19cc",
	"X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
}
# from .models import Student 

from rest_framework.renderers import JSONRenderer 

langauge = {'java' : 62 , 'python' : 71 , 'c++17' :54 }
# Create your views here.

def login(request):
    if request.method == 'POST':
        dict = request.POST.keys()  
        if 'pass1' in dict:
            print(request.POST['pass1']) 
        if 'pass'  in dict : 
            print(request.POST['pass']) 

        print(request.user.is_authenticated)  
        # print(request.POST.keys())
        # print(request.POST['email'])
        # print(request.COOKIES)
        # print(request.session)
        # print(request.user)
    return render(request , 'Executor/login.html') 

def home(request):
    data = CodingProblem.objects.all()
    context = {'problem': data} 
    return render(request , 'Executor/index.html' , context  = context) 

def problems(request , pk):
    data = CodingProblem.objects.get(id = pk) 
    context = {'data' : data} 
    return render(request , 'Executor/problems.html' , context = context) 

def run_code(request):
    if request.method=='POST' : 
        
        #code
        code = request.POST['code'] 
        encoded = base64.b64encode(code.encode()).decode() 
        #language
        lang = request.POST['selected_language'].lower() 
        
        #problemid
        problemid = request.POST['problemid'] 
        
        #input parameter
        input_ = InputParameter.objects.get(id =problemid).value
        
        #output parameter
        output_ = OutputParameter.objects.get(id =problemid).value


        
        payload = {
            "language_id": langauge[lang],
            "source_code": encoded,
            "stdin":base64.b64encode(input_.encode()).decode() 
        }

        #send post request for creating submission 
        # response = requests.post(URL, json=payload, headers=headers, params=querystring)

        # print(response.json())
        # submission_token = response.json()['token'] 

        #send get request for getting subbmission
        # URL_RESP = f"https://judge0-ce.p.rapidapi.com/submissions/{submission_token}"
        # response = requests.get(URL_RESP, headers=headers, params=querystring)
        # print(response.json()['stdout']) 
        
        result = None 
        # result = base64.b64decode(response.json()['stdout']).decode() 


        response_data = {'result': result}
        return JsonResponse(response_data)
    return render(request , 'Executor/submit.html') 



def get_data(request  , pk ):
    data = CustomUser.objects.get(id = pk) 
    serializer = StudentSerializers(data) 
    print(data)
    print(request.user)
    jsonData = JSONRenderer().render(serializer.data) 
    return HttpResponse(jsonData , content_type = 'application/json') 
