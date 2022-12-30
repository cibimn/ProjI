from django.contrib import admin
from .models import (User,VOW,Agent,customers,score,Reviews,
                    Answers, Questions, organization, category, usercategory, API, 
                    schedule, feedback, classes)
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class customerResource(resources.ModelResource):

    class Meta:
        model = customers


class CustomerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = customerResource
    list_display = ['name', 'classes' ,'age', 'email', 'agent', 'organization']
    list_display_links = ['name']
    # list_editable = ['email']
    list_filter = ['category','agent','organization']
    search_fields = ['name', 'email']
    
admin.site.register(customers, CustomerAdmin)


class VOWAdmin(admin.ModelAdmin):
    list_display = ['Affirmation', 'agent', 'date', 'category']
    list_display_links = ['Affirmation']
    search_fields =list_display = ['Affirmation', 'agent', 'category']
    list_filter = ['category','agent']

admin.site.register(VOW, VOWAdmin)

class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'organization']
    list_display_links = ['user']
    list_filter = ['organization']

admin.site.register(Agent,AgentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cateogry', 'agent']
    list_display_links = ['cateogry']

admin.site.register(category, CategoryAdmin)

class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ['cateogry', 'agent']
    list_display_links = ['cateogry']

admin.site.register(usercategory,UserCategoryAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['score', 'date', 'email']

admin.site.register(score, ScoreAdmin)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['review', 'date', 'email', 'agent']

admin.site.register(Reviews, ReviewsAdmin)

class AnswersAdmin(admin.ModelAdmin):
    list_display = ['date', 'email', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5']
    list_filter = ['date']
    
admin.site.register(Answers, AnswersAdmin)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['category', 'date', 'agent', 'question1', 'question2', 'question3', 'question4', 'question5']
    list_filter = ['date']
    
admin.site.register(Questions, QuestionsAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display =['username','is_organisor', 'is_agent']
    list_filter = ['is_organisor', 'is_agent']
    
admin.site.register(User,UserAdmin)

# admin.site.register(UserProfile)
admin.site.register(organization)

class API_ADMIN(admin.ModelAdmin):
    list_display = ['Key']

    def has_add_permission(self, request):
        base_add_permission = super(API_ADMIN, self).has_add_permission(request)
        if base_add_permission:
                count = API.objects.all().count()
                if count < 3:
                    print('True')
                    return True
                else:
                    return False
    def has_change_permission(self, request, obj=None):
        return False
    
admin.site.register(API,API_ADMIN)

class scheduleadmin(admin.ModelAdmin):
    list_display = ['date', 'agent', 'date', 'no_of_times']

admin.site.register(schedule, scheduleadmin)

class feedbackadmin(admin.ModelAdmin):
    list_display= ['date', 'affirmation', 'agent',  'feedback']
    list_filter = ['agent', 'feedback']
    
admin.site.register(feedback, feedbackadmin)

class classesadmin(admin.ModelAdmin):
    list_display = ['std', 'sec']

admin.site.register(classes, classesadmin)

admin.site.site_header = 'Project I'
admin.site.site_title = "Project I"
admin.site.index_title = "Welcome to Project I Admin Panel"