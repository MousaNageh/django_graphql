from django.urls import path
from graphene_django.views import GraphQLView
from .schema import booksChema,quizSchema
urlpatterns = [
    path("",GraphQLView.as_view(graphiql=True,schema=booksChema)),
    path("quiz",GraphQLView.as_view(graphiql=True,schema=quizSchema)),
]
