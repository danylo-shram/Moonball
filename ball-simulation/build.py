from pybuilder.core import use_plugin, init, Author, task
import os
import shutil

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")  # Перевірка стилю коду
use_plugin("python.coverage")
use_plugin("python.distutils")  # Для створення дистрибутиву
use_plugin("copy_resources")  # Для копіювання ресурсів

name = "ball-simulation"
version = "1.0.0"
default_task = ["clean", "analyze", "publish"]

authors = [Author("Студент", "student@example.com")]
license = "MIT"
summary = "Симуляція вільного падіння м'ячика з відбиттям"
url = "https://github.com/yourusername/ball-simulation"

@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_main_resources", "src/main/resources")
    project.depends_on("tkinter")
    
    # Налаштування ресурсів
    project.set_property("copy_resources_target", "$dir_dist")
    project.get_property("copy_resources_glob").append("src/main/resources/*.gif")
    
    # Налаштування flake8 (можна пропустити деякі помилки)
    project.set_property("flake8_ignore", "E501")  # Ігнорувати помилки довжини рядка
    
    # Налаштування тестування
    project.set_property("coverage_threshold_warn", 70)
    project.set_property("coverage_break_build", False)

@task
def run(project):
    """Запуск програми без створення виконуваного файлу"""
    os.system("python src/main/python/ball_simulation/ball_simulation.py")

@task
def package(project):
    """Створює виконуваний файл з проекту за допомогою PyInstaller"""
    print("Створення виконуваного файлу...")
    os.system("pyinstaller --onefile --name ball-simulation src/main/python/ball_simulation/ball_simulation.py")
    
    # Копіювання ресурсів у директорію dist
    os.makedirs("dist/resources", exist_ok=True)
    shutil.copy("src/main/resources/bg3.gif", "dist/resources/")
    print("Виконуваний файл створено в директорії dist/")

@task
def clean_all(project):
    """Повне очищення згенерованих файлів"""
    dirs_to_clean = ["dist", "build", "target", "__pycache__", ".pybuilder"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
    print("Всі згенеровані файли видалено")