import uuid

from django.db import models


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Question(BaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='question_category'
    )
    question = models.CharField(max_length=200)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

    def get_answer(self):
        data = []
        answers = list(Answer.objects.filter(question=self))
        for ans_obj in answers:
            data.append({
                'answer': ans_obj.answer,
                'is_correct': ans_obj.is_correct
            })
        return data


class Answer(BaseModel):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='question_answer'
    )
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
