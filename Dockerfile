FROM python:2.7
MAINTAINER 周琪 <zhouqi@benditoutiao.com>



WORKDIR /app

COPY . .
RUN apt update && apt install sqlite3 -y && \
  pip install -r requirements.txt --index-url=http://pypi.douban.com/simple --trusted-host=pypi.douban.com && \
  pip install pillow --index-url=http://pypi.douban.com/simple --trusted-host=pypi.douban.com && \
  pip install xadmin --index-url=http://pypi.douban.com/simple --trusted-host=pypi.douban.com && \
  pip uninstall xadmin -y


EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
