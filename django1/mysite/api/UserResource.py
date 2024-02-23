from django.http import JsonResponse
from mysite.api.RestResourceBase import RestResourceBase
from mysite.api.valid import *
from mysite.models import mysite

class UserResource(RestResourceBase):
    def __init__(self):
        super().__init__()
    def doTransaction(self,txcode,message):
        match txcode:
            case 'BASIC_USER_LIST_ALL':
                self.data = List_All()        
            case 'BASIC_USER_LIST_FILTER':
                self.data = List_Filter(message)       
            case 'BASIC_USER_FIND_BY_USERNAME':
                self.data = Find_By_Username(message)
            case 'BASIC_USER_INSERT':
                self.data = Insert(message)        
            case 'BASIC_USER_UPDATE':
                self.data = Update(message)
                        
    def decodecontent(self,txcode, message):
        match txcode:
            case 'BASIC_USER_LIST_ALL':
                pass
            case 'BASIC_USER_LIST_FILTER':
                pass                   
            case 'BASIC_USER_FIND_BY_USERNAME':
                pass
            case 'BASIC_USER_INSERT':
                self.check_fields(message, ['username', 'email', 'password'])
                check_valid(message)
                if mysite.objects.filter(username=message["username"]).exists():
                    raise Exception('username已存在')
                if mysite.objects.filter(email=message["email"]).exists():
                    raise Exception('email已存在')
            case 'BASIC_USER_UPDATE':
                self.check_fields(message, ['id', 'username', 'email', 'password'])
                check_valid(else_mysite,message)
                else_mysite = mysite.objects.exclude(id=message["id"])
                if else_mysite.filter(username=message["username"]).exists():
                    raise Exception('username已存在')
                if else_mysite.filter(email=message["email"]).exists():
                    raise Exception('email已存在')

    def encodecontent(self,txcode):
        match txcode:
            case 'BASIC_USER_LIST_ALL':                
                return JsonResponse({"message":{'data': self.data}},safe=False)           
            case 'BASIC_USER_LIST_FILTER':                
                return JsonResponse({"message":{'data': self.data}},safe=False)
            case 'BASIC_USER_FIND_BY_USERNAME':                
                return JsonResponse({"message":{'data': self.data}},safe=False)        
            case 'BASIC_USER_INSERT':               
                return JsonResponse(self.data)
            case 'BASIC_USER_UPDATE':                
                return JsonResponse(self.data)
            
fields = mysite.objects.values('id', 'username', 'email', 'password', 'last_modify_date', 'created')

def List_All():
    return list(fields.order_by('id', 'created'))

def List_Filter(message):
    if 'username' in message and message['username']:
        result = fields.filter(username__icontains=message['username'])
    if 'email' in message and message['email']:
        result = result.filter(email__icontains=message['email'])
    return list(result.order_by('id', 'created'))

def Find_By_Username(message):
    result = fields.filter(username__icontains=message['username']).values('username')
    return list(result)

def Insert(message):
    mysite.objects.create(**message)
    return {'Insert': '新增成功'}

def Update(message):
    mysite_entry = mysite.objects.get(id=message["id"])
    for key, value in message.items():
        setattr(mysite_entry, key, value)
    mysite_entry.save()
    return {'Update': '修改成功'}

def check_valid(message):
    if not valid_string(message["username"]):
        raise Exception('username格式錯誤')
    if not valid_email(message["email"]):
        raise Exception('email格式錯誤')
    if not valid_password(message["password"]):
        raise Exception('password格式錯誤')