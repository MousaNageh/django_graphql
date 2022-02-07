from django.db import models

# Create your models here.
class Books(models.Model):
  title = models.CharField(max_length=255)
  descrpition = models.TextField()
  file = models.FileField(upload_to="books")
  
  def __str__(self):
      return self.title
  def __repr__(self):
    return self.title


class Category(models.Model):
  name = models.CharField(max_length=255)
  def __str__(self):
        return self.name 

class Quiz(models.Model):
  title = models.CharField(max_length=255,default="new quiz")
  category = models.ForeignKey(Category,related_name="categorQuizzes",on_delete=models.CASCADE)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  def __str__(self):
        return self.title  


class Question(models.Model):
  QUESTION_TYPE = [
    ("fundamental","fundamental"),
    ("beginner","beginner"),
    ("intermediate","intermediate"),
    ("advanced","advanced"),
    ("expert","expert")
  ]
  quiz =models.ForeignKey(Quiz,related_name="quizQuestions",on_delete=models.CASCADE)
  type = models.CharField(max_length=255,choices=QUESTION_TYPE)
  question = models.TextField()
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  def __str__(self):
        return self.type


class Answer(models.Model):
  question = models.ForeignKey(Question,related_name="questionsAnswers",on_delete=models.CASCADE)
  answer = models.TextField()
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  def __str__(self):
        return self.answer