#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Media Catalog - программа для каталогизации личной медиатеки
Автор: Студент 1 (владелец)
Задача #1: Базовая структура и отображение каталога
"""

# Глобальный каталог для хранения элементов
catalog = []


def display_catalog():
    """Отображение всех элементов каталога"""
    if not catalog:
        print("\n📁 Каталог пуст. Добавьте первый элемент!")
        return
    
    print("\n" + "="*60)
    print("📀 ТЕКУЩИЙ КАТАЛОГ")
    print("="*60)
    
    for i, item in enumerate(catalog, 1):
        status_icon = "✅" if item.get('status') == "Просмотрено" else "⏳"
        rating_display = f"⭐ {item['rating']}/10" if item.get('rating') else "❌ не оценено"
        
        print(f"{i}. {status_icon} {item['title']} ({item['year']})")
        print(f"   Жанр: {item['genre']} | Тип: {item['type']} | {rating_display}")
    
    print("="*60)


def main_menu():
    """Главное меню приложения"""
    while True:
        print("\n" + "📀 MEDIA CATALOG".center(60))
        print("="*60)
        print("1. Показать каталог")
        print("2. Добавить элемент")
        print("3. Оценить элемент")
        print("4. Импорт из CSV")
        print("5. Сохранить в CSV")
        print("0. Выход")
        print("="*60)
        
        choice = input("Выберите действие (0-5): ").strip()
        
        if choice == '1':
            display_catalog()
        elif choice == '2':
            print("🔜 Функция добавления в разработке (задача студента 2)")
        elif choice == '3':
            print("🔜 Функция оценки в разработке (задача студента 3)")
        elif choice == '4':
            print("🔜 Импорт CSV в разработке (задача студента 3)")
        elif choice == '5':
            print("🔜 Сохранение CSV в разработке (задача студента 3)")
        elif choice == '0':
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")
        
        input("\nНажмите Enter для продолжения...")


# ========== ТОЧКА ВХОДА ==========
if __name__ == "__main__":
    # Добавим несколько примеров для демонстрации
    example_items = [
        {
            'title': 'Матрица', 
            'year': 1999, 
            'genre': 'Sci-Fi', 
            'type': 'фильм', 
            'status': 'Просмотрено', 
            'rating': 10
        },
        {
            'title': 'Властелин колец', 
            'year': 1954, 
            'genre': 'Фэнтези', 
            'type': 'книга', 
            'status': 'В планах', 
            'rating': None
        },
        {
            'title': 'The Witcher 3', 
            'year': 2015, 
            'genre': 'RPG', 
            'type': 'игра', 
            'status': 'Просмотрено', 
            'rating': 9
        }
    ]
    
    for item in example_items:
        catalog.append(item)
    
    print("🎬 Добро пожаловать в Media Catalog!")
    print(f"📊 В каталоге {len(catalog)} примеров для демонстрации")
    
    main_menu()