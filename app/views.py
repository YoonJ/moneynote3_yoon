from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dbconnect import insert_data

#temp_data = get_data('김채우오')
#print(temp_data)

# Create your views here.
def keyboard(request):

    return JsonResponse(
        {
        'type': 'buttons',
        'buttons': ['데이터 생성','1']
        }
    )

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']

    if return_str == '데이터 생성':
        insert_data()
        return JsonResponse({
            'message':{
                'text':'데이터 삽입'
            },
            'keyboard':{
                'type': 'buttons',
                'buttons': ['데이터 생성]
            }
        })
    else:
        return JsonResponse({
            'message':{
                'text':'버튼 누르기'
            },
            'keyboard':{
                'type': 'buttons',
                'buttons': ['데이터 생성]
            }
        })
