from django.db import models

class Group(models.Model):
	group_text= models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.group_text

class Question(models.Model):
	group = models.ForeignKey(Group)
	question_text = models.CharField(max_length=200)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	corrected = models.BooleanField(default=False)

	def __str__(self):
		return self.choice_text