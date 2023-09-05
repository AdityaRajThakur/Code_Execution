from django.contrib import admin
from .models import CustomUser
from .models import CodingProblem , InputParameter , OutputParameter 




admin.site.register(CustomUser)
admin.site.register(CodingProblem)
admin.site.register(InputParameter)
admin.site.register(OutputParameter)