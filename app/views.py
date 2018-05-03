from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def keyboard(request):

    return JsonResponse(
        {
        'type': 'buttons',
        'buttons': ['1번','2번']
        }
    )

def message(request):

    return JsonResponse(
        {
            'message':{
                'text':'메세지를 써라'
            },
            'keyboard':{
                'type': 'buttons',
                'buttons': ['1번', '2번','3번']
            }
        }
    )
