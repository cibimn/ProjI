from ninja import NinjaAPI, Schema
from ninja.security import HttpBearer
from ninja.security import APIKeyHeader
from vow.models import API, schedule, customers




class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        api_key = [str(key) for key in API.objects.all()]
        if key in api_key:
            return key

header_key = ApiKey()

api = NinjaAPI()


@api.get("/headerkey", auth=header_key)
def apikey(request):
    return f"Authenticated"


####################Get Schedule########################
class ScheduleItem(Schema):
    date: str
    user_email: str

def get_user_id(email):
    ids = customers.objects.filter(Email=email).values()
    id = ids.values()
    print()
    return(id[0]['id'])

@api.post("/schedule", auth=header_key)
def schedule_api(request, item: ScheduleItem):
    print(item.date)
    id = get_user_id(item.user_email)
    a = schedule.objects.filter(date=str(item.date), user=id)
    print(a)
    affirmation = dict({"affirmation":str(a[0].affirmation), "times":int(a[0].no_of_times)})
    print(type(item))
    return affirmation


####################Create Customer########################
class create_customer_api(Schema):
    first_name: str 
    last_name: str
    age: int
    email: str 
    agent: int
    organization: int
    
@api.post("/create_customer", auth=header_key)
def create_customer(request, item: create_customer_api):

    try:
        customers.objects.create(first_name=item.first_name,last_name=item.last_name,email=item.email,age=item.age,agent_id=item.agent,organization_id=item.organization)
        message = dict({"status": "success"})
    except Exception as e:
        print(e)
        message = dict({"status":"failure", "error_message":str(e)})
    return message