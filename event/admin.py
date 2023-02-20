from django.contrib import admin,messages
from .models import *




from datetime import datetime
#  nb : Try to use StackedInline instead of TabularInline
class ParticipationInline(admin.TabularInline):
    model = participants
    readonly_fields=('date_participation',)
    extra = 1
    can_delete=False
    classes =['collapse']
    



# Change state to true with actions:
def set_Accept(ModelAdmin , request , queryset):
    rows_updated =  queryset.update(state=True)
            
    if (rows_updated ==1): 
        msg = " 1 event was"

    else:
        msg = f"{rows_updated}  events were  "

    messages.success(request,f'{msg} successfully updated' )




# Change state to false with actions:
def set_Refuse(ModelAdmin , request , queryset):
    rows_updated =  queryset.update(state=False)
            
    if (rows_updated ==1): 
        message = " 1 event was"

    else:
        message = f"{rows_updated}  events were  "

    messages.success(request,f'{message} successfully updated' )


set_Accept.short_description = "State True"

set_Refuse.short_description = "State False"





@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('title', 'description' ,'image', 'evt_date','category','state', 'created_date','updated_date' ,'organisateur','event_nbr_participant')
     

    list_filter = (  
        'state','category',
        
    )


    
    actions = [set_Accept , set_Refuse]


    autocomplete_fields=['organisateur']

    inlines =[ ParticipationInline]

    # fields =(('title','category') , 'description')

    readonly_fields=('created_date','updated_date')

    fieldsets = ( 
        
        ('Event description', {
                'fields': ('title' ,'category','state','organisateur' , 'image'),
        }),
        ('Dates' , {
        'fields':('evt_date','created_date','updated_date'),
        }),
                 
                 
                 
                 )
    list_per_page = 2

    ordering = ['-title']


    def event_nbr_participant(self,obj):
        count = obj.participant.count()
        return count 
    


    event_nbr_participant.short_description = 'Nombre des participants'



admin.site.register(participants) 
