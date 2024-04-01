## Функциональность

- **Создание задач**: Пользователи могут создавать новые задачи, указывая название, описание и срок выполнения.
- **Просмотр списка задач**: Приложение отображает список всех существующих задач с возможностью фильтрации и сортировки.
- **Редактирование задач**: Пользователи могут изменять название, описание и срок выполнения существующих задач.
- **Выполнение задач**: Задачи можно отмечать как выполненные, что позволяет отслеживать прогресс.
- **Удаление задач**: Пользователи могут удалять ненужные задачи из списка.

## Технологии

**Бэкенд**:
- Django REST Framework (DRF) для создания API
**Фронтенд**:
- React для создания пользовательского интерфейса
- Redux для управления состоянием приложения
- Single Page Application (SPA) для обеспечения плавного пользовательского опыта. Клиент общается с сервером исключительно json файлами

## Установка и запуск

1. Клонируйте репозиторий на свой локальный компьютер.
2. Настройте и активируйте виртуальное окружение Python.
3. Установите зависимости бэкенда, выполнив `pip install -r requirements.txt` в корневой директории проекта.
4. Примените миграции базы данных:`python manage.py migrate`
3. Запустите сервер разработки:`python manage.py runserver`
