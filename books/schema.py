import graphene 
from graphene_django import DjangoObjectType,DjangoListField
from .models import Books,Category,Quiz,Question,Answer
  
  
class BookType(DjangoObjectType):
  class Meta :
    model = Books
    fields = "__all__"

class BookQuery(graphene.ObjectType):
  allBooks = graphene.List(BookType)
  def resolve_allBooks(root,info):
      return Books.objects.all()
booksChema = graphene.Schema(query=BookQuery)


#########################################################
class CategoryType(DjangoObjectType):
  class Meta:
    model=Category
    fields="__all__"

class AnswerType(DjangoObjectType):
  class Meta:
    model=Answer
    fields="__all__"


class QuestionsType(DjangoObjectType):
  questionsAnswers = DjangoListField(AnswerType)
  class Meta:
    model=Question
    fields=[
      "id",
      "type",
      "question",
      "createdAt",
      "updatedAt",
      "questionsAnswers"
    ]

class QuizType(DjangoObjectType):
  quizQuestions = DjangoListField(QuestionsType)
  class Meta:
    model=Quiz
    fields=[
      "id",
      "title",
      "category",
      "createdAt",
      "updatedAt",
      "quizQuestions"
    ] 





class QuizQuery(graphene.ObjectType):
    allQuizs = graphene.List(QuizType)
    filterQuizs = graphene.List(QuizType,title=graphene.String())
    singleQuiz = graphene.Field(QuizType,id=graphene.Int())
    
    def resolve_allQuizs(root,info):
        return Quiz.objects.filter.all()
    
    def resolve_filterQuizs(root,info,title):
      try :
        return Quiz.objects.filter(title__contains = title)
      except :
        return []
    
    def resolve_singleQuiz(root,info,id):
        return Quiz.objects.get(id =id)
      

quizSchema = graphene.Schema(query=QuizQuery)

