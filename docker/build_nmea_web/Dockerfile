FROM centos:7.7.1908
RUN yum update -y
RUN yum install git.x86_64 python3.x86_64 gcc.x86_64 wget.x86_64 make.x86_64 unzip.x86_64 -y
RUN pip3 install virtualenv
RUN mkdir /app
RUN cd /app
RUN virtualenv -p /usr/bin/python3 /app/python_venv
RUN source /app/python_venv/bin/activate
RUN pip install Django
RUN wget https://www.sqlite.org/2019/sqlite-autoconf-3300100.tar.gz
RUN gunzip sqlite-autoconf-3300100.tar.gz
RUN tar xvf sqlite-autoconf-3300100.tar
RUN cd sqlite-autoconf-3300100
RUN ./configure 
RUN make
RUN make install
RUN cd /app
RUN wget https://github.com/sebcb1/NMEA/archive/master.zip
RUN cd NMEA-master/web




source /app/python_venv/bin/activate
export LD_LIBRARY_PATH=/usr/local/lib
python manage.py runserver 0:8000