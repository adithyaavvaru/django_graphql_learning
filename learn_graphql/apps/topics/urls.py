from django.contrib import admin
from django.urls import path
# from django.urls import
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', GraphQLView.as_view(graphiql=True)),
]
