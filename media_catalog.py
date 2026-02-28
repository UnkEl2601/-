

import os
import csv

def display_catalog():
  feature/add-video
    pass

def rate_media() -> None:
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
main
