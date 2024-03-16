1. **Заклоньте проект с моего репозитория:**
    ```bash
        git clone <ссылка на репозиторий>
    ```
2. **Создайте env и пропишите название бд:**
    DB_NAME=<название бд>
3. **Создайте виртуальное окружение:**
     ```bash
        python3 -m venv venv
    ```
4. **Скачайте зависимости:**
     ```bash
        pip install -r requirements.txt
    ```
5. **Создайте суперюзера:**
     ```bash
        ./manage.py createsuperuser
    ```

6. **Запустите проект:**
      ```bash
        ./manage.py runserver
    ```


