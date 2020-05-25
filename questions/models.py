from django.db import models


QUESTIONS_CHOICES = (
    ('multiple', 'Multiple Choices'),
    ('choose', 'Choose one answer'),
    ('essay', 'Essay'),
)

class Exam(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'user')


class Question(models.Model):
    order = models.IntegerField()
    question = models.TextField()
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
    option_type = models.CharField(choices=QUESTIONS_CHOICES, max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question


class QuestionOption(models.Model):
    order = models.IntegerField()
    question  = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    option = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.question} - {self.option}'


class Answer(models.Model):
    answer = models.ForeignKey(QuestionOption, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('users.User', related_name='examinee', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.answer.option}'
