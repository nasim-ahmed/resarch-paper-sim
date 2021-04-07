# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from ProjectUtilities import dataUtil
import json


def index(request):
    df = dataUtil.load_dataset_meta()
    return dataframe_to_json_response(df)


def get_paper(request):
    params = request.GET
    try:
        source = params['id']
    except:
        return JsonResponse({'status':'false', 'message':"missing params"}, status=400)
    return dataframe_to_json_response(dataUtil.get_paper_by_id(source))


def compare2(request):
    params = request.GET
    try:
        source = params['source']
        target = params['target']
    except:
        return JsonResponse({'status': 'false', 'message': "missing params"}, status=400)

    print(source, target)
    results = dataUtil.get_compare(source, target)
    print(results)
    return JsonResponse({'results': results}, status=200)


def compare(request):
    params = request.GET
    try:
        source = params['source']
        target = params['target']
    except:
        return JsonResponse({'status': 'false', 'message': "missing params"}, status=400)

    with open('./api/temp.json', 'r') as f:
        r = json.load(f)
    return JsonResponse(r, status=200)


def dataframe_to_json_response(_df):
    json_string = _df.to_json(orient='records')
    parsed = json.loads(json_string)
    response = JsonResponse({
        'dataset': parsed
    })
    return response