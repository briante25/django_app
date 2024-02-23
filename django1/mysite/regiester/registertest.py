from django.shortcuts import render, redirect
from mysite.models import mysite 
from mysite.api.api import check
import json

def register_user(request):
    if request.method == 'POST':
        # 獲取表單數據
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        txcode = 'BASIC_USER_INSERT'
        data = {
                    "header":{
                        "txcode": txcode
                    }
                    ,
                    "message":{
                        "username": username,
                        "email" : email,
                        "password" : password,
                    }    
                }

        error_message = json.loads(check(data).content.decode('unicode-escape'))
        error_message = error_message.get('error', '')
        if error_message:
            return render(request, 'registration/register.html', {'error': error_message}) 
        
        # 在這裡可以發送歡迎郵件或其他後續處理
        send_welcome_email(email)

        return redirect('success')  # 定向到成功頁面或其他頁面
    else:
        return render(request, 'registration/register.html')

def success_view(request):
    # 在這裡處理成功註冊後的行為
    return render(request, 'registration/success.html')



from django.core.mail import send_mail

# 發送歡迎郵件的功能
def send_welcome_email(user_email):
    # 寄送歡迎郵件
    send_mail(
        '歡迎加入我們！',  # 郵件標題
        '感謝您的註冊，歡迎加入我們的網站！',  # 郵件內容
        '41041118@gm.nfu.edu.tw',  # 寄件人郵件地址
        [user_email],  # 收件人郵件地址（這裡使用註冊的新用戶郵件地址）
        fail_silently=False,
    )