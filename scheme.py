import matplotlib.pyplot as plt

# Координаты пунктов (подобраны так, чтобы повторить конфигурацию сети из учебника)
points = {
    'O': (0, 4),
    'Q': (0, 0),
    'T': (12, 0),
    'S': (12, 4),
    'P1': (3, 2.5),
    'P2': (7, 1.2),
    'P3': (9, 3)
}

fig, ax = plt.subplots(figsize=(10, 6))

# Соединяем линии для образования треугольников
lines = [
    ('O', 'Q'), ('Q', 'P1'), ('P1', 'O'),  # Треугольник 1
    ('Q', 'P2'), ('P2', 'P1'),             # Треугольник 2
    ('P1', 'P2'), ('P2', 'P3'), ('P3', 'P1'), # Треугольник 3 (центральный)
    ('P2', 'T'), ('T', 'P3'), ('P3', 'P2'), # Треугольник 4
    ('T', 'S'), ('S', 'P3'), ('P3', 'T'),  # Треугольник 5
    ('O', 'P1'), ('P1', 'P3'), ('P3', 'S'), # Верхние связи
    ('O', 'Q'), ('Q', 'P1'), ('O', 'S'), ('S', 'T')
]

# Чтобы не было дублей линий, создаем уникальные отрезки
unique_lines = set(tuple(sorted(line)) for line in lines)

for p1, p2 in unique_lines:
    x_values = [points[p1][0], points[p2][0]]
    y_values = [points[p1][1], points[p2][1]]
    ax.plot(x_values, y_values, color='black', linewidth=1.5)

# Пунктирная ходовая линия (O -> P1 -> P2 -> P3 -> T)
path_x = [points['O'][0], points['P1'][0], points['P2'][0], points['P3'][0], points['T'][0]]
path_y = [points['O'][1], points['P1'][1], points['P2'][1], points['P3'][1], points['T'][1]]
ax.plot(path_x, path_y, color='gray', linestyle='--', linewidth=1.2, alpha=0.7)

# Рисуем точки и подписываем их
for name, (x, y) in points.items():
    ax.plot(x, y, 'ko', markersize=5)
    if name == 'P1':
        ax.text(x, y + 0.2, name, fontsize=12, ha='center', va='bottom', fontweight='bold')
    else:
        ax.text(x, y + 0.2, name, fontsize=12, ha='center', va='bottom', fontweight='bold')

# Добавляем номера треугольников (I, II, III, IV, V)
ax.text(1.5, 1.8, 'I', fontsize=12, style='italic')
ax.text(5, 1.0, 'II', fontsize=12, style='italic')
ax.text(8, 2.0, 'III', fontsize=12, style='italic')
ax.text(10, 1.0, 'IV', fontsize=12, style='italic')
ax.text(10, 3.2, 'V', fontsize=12, style='italic')

# Настройки отображения
ax.set_aspect('equal')
ax.axis('off') # Убираем оси координат
plt.title('Схема сети триангуляции (цепи треугольников)', fontsize=14)

# Сохраняем файлы
plt.savefig('scheme.png', dpi=300, bbox_inches='tight', transparent=False, facecolor='white')
plt.savefig('scheme.pdf', bbox_inches='tight', facecolor='white')

print("Готово! Файлы scheme.png и scheme.pdf созданы.")
