@echo off
chcp 65001
echo Создаем виртуальное окружение...
python -m venv myenv

echo Активируем виртуальное окружение...
call myenv\Scripts\activate

echo Устанавливаем зависимости из файла requirements.txt...
pip install -r requirements.txt

echo Создаем новый проект Django, если он не существует...
if not exist myproject (django-admin startproject myproject)

cd myproject

echo Создаем новое приложение, если оно не существует...
if not exist newapp (python manage.py startapp newapp)

echo Применяем миграции...
python manage.py migrate

echo Замораживаем зависимости...
pip freeze > ..\requirements_freeze.txt

echo Запускаем Django сервер...
python manage.py runserver

cd ..

echo Деактивируем виртуальное окружение...
call myenv\Scripts\deactivate

echo Проект создан и зависимости установлены!
pause
