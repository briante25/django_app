# 获取 Django 进程的 PID
django_pid=$(pgrep -f "python manage.py runserver")

while true; do
    # 检测 Django 进程是否存在
    if ! ps -p $django_pid > /dev/null; then
        
        
        # 获取 Celery 进程的 PID
        celery_pid=$(pgrep -f "celery -A django1 beat")

        # 关闭 Celery 进程
        if [ -n "$celery_pid" ]; then
            echo "Stopping Celery process"
            kill -TERM $celery_pid
        
        fi

        break
    fi

    # 等待 30 秒后再次检测
    sleep 30
done
