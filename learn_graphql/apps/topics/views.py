from django.shortcuts import render
from django.http import HttpResponse

from learn_graphql.schema import schema


# Create your views here.
def topics(response):
    query_string = '{ hello }'
    result = schema.execute(query_string)
    return HttpResponse(result.data['hello'])
