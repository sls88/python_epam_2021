from django.db import models  # noqa


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Homework(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    text = models.TextField()
    deadline = models.DurationField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.text


class HomeworkResult(models.Model):
    homeworker = models.ForeignKey(Student, on_delete=models.CASCADE)
    task_text = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.solution


class HomeworkDone(models.Model):
    good_homework = models.ForeignKey(HomeworkResult, on_delete=models.CASCADE)
