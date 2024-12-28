# Используем официальный образ Python 3.12 на базе Debian slim (легкий образ)
FROM python:3.12-slim

# Устанавливаем системные зависимости:
# - curl для загрузки файлов по HTTP
# - netcat-openbsd для проверки доступности сервисов
RUN apt-get update && apt-get install -y \
    curl \                        
    netcat-openbsd \             
    && rm -rf /var/lib/apt/lists/* 
# Убираем кэш apt, чтобы уменьшить размер образа

# Устанавливаем wait-for-it.sh для ожидания, пока база данных станет доступной, прежде чем запустить приложение
RUN curl -o /usr/local/bin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it 
# Даем права на выполнение скрипта

# Устанавливаем рабочую директорию внутри контейнера на /app
WORKDIR /app

# Копируем все файлы из текущей директории (где находится Dockerfile) в /app внутри контейнера
COPY . /app

# Устанавливаем зависимости Python, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем скрипт оболочки start.sh, который будет запускать два Python-скрипта
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
# Даем права на выполнение скрипта start.sh

# Запускаем приложение только после того, как база данных будет доступна, и выполняем оба Python-скрипта (9_2 и 9_3)
CMD ["./start.sh"]
