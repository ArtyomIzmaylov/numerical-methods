import pandas as pd

data = {
    "Наименование продуктов": ["Пирожки", "Молоко (1 л)", "Хлеб (1 батон)", "Сыр «Российский» (1 кг)", "Говядина (1 кг)", "Картофель (1 кг)"],
    "Княжеское": [None, 48, 34, 240, 370, 22],
    "Васильево": [None, 45, 32, 280, 400, 16],
    "Рябиновка": [None, 50, 33, 270, 380, 28],
    None: [None, 52, 28, 260, 420, 30]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Сохранение в Excel файл
file_path = 'prices.xlsx'
df.to_excel(file_path, index=False)

file_path
