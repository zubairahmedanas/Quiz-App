from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from home.models import Question


# Create your views here.

def home(request):
    return HttpResponse(request, 'home.html')


def get_quiz(request):
    try:
        ques_objs = list(Question.objects.all())
        data = []
        # print("all the ques_objs:", ques_obj)
        for ques_obj in ques_objs:
            data.append({
                "category": ques_obj.category.category_name,
                "question": ques_obj.question,
                "marks": ques_obj.marks,
                "answers": ques_obj.get_answer()
            })
        payload = {
            'status': True,
            'data': data
            }
        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse("something went wrong")
