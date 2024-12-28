#!/bin/bash
# shell script для последовательного запуска нескольких приложений


# Запуск listing_9_2.py
echo "Запуск listing_9_2.py..."
python3 listing_9_2.py

# Проверка успешного выполнения listing_9_2.py
if [ $? -eq 0 ]; then
    echo "listing_9_2.py завершен успешно."
else
    echo "listing_9_2.py завершен с ошибкой!"
    exit 1
fi

# Запуск listing_9_3.py
echo "Запуск listing_9_3.py..."
python3 listing_9_3.py

# Проверка успешного выполнения listing_9_3.py
if [ $? -eq 0 ]; then
    echo "listing_9_3.py завершен успешно."
else
    echo "listing_9_3.py завершен с ошибкой!"
    exit 1
fi
