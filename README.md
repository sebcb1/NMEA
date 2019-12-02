# NMEA

## Install a new dev erver

```
yum install ansible.noarch
ansible-playbook install_dev_server.yml
```

## Init repositoy

To init repo after creating initial repo on github:

```
git clone https://github.com/sebcb1/NMEA.git
cd NMEA
git config --global user.email "sebastienbrillard@icloud.com"
git config --global user.name "Seb"
virtualenv -p /usr/bin/python3 python_venv
source python_venv/bin/activate
pip install Django
echo "python_venv/*" >.gitignore
echo "*.pyc" >>.gitignore
echo "*.sqlite3" >>.gitignore
git add .gitignore
wget https://www.sqlite.org/2019/sqlite-autoconf-3300100.tar.gz
gunzip sqlite-autoconf-3300100.tar.gz
tar xvf sqlite-autoconf-3300100.tar
cd sqlite-autoconf-3300100
./configure 
make
su
make install
gzip sqlite-autoconf-3300100.tar
echo "sqlite-autoconf-3300100/*" >> .gitignore
git add sqlite-autoconf-3300100.tar.gz

django-admin startproject web
python manage.py migrate
python manage.py createsuperuser
git add web
cd web
vi ./web/settings.py
	ALLOWED_HOSTS = ['*']
export LD_LIBRARY_PATH=/usr/local/lib
python manage.py runserver 0:8000



see: http://192.168.56.10:8000

deactivate


cd ~/NMEA
git commit -m "update" -a
git push
```

## Start webserver

To start the web server:

```
cd NMEA
source python_venv/bin/activate
export LD_LIBRARY_PATH=/usr/local/lib
cd web
python manage.py runserver 0:8000
```

To update db if necessary:

```
python manage.py makemigrations
python manage.py migrate
```

Then connect on http://192.168.56.10:8000/admin/

## Send trame

Use curl to send trame:

```
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INZDA,163115,14,06,2008,-05,00*78
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INMTW,19.8,C*14
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$PSMT,0,0,0,2,appver,0*28
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INDPT,8.9,0.0*46
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INHDG,0.0,0.0,$INHDT,0.0,T*25
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INRMC,163116,A,5040.9533,N,00103.1228,W,4.9,0.0,140608,1.1,W*64
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$PSMT,0,0,0,2,appver,0*28
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INDPT,8.7,0.0*48
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INHDG,0.0,0.0,$INHDT,0.0,T*25
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INGLL,5040.9561,N,00103.1228,W,163118,A*25
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INVTG,0.0,T,1.1,M,4.9,N,9.0,K*5A
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INMTW,20.0,C*16
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$PSMT,0,0,0,2,appver,0*28
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INDPT,8.7,0.0*48
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INHDG,0.0,0.0,$INHDT,0.0,T*25
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INRMC,163118,A,5040.9561,N,00103.1228,W,4.9,0.0,140608,1.1,W*6D
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$PSMT,0,0,0,2,appver,0*28
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INDPT,8.6,0.0*49
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INHDG,0.0,0.0,$INHDT,0.0,T*25
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INGGA,163119,5040.9574,N,00103.1228,W,2,,1.0,330.0,M,,,,*19
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INZDA,163119,14,06,2008,-05,00*74
curl -X POST  http://192.168.56.10:8000/api/trames?content=\$INMTW,20.1,C*17
```

## Build docker image

To build docker image on x86:

```
cd /home/sebastien/NMEA/docker/build_nmea_web
su
docker build -t sebcb1/nmea_web:0.1.0 .
docker login
docker push sebcb1/nmea_web:0.1.0
```
