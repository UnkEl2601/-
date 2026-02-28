#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Media Catalog - программа для каталогизации личной медиатеки
Автор: Студент 3
Задача #3: Оценки и работа с CSV
"""

import os
import csv

# Глобальный каталог (будет заполнен из main)
catalog = []


def display_catalog():
    """Отображение всех элементов каталога (функция студента 1)"""
    # Эта функция уже должна быть в файле от студента 1
    pass


def rate_media() -> None:
    """Добавление оценки к элементу каталога"""
    if not catalog:
        print("\n📁 Каталог пуст. Нечего оценивать!")
        return

    display_catalog()

    try:
        idx = int(input("\nВведите номер элемента для оценки: ")) - 1
        if idx < 0 or idx >= len(catalog):
            print("❌ Неверный номер!")
            return
        
        rating = int(input("Введите оценку (1-10): "))
        if rating < 1 or rating > 10:
            print("❌ Оценка должна быть от 1 до 10!")
            return
        
        catalog[idx]['rating'] = rating
        print(f"✅ Оценка {rating} добавлена к '{catalog[idx]['title']}'!")
        
    except ValueError:
        print("❌ Введите корректное число!")


def import_from_csv(filename: str) -> None:
    """Импорт данных из CSV файла"""
    if not os.path.exists(filename):
        print(f"❌ Файл {filename} не найден!")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                # Конвертация строк в нужные типы
                item = {
                    'title': row['title'],
                    'year': int(row['year']),
                    'genre': row['genre'],
                    'type': row['type'],
                    'status': row['status'],
                    'rating': int(row['rating']) if row['rating'] else None
                }
                catalog.append(item)
                count += 1
        
        print(f"✅ Импортировано {count} элементов из {filename}")
        
    except Exception as e:
        print(f"❌ Ошибка при импорте: {e}")


def save_to_csv(filename: str) -> None:
    """Сохранение каталога в CSV файл"""
    if not catalog:
        print("📁 Каталог пуст. Нечего сохранять!")
        return

    try:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['title', 'year', 'genre', 'type', 'status', 'rating']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            for item in catalog:
                writer.writerow(item)
        
        print(f"✅ Каталог сохранен в {filename} ({len(catalog)} элементов)")
        
    except Exception as e:
        print(f"❌ Ошибка при сохранении: {e}")