# NMEA

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

## Install a new server

```
yum install ansible.noarch
ansible-playbook install_dev_server.yml
```