from mysite.api.UserResource import UserResource
import traceback
import sys

def txcode(txcode,message):
    cls = None
    try:
        match txcode:
            case 'BASIC_USER_LIST_ALL':
                cls = UserResource()         
            case 'BASIC_USER_LIST_FILTER':
                cls = UserResource()
            case 'BASIC_USER_FIND_BY_USERNAME':
                cls = UserResource()       
            case 'BASIC_USER_INSERT':
                cls = UserResource()
            case 'BASIC_USER_UPDATE':
                cls = UserResource()
            case _:
                raise Exception(f'無對應交易: {txcode}')
        return Transaction(cls,txcode,message)
    except Exception as e :
        traceback.print_exc(file=sys.stderr)
        raise Exception(e)

def Transaction(cls,txcode,message):
    cls.decodecontent(txcode,message) 
    cls.doTransaction(txcode,message)   
    return cls.encodecontent(txcode)             
   