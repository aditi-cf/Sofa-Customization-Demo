import json
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Size, Back, BackVariant, PipeVariant, Pipe, Arm, ArmVariant, LegVariant, Leg, Color
from SofaConfig import config_sofa


def index(request):

    arm = ArmVariant.objects.filter(size='size_1', armId=Arm.objects.filter(name='arm_1'),
                                    color=Color.objects.filter(name='green'))[0].as_json()
    back = BackVariant.objects.filter(size='size_1', backId=Back.objects.filter(name='back_1'),
                                      armId=Arm.objects.filter(name='arm_1'))[0].as_json()
    leg = LegVariant.objects.filter(size='size_1', armId=Arm.objects.filter(name='arm_1'))[0].as_json()
    pipe = PipeVariant.objects.filter(size='size_1', color=Color.objects.filter(name='lightgreen'),
                                      armId=Arm.objects.filter(name='arm_1'),
                                      backId=Back.objects.filter(name='back_1'))[0].as_json()
    size = Size.objects.filter(name='size_1')[0].as_json()
    price = float(arm['price']) + float(back['price']) + float(leg['price']) + float(pipe['price'])
    context = {'data': json.dumps([{'arm': arm}, {'back': back},
                                   {'leg': leg}, {'pipe': pipe}, {'size': [size]}, {'price': price}])}

    return render(request, 'csofa/index.html', context)


def index1(request):
    furniture = {'data': json.dumps(config_sofa())}
    return render(request, 'csofa/index1.html', furniture)


def arm_all(request):
    q_set = ArmVariant.objects.filter(size=request.GET["size"], color=Color.objects.filter(name=request.GET["color"]))
    response = []
    for q in q_set:
        response.append(q.as_json())
    return JsonResponse({'data': response})


def arm_color_all(request):
    q_set = ArmVariant.objects.filter(size=request.GET["size"], armId=Arm.objects.filter(name=request.GET["arm"]))
    response = []
    for q in q_set:
        response.append(q.as_json())
    return JsonResponse({'data': response})


def back_all(request):
    q_set = BackVariant.objects.filter(size=request.GET["size"], color=Color.objects.filter(name=request.GET["color"]),
                                       armId=Arm.objects.filter(name=request.GET["arm"]))
    response = []
    for q in q_set:
        response.append(q.as_json())
    return JsonResponse({'data': response})


def back_color_all(request):
    q_set = BackVariant.objects.filter(size=request.GET["size"], backId=Back.objects.filter(name=request.GET["back"]),
                                       armId=Arm.objects.filter(name=request.GET["arm"]))
    response = []
    for q in q_set:
        response.append(q.as_json())
    return JsonResponse({'data': response})


def leg_all(request):
    q_set = LegVariant.objects.filter(size=request.GET["size"], armId=Arm.objects.filter(name=request.GET["arm"]))
    response = []
    for q in q_set:
        response.append(q.as_json())
    return JsonResponse({'data': response})


def leg_color_all(request):
    q_set = LegVariant.objects.filter(size=request.GET["size"], armId=Arm.objects.filter(name=request.GET["arm"]),
                                      legId=Arm.objects.filter(name=request.GET["leg"]))
    response = []
    for q in q_set:
        response.append(q.as_json())
    return JsonResponse({'data': response})


def pipe_all(request):
    q_set = PipeVariant.objects.filter(size=request.GET["size"], color=Color.objects.filter(name='lightgreen'),
                                       armId=Arm.objects.filter(name=request.GET["arm"]),
                                       backId=Back.objects.filter(name=request.GET["back"]))
    response = []
    for q in q_set:
        response.append(q.as_json())
    return JsonResponse({'data': response})


def pipe_color_all(request):
    q_set = PipeVariant.objects.filter(size=request.GET["size"], pipeId=Pipe.objects.filter(name=request.GET["pipe"]),
                                       armId=Arm.objects.filter(name=request.GET["arm"]),
                                       backId=Back.objects.filter(name=request.GET["back"]))
    response = []
    for q in q_set:
        response.append(q.as_json())
    return JsonResponse({'data': response})


