import subprocess
from django.http import HttpResponse, HttpResponseServerError
import os

# 將 'jasperstarter' 所在的整個 'bin' 目錄添加到 PATH
os.environ['PATH'] = '/home/briante/demo/jasperstarter/bin:' + os.environ['PATH']

def generate_report():
    # 指定jrxml文件的路徑
    jrxml_path = '/home/briante/demo/django1/mysite/report/Blank_A4_3.jrxml'

    # 指定生成的PDF文件的路徑和名稱（刪除.pdf擴展名）
    pdf_output_path = '/home/briante/Downloads/output'

    # 設置參數（如果有的話）
    # params = {
    #     'param1': 'value1',
    #     'param2': 'value2',
    #     # 添加任何其他參數
    # }

    # 構建JasperReports命令
    jasper_cmd = [
        '/home/briante/demo/jasperstarter/bin/jasperstarter',
        'pr',  # 使用 'pr' 命令來處理報告
        jrxml_path,
        '-o', pdf_output_path,
        '-f', 'pdf',
        '-t','postgres',
        '-H','aiot0616.antnex.com.tw',
        '-u', 'djangoapi',
        '-p', 'djangoapi@innostar.com',
        '-n', 'djangodb',
        '--db-port', '15432',
        '--db-driver','org.postgresql.Driver',
        '--db-url','jdbc:postgresql://aiot0616.antnex.com.tw:15432/djangodb',
        '--jdbc-dir','/home/briante/demo/jasperstarter/jdbc',
        '--data-file', '/home/briante/demo/django1/mysite/report/query-file.sql',
    ]

    # 添加參數
    # for key, value in params.items():
    #     jasper_cmd.extend(['-P', f'{key}={value}'])

    # 執行命令
    result = subprocess.run(jasper_cmd)
    if result.returncode == 0:
        # Report generated successfully
        return pdf_output_path + '.pdf'
    else:
        # Report generation failed
        raise RuntimeError("Error: Report generation failed.")
    
# 將生成的PDF文件返回給用戶    
def return_report_pdf(request):
    try:
        pdf_output_path = generate_report()

        with open(pdf_output_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="output.pdf"'
            return response
    except FileNotFoundError:
        return HttpResponse("Error: Report file not found.", status=500)
    except RuntimeError as e:
        return HttpResponseServerError(str(e), status=500)
    