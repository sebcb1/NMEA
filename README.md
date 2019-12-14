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
python3 manage.py migratemigrations api
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

Use curl to send trames:

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
docker build --no-cache -t sebcb1/nmea_web:0.2.0 .
docker login
docker push sebcb1/nmea_web:0.2.0
```

To test:

```
cd /home/sebastien/NMEA/docker
su
docker-compose run web /bin/bash
cd /app
./start.sh
```

To build docker image on RPy:

```
sudo su -
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
docker run hello-world

curl -sSL https://get.docker.com | sh
apt-get install libffi-dev libssl-dev
apt-get install docker-compose docker
git clone https://github.com/sebcb1/NMEA.git
cd ./NMEA/docker/build_nmea_web
docker build --no-cache -t sebcb1/nmea_web:0.2.0 .
docker login
docker push sebcb1/nmea_web:0.2.0
```



## Start web container docker

```
cd /home/sebastien/NMEA/docker
su
docker-compose up -d 
docker-compose logs -f web
```

## Install Raspberry Pi




### Root login:

Edit /etc/ssh/sshd_config
```
PermitRootLogin yes
```

Then:

```
/etc/init.d/ssh restart
sudo passwd root
```

### Deploy dev part on raspberry pi

git clone https://github.com/sebcb1/NMEA.git
cd NMEA
git config --global user.email "sebastienbrillard@icloud.com"
git config --global user.name "Seb"

gunzip sqlite-autoconf-3300100.tar.gz
tar xvf sqlite-autoconf-3300100.tar
cd sqlite-autoconf-3300100
./configure 
make
sudo su 
make install
exit
cd ..
rm -rf sqlite-autoconf-3300100
gzip sqlite-autoconf-3300100.tar

pip3 install Django

cd web
export LD_LIBRARY_PATH=/usr/local/lib
python3 manage.py migrate
python3 manage.py makemigrations api
python3 manage.py createsuperuser
python3 manage.py migrate

python3 manage.py runserver 0:8000

### Refresh dev part on raspberry pi


## Links

https://f-leb.developpez.com/tutoriels/arduino/esp8266/debuter/

https://www.fais-le-toi-meme.fr/fr/electronique/materiel/esp8266-arduino-wifi-2-euros
https://reso-nance.org/wiki/_detail/materiel/esp8266/esp-with-arduino-circuit.jpg?id=materiel%3Aesp8266%3Aaccueil
http://espace-raspberry-francais.fr/Debuter-sur-Raspberry-Francais/Installation-Raspbian-et-premier-demarrage-Raspberry-Pi-Francais/
https://code4pi.fr/2017/05/creer-hotspot-wifi-raspberry/
https://github.com/raspberrypi/documentation/issues/1018#ref-commit-c1e42a2
https://github.com/billz/raspap-webgui
https://www.balena.io/etcher/
https://code4pi.fr/2013/12/installation-dun-serveur-web-lighttpd/

