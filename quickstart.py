import os
import subprocess
import shutil

def create_django_project(project_name):
    subprocess.run(['django-admin', 'startproject', project_name])

def add_app_to_installed_apps(project_name, app_name):
    settings_path = f'{project_name}/{project_name}/settings.py'
    
    # Read the content of settings.py
    with open(settings_path, 'r') as f:
        lines = f.readlines()
    
    # Find the line where INSTALLED_APPS is defined
    for i, line in enumerate(lines):
        if line.startswith('INSTALLED_APPS = ['):
            # Add the new app to the INSTALLED_APPS list
            lines[i] = line.rstrip() + f"\n    '{app_name}',\n"
            break
    
    # Write the modified content back to settings.py
    with open(settings_path, 'w') as f:
        f.writelines(lines)


def create_django_app(project_name, app_name):
    # Set the current working directory to the project directory
    project_dir = os.path.join(os.getcwd(), project_name)

    # Change to the project directory and run the startapp command
    subprocess.run(['python', 'manage.py', 'startapp', app_name], cwd=project_dir)

def configure_project_url_routing(project_name, app_name):
    urls_path = f'{project_name}/{project_name}/urls.py'
    with open(urls_path, 'w') as urls_file:
        urls_file.write("from django.contrib import admin\nfrom django.urls import include, path\n\n")
        urls_file.write("urlpatterns = [\n    path('admin/', admin.site.urls),\n    ")
        urls_file.write(f'path("", include("{app_name}.urls")),\n]')

def configure_app_url_routing(project_name, app_name):
    urls_path = f'{project_name}/{app_name}/urls.py'
    content = """
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]"""
    with open(urls_path, 'w') as urls_file:
        urls_file.write(content)


def create_home_view(project_name, app_name):
    views_path = f'{project_name}/{app_name}/views.py'
    views_content = """
from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, '""" + app_name + "/home.html')"

    with open(views_path, 'w') as views_file:
        views_file.write(views_content)

def create_template_directory(project_name, app_name):
    app_dir = f'{project_name}/{app_name}'
    templates_dir = f'{project_name}/{app_name}/templates'

    # Change to the project directory and run the startapp command
    subprocess.run(['mkdir', 'templates'], cwd=app_dir)
    subprocess.run(['mkdir', app_name], cwd=templates_dir)

def create_home_template(project_name, app_name):
    templates_path = f'{project_name}/{app_name}/templates/{app_name}/home.html'
    template_content = """
<!DOCTYPE html>
<html>
    <body>
        <h2>This is the home page</h2>
        <p>This software is broken</p>
    </body>
</html>
"""
    with open(templates_path, 'w') as template_file:
        template_file.write(template_content)

if __name__ == '__main__':
    project_name = 'test_project'
    app_name = 'test_app'
    create_django_project(project_name)
    create_django_app(project_name, app_name)
    add_app_to_installed_apps(project_name, app_name)
    configure_project_url_routing(project_name, app_name)
    configure_app_url_routing(project_name, app_name)
    create_home_view(project_name, app_name)
    create_template_directory(project_name, app_name)
    create_home_template(project_name, app_name)