import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from alphabet_cipher import AlphabetCipher
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

class AlphabetHistogram:
    def __init__(self):
        self.cipher = AlphabetCipher()
        # Алфавит в правильном порядке (32 символа)
        self.alphabet = ['_', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 
                         'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    
    def generate_hashes(self, seed, count=10000):
        """Генерирует цепочку хеш-значений."""
        print(f"Генерация {count} хеш-значений...")
        hashes = []
        current = seed
        for i in range(count):
            hash_value = self.cipher.SpongeFun_hash(current)
            hashes.append(hash_value)
            current = hash_value[:16]
            
            if (i + 1) % 2000 == 0:
                print(f"  Сгенерировано {i + 1} хешей...")
        
        print(f"  Готово! Всего {len(hashes)} хешей, длина каждого: {len(hashes[0])} символов")
        return hashes
    
    def analyze_position(self, hashes, position):
        """Анализирует частоту символов на заданной позиции."""
        symbols = []
        for h in hashes:
            if len(h) > position:
                symbols.append(h[position])
        return Counter(symbols)
    
    def plot_histogram(self, counter, position, total_hashes, filename):
        """Создаёт и сохраняет гистограмму для одной позиции."""
        
        # Подготавливаем данные
        frequencies = [counter.get(sym, 0) for sym in self.alphabet]
        
        # Переводим в тысячи
        frequencies_k = [f / 1000 for f in frequencies]
        
        # Создаём фигуру
        fig, ax = plt.subplots(figsize=(18, 8))
        
        # Цвета: градиент от синего к фиолетовому
        colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(self.alphabet)))
        
        # Строим столбцы
        bars = ax.bar(range(len(self.alphabet)), frequencies_k, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Ожидаемая частота в тысячах (при равномерном распределении)
        expected_freq_k = total_hashes / 32 / 1000
        ax.axhline(y=expected_freq_k, color='red', linestyle='--', linewidth=2, 
                   label=f'Ожидаемая частота ({expected_freq_k:.2f}k)')
        
        # Настройка осей
        ax.set_xlabel('Символы алфавита', fontsize=14, fontweight='bold')
        ax.set_ylabel('Частота появления (тыс.)', fontsize=14, fontweight='bold')
        ax.set_title(f'Распределение символов на позиции {position}\n(всего хешей: {total_hashes:,})', 
                     fontsize=16, fontweight='bold')
        
        # Подписи символов на оси X
        ax.set_xticks(range(len(self.alphabet)))
        ax.set_xticklabels(self.alphabet, fontsize=10, rotation=45, ha='right')
        
        # Добавляем значения на столбцы (только если значение больше 0)
        for i, (bar, freq_k) in enumerate(zip(bars, frequencies_k)):
            if freq_k > 0:
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                       f'{freq_k:.2f}', ha='center', va='bottom', fontsize=8, rotation=90)
        
        # Статистика
        unique = len([f for f in frequencies if f > 0])
        coverage = unique / 32 * 100
        max_freq_k = max(frequencies_k)
        min_freq_k = min([f for f in frequencies_k if f > 0])
        
        # Добавляем текст со статистикой в правый верхний угол
        stats_text = f'Уникальных символов: {unique}/32 ({coverage:.1f}%)\n'
        stats_text += f'Максимальная частота: {max_freq_k:.2f}k\n'
        stats_text += f'Минимальная частота: {min_freq_k:.2f}k'
        
        ax.text(0.98, 0.97, stats_text, transform=ax.transAxes, fontsize=11,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))
        
        # Легенда
        ax.legend(loc='upper left')
        
        # Сетка
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        # Устанавливаем пределы Y с небольшим запасом
        y_max = max(frequencies_k) + 2
        ax.set_ylim(0, y_max)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"  Гистограмма сохранена: {filename}")
        
        return {
            'unique': unique,
            'coverage': coverage,
            'max_freq_k': max_freq_k,
            'min_freq_k': min_freq_k,
            'expected_freq_k': expected_freq_k
        }
    
    def run(self, seed="ХОРОШО_БЫТЬ_ВАМИ", num_hashes=10000, positions=[0, 31]):
        """Запускает анализ и создаёт две одинаковые гистограммы."""
        
        print("=" * 60)
        print("ГИСТОГРАММА РАСПРЕДЕЛЕНИЯ СИМВОЛОВ ПО ПОЗИЦИЯМ")
        print("=" * 60)
        
        # Генерируем хеши
        hashes = self.generate_hashes(seed, num_hashes)
        
        # Анализируем каждую позицию и создаём гистограммы
        results = {}
        for pos in positions:
            print(f"\nАнализ позиции {pos}...")
            counter = self.analyze_position(hashes, pos)
            filename = f"histogram_position_{pos}.png"
            results[pos] = self.plot_histogram(counter, pos, num_hashes, filename)
        
        # Вывод результатов
        print("\n" + "=" * 60)
        print("РЕЗУЛЬТАТЫ")
        print("=" * 60)
        
        for pos in positions:
            print(f"\nПозиция {pos}:")
            print(f"  Уникальных символов: {results[pos]['unique']}/32 ({results[pos]['coverage']:.1f}%)")
            print(f"  Максимальная частота: {results[pos]['max_freq_k']:.2f}k")
            print(f"  Минимальная частота: {results[pos]['min_freq_k']:.2f}k")
            print(f"  Ожидаемая частота:   {results[pos]['expected_freq_k']:.2f}k")
        
        print("\n" + "=" * 60)
        print("СОЗДАННЫЕ ФАЙЛЫ:")
        for pos in positions:
            print(f"  - histogram_position_{pos}.png")
        print("=" * 60)


if __name__ == '__main__':
    # Создаём гистограммы для позиций 0 и 31
    # Для полного анализа используйте num_hashes=10000
    histogram = AlphabetHistogram()
    histogram.run("ХОРОШО_БЫТЬ_ВАМИ", num_hashes=10000, positions=[0, 31])