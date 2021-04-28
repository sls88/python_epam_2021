from django.contrib import admin  # noqa

from .models import Homework, HomeworkDone, HomeworkResult, Student, Teacher

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(HomeworkResult)
admin.site.register(HomeworkDone)
