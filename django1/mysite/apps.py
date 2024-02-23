from django.apps import AppConfig
from subprocess import Popen, PIPE
import sys,atexit,os,json 
from django.db import connections
from psycopg2 import OperationalError
from django.db import connections
from django.core.exceptions import ValidationError
from mysite.report.jasperreport import generate_report
from django.test import Client

class MysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite'

    def ready(self):        
        # 檢查是否是主進程（不在autoreload期間的子進程中）
        if 'runserver' in sys.argv and os.environ.get("RUN_MAIN") == "true":
            print('排程啟動中...')
            self.start_celery_beat()
            print("資料庫連接測試中...")
            self.check_postgresql()
            print('API功能測試中...')
            self.check_api()
            print('PDF功能測試中...')
            path_pdf = self.check_pdf()
            print('郵件發送功能測試中...')           
            self.check_email('41041124@gm.nfu.edu.tw',path_pdf)
        
    def start_celery_beat(self):
        celery_command = f"celery -A django1 beat -l info"
        beat_process = Popen(celery_command, shell=True, stdin=None, stdout=PIPE, stderr=PIPE)
        print('排程啟動程序...OK')
        # 註冊一個關閉處理程序，以確保退出時停止 Celery Beat
        def close_beat():
            beat_process.terminate()
            beat_process.wait()    
        atexit.register(close_beat)

    def check_postgresql(self):
        try:
            # 嘗試使用psycopg2連接PostgreSQL資料庫
            connection = connections['default']
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')
        except OperationalError:
            # 如果連接失敗，輸出錯誤信息
            print("!無法連接到資料庫,請檢查配置...")
        else:
            # 連接成功，可以進行進一步的初始化操作
            print("成功連接到資料庫...OK")

    def check_api(self):
        try:
            client = Client()
            data = {
                "header":{
                    "txcode":"BASIC_USER_LIST_ALL"
                },
                "message":{
                }
            } 
            data = json.dumps(data)          
            response = client.post('/testapi/',data,content_type= 'application/json')
            # 如果響應狀態碼在2xx範圍內，視為API連接成功
            if response.status_code == 200:
                print("API連接成功...OK")
            else:
                print(f"API連接失敗:{response.content.decode('utf-8')}")
        except Exception as e:
                # 處理其他連接錯誤或異常
                print(f"API連接失敗:{str(e)}")

    def check_pdf(self):
        try:
            path_pdf = generate_report()
            print('PDF功能測試...OK')
            return path_pdf
        except RuntimeError as e:
            print(f'PDF功能測試...失敗: {e}')

    def check_email(self,user_email,path_pdf):
        try:
            from mysite.mail.mailtest import send_email_to_user
            # 寄送測試郵件
            send_email_to_user(user_email,'已啟動伺服器！','郵件發送功能測試...',path_pdf)        
            print('郵件發送功能測試...OK')
        except ValidationError as e:
            # 處理驗證錯誤
            print(f'!郵件發送失敗: {e}')
        except Exception as e:
            # 處理其他異常情況
            print(f'!郵件發送失敗: {e}')