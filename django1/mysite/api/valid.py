import re

def valid_email(email):
    # 定義正則表達式，檢查信箱格式
    regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+$'

    # 使用 re.match() 方法檢查信箱格式
    match = re.match(regex_pattern, email)

    # 如果匹配成功，返回 True；否則返回 False
    return bool(match)
    
def valid_string(input):
    # 定義正則表達式，確保只包含中英文字母和數字
    regex_pattern = r'^[a-zA-Z0-9\u4e00-\u9fa5]+$'

    # 使用 re.match() 方法檢查字符串格式
    match = re.match(regex_pattern, input)

    # 如果匹配成功，返回 True；否則返回 False
    return bool(match)

def valid_password(input):
    # 定義正則表達式，確保只包含中英文字母和數字
    regex_pattern = r'^[a-zA-Z0-9]+$'

    # 使用 re.match() 方法檢查字符串格式
    match = re.match(regex_pattern, input)

    # 如果匹配成功，返回 True；否則返回 False
    return bool(match)