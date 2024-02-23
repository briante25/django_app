import json,traceback,sys
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from mysite.api.txcode import txcode

@csrf_exempt
def apitest(request):
    if request.method == 'POST':
        try:
            # 從請求主體中讀取JSON數據
            json_data = json.loads(request.body.decode('utf-8'))            
            # 調用 .txcode 模塊中的 check 函數                        
            return check(json_data)          
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)       
        except Exception as e:
            return JsonResponse({'error':str(e)},status=400)        
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)
    
def check(data):
    header=data["header"]
    message=data["message"]
    try:
        if 'txcode' in header:
            return txcode(header["txcode"],message)
        else:
            raise Exception('缺少txcode')
    except Exception as e :
        traceback.print_exc(file=sys.stderr)
        raise Exception(e)

