# Телеграм-бот DZ_TG04_BOT (ДЗ к уроку TG04)

## Описание

@DZ_TG04_BOT — это ваш гид по меню с кнопками и динамическим взаимодействием. Бот предоставляет пользователям простой интерфейс для общения и получения полезных ссылок. Используйте команды `/start` для приветствия, `/links` для получения ссылок на новости, музыку и видео, и `/dynamic` для динамического меню.

## Установка и настройка

1. **Клонирование репозитория**

   ```bash
   git clone https://github.com/yourusername/dz_tg04_bot.git
   cd dz_tg04_bot
   ```

2. **Создание виртуального окружения и установка зависимостей**

   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows используйте `venv\\Scripts\\activate`
   pip install -r requirements.txt
   ```

3. **Настройка переменных окружения**

   - Создайте файл `.env` в корне проекта и добавьте ваш токен телеграм-бота:

     ```
     TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
     ```

4. **Запуск бота**

   ```bash
   python main_TG04.py
   ```

## Использование

### Команды

- `/start` — Запускает бота и показывает меню с кнопками "Привет" и "Пока".
- `/links` — Отображает инлайн-кнопки с URL-ссылками на новости, музыку и видео.
- `/dynamic` — Показывает инлайн-кнопку "Показать больше", которая при нажатии заменяется на "Опция 1" и "Опция 2".

### Поведение бота

- **Приветствие и прощание**: При нажатии на кнопку "Привет" бот отвечает "Привет, {имя пользователя}!", а при нажатии на кнопку "Пока" — "До свидания, {имя пользователя}!".
- **Ссылки**: Команда `/links` выводит кнопки с ссылками на популярные ресурсы.
- **Динамическое меню**: Команда `/dynamic` показывает кнопку "Показать больше", которая заменяется на две новые кнопки — "Опция 1" и "Опция 2". При выборе одной из них бот сообщает о выбранной опции.

## Зависимости

- Python 3.12+
- aiogram 3.15.0
- python-dotenv

Установите все необходимые зависимости с помощью команды `pip install -r requirements.txt`.

## Логирование

Бот использует стандартную библиотеку `logging` для ведения журнала событий. Логи отображаются в консоли для удобства отладки и мониторинга.

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с разработчиком по адресу электронной почты: [6202818@gmail.com](mailto:6202818@gmail.com).

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле `LICENSE`.
