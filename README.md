- Project Start
    ```python -m venv venv```
    ```venv\Scripts\activate```
    ```pip install django```
    ```django-admin startproject news_app .```
    ```python manage.py runserver```
    ```django-admin startapp home``` > needs to be added into /news_app/settings.py under INSTALLED_APPS


- Migrations : DB changes 
    ```python manage.py migrate```  
    ```python manage.py createsuperuser```  > admin/admin (To change in prod release)


Linode     
#Alejo1991tb