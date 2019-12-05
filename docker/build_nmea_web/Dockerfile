FROM centos:7.7.1908

# OS part
RUN yum update -y
RUN yum install git.x86_64 python3.x86_64 gcc.x86_64 wget.x86_64 make.x86_64 unzip.x86_64 -y
#RUN pip3 install virtualenv
RUN mkdir /app

# Python lib
#RUN virtualenv -p /usr/bin/python3 /app/python_venv
#RUN source /app/python_venv/bin/activate & pip3 install Django
RUN pip3 install Django

# Get SQLite
WORKDIR /app
RUN wget https://www.sqlite.org/2019/sqlite-autoconf-3300100.tar.gz
RUN gunzip sqlite-autoconf-3300100.tar.gz
RUN tar xvf sqlite-autoconf-3300100.tar
WORKDIR /app/sqlite-autoconf-3300100
RUN ./configure 
RUN make
RUN make install

# Get NMEA Django site
WORKDIR /app
RUN wget https://github.com/sebcb1/NMEA/archive/master.zip
RUN unzip master.zip
WORKDIR /app/NMEA-master/web

# Initialize website
ENV LD_LIBRARY_PATH=/usr/local/lib
RUN python3 manage.py migrate
RUN python3 manage.py makemigrations api
RUN python3 manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python3 manage.py shell
COPY start.sh /app
RUN chmod u+x /app/start.sh
ENTRYPOINT  ["/app/start.sh"]

EXPOSE 8000

