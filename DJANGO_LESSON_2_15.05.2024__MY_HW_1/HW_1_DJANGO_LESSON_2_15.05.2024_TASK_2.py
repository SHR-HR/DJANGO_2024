import os
import subprocess
import sys


def run_command(command, env=None):
    """Выполнить команду в командной строке"""
    result = subprocess.run(command, shell=True, text=True, env=env, capture_output=True)
    if result.returncode != 0:
        print(f"Ошибка выполнения команды: {command}")
        print(result.stderr)
    else:
        print(f"Команда выполнена успешно: {command}")
        print(result.stdout)
    return result


def create_and_setup_virtualenv(env_name, django_version, project_name):
    """Создать виртуальное окружение и установить нужную версию Django"""
    run_command(f"python -m venv {env_name}")

    # Установка setuptools, чтобы избежать ошибки с distutils
    pip_install_setuptools_command = f"{env_name}\\Scripts\\python.exe -m pip install setuptools"
    run_command(pip_install_setuptools_command)

    pip_install_command = f"{env_name}\\Scripts\\python.exe -m pip install django=={django_version}"
    run_command(pip_install_command)

    startproject_command = f"{env_name}\\Scripts\\python.exe -m django startproject {project_name}"
    result = run_command(startproject_command)

    if result.returncode == 0:
        print(f"Проект {project_name} создан с Django {django_version} и виртуальным окружением {env_name}")
    else:
        print(f"Не удалось настроить проект {project_name}")


def main():
    print(f"Используемая версия Python: {sys.version}")

    # Настройка первого виртуального окружения
    print("Настройка env_django_3_2 с Django 3.2")
    create_and_setup_virtualenv("env_django_3_2", "3.2", "myproject_env_django_3_2")

    # Настройка второго виртуального окружения
    print("Настройка env_django_latest с последней версией Django")
    run_command(f"python -m venv env_django_latest")
    run_command(f"env_django_latest\\Scripts\\python.exe -m pip install django")
    result = run_command(f"env_django_latest\\Scripts\\python.exe -m django startproject myproject_env_django_latest_2")
    if result.returncode == 0:
        print(
            f"Проект myproject_env_django_latest_2 создан с последней версией Django и виртуальным окружением env_django_latest")
    else:
        print(f"Не удалось создать виртуальное окружение myproject_env_django_latest_2")

    print("Настройка завершена")


if __name__ == "__main__":
    main()

# import subprocess
# import os
#
#
# def run_command(command, env=None):
#     """ Запускает команду в подпроцессе с указанным окружением """
#     try:
#         result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True, env=env)
#         print(f"Команда выполнена успешно: {command}")
#         print(result.stdout)
#         return True
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка выполнения команды: {command}")
#         print(e.stderr)
#         return False
#
#
# def create_and_activate_venv(venv_name, django_version):
#     """ Создает и активирует виртуальное окружение, устанавливает Django """
#     if not os.path.exists(venv_name):
#         os.makedirs(venv_name)
#     if not run_command(f"python -m venv {venv_name}"):
#         return False
#     # Определяем пути для активации и для python в виртуальном окружении
#     activate_path = f"{venv_name}\\Scripts\\activate_this.py"
#     python_path = f"{venv_name}\\Scripts\\python.exe"
#     # Установка Django
#     if run_command(f"{python_path} -m pip install django=={django_version}"):
#         return python_path  # Возвращаем путь к Python в виртуальном окружении
#     return False
#
#
# def setup_django_project(venv_python, project_name):
#     """ Настройка Django проекта """
#     if run_command(f"{venv_python} -m django admin startproject {project_name}"):
#         os.chdir(project_name)  # Переходим в каталог проекта
#         if run_command(f"{venv_python} manage.py migrate"):  # Выполнение миграций
#             return run_command(f"{venv_python} manage.py runserver 0.0.0.0:8000")  # Запуск сервера
#     return False
#
#
# def main():
#     django_versions = {"env_django_3_2": "3.2", "env_django_latest": ""}
#     projects = {}
#
#     for venv, version in django_versions.items():
#         print(f"Настройка {venv} с Django {version or 'latest version'}")
#         python_exec = create_and_activate_venv(venv, version or "django")  # 'django' для последней версии
#         if python_exec:
#             projects[venv] = f"myproject_{venv}"
#             if not setup_django_project(python_exec, projects[venv]):
#                 print(f"Не удалось настроить проект {projects[venv]}")
#         else:
#             print(f"Не удалось создать виртуальное окружение {venv}")
#
#     print("Настройка завершена")
#
#
# if __name__ == "__main__":
#     main()
