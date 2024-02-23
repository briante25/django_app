class RestResourceBase:
    def __init__(self):
        self.data = None
    
    def doTransaction(self,txcode,message):
        pass
                       
    def decodecontent(self,txcode,message):
        pass

    def encodecontent(self,txcode):
        pass

    def check_fields(self,message,fields):
        error=[]
        for field in fields:
            if field not in message:
                error.append(field)
        if error:
            raise Exception(f'缺少{error}')