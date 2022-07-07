from django.contrib import admin
from .models import Interview,Application,Techstack

admin.site.site_header = 'Project tilapea'

class InterviewInline(admin.TabularInline):
	model = Interview
	extra = 0
	max_num = 10

class TechstackInline(admin.TabularInline):
	model = Techstack
	extra = 0
	max_num = 10


class ApplicationAdmin(admin.ModelAdmin):
	list_display= ('id',"title",'location',
	             'status')
	list_filter=("title", "status","location",)

	inlines = [
		TechstackInline,


	 ]
	class Meta:
		model = Application


class InterviewAdmin(admin.ModelAdmin):
	list_display= ('id','salary_talk','salary',)
	list_filter=("salary",)

	class Meta:
		model = Application


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Interview,InterviewAdmin)
# admin.site.register(Schedule)
admin.site.register(Techstack)
