import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from alphabet_cipher import AlphabetCipher
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # Бэкенд без GUI (для сохранения в файл)
import matplotlib.pyplot as plt
import numpy as np

class PositionHistogramPlot:
    def __init__(self):
        self.cipher = AlphabetCipher()
        # Алфавит в правильном порядке
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
        
        # Создаём фигуру
        fig, ax = plt.subplots(figsize=(16, 8))
        
        # Строим столбцы
        colors = plt.cm.viridis(np.linspace(0, 0.9, len(self.alphabet)))
        bars = ax.bar(range(len(self.alphabet)), frequencies, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Ожидаемая частота (равномерное распределение)
        expected_freq = total_hashes / 32
        ax.axhline(y=expected_freq, color='red', linestyle='--', linewidth=2, 
                   label=f'Ожидаемая частота ({expected_freq:.1f})')
        
        # Настройка осей
        ax.set_xlabel('Символы алфавита', fontsize=12, fontweight='bold')
        ax.set_ylabel('Частота появления (из {:,} хешей)'.format(total_hashes), fontsize=12, fontweight='bold')
        ax.set_title(f'Распределение символов на позиции {position}\n(всего хешей: {total_hashes:,})', 
                     fontsize=14, fontweight='bold')
        
        # Подписи символов на оси X
        ax.set_xticks(range(len(self.alphabet)))
        ax.set_xticklabels(self.alphabet, fontsize=9, rotation=45, ha='right')
        
        # Добавляем значения на столбцы
        for i, (bar, freq) in enumerate(zip(bars, frequencies)):
            if freq > 0:
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
                       f'{freq}', ha='center', va='bottom', fontsize=8, rotation=90)
        
        # Статистика
        unique = len([f for f in frequencies if f > 0])
        coverage = unique / 32 * 100
        max_freq = max(frequencies)
        min_freq = min([f for f in frequencies if f > 0])
        deviation = sum(abs(f - expected_freq) for f in frequencies) / 32
        
        # Добавляем текст со статистикой
        stats_text = f'Уникальных символов: {unique}/32 ({coverage:.1f}%)\n'
        stats_text += f'Максимальная частота: {max_freq}\n'
        stats_text += f'Минимальная частота: {min_freq}\n'
        stats_text += f'Среднее отклонение: {deviation:.2f} ({deviation/expected_freq*100:.1f}%)'
        
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        # Легенда
        ax.legend(loc='upper right')
        
        # Сетка
        ax.grid(axis='y', alpha=0.3)
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"  Гистограмма сохранена: {filename}")
        
        return {
            'unique': unique,
            'coverage': coverage,
            'max_freq': max_freq,
            'min_freq': min_freq,
            'deviation': deviation,
            'expected': expected_freq
        }
    
    def plot_comparison_histogram(self, counter1, counter2, pos1, pos2, total_hashes, filename):
        """Создаёт сравнительную гистограмму для двух позиций."""
        
        frequencies1 = [counter1.get(sym, 0) for sym in self.alphabet]
        frequencies2 = [counter2.get(sym, 0) for sym in self.alphabet]
        
        fig, ax = plt.subplots(figsize=(18, 8))
        
        x = np.arange(len(self.alphabet))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, frequencies1, width, label=f'Позиция {pos1}', 
                       color='steelblue', alpha=0.8, edgecolor='black', linewidth=0.5)
        bars2 = ax.bar(x + width/2, frequencies2, width, label=f'Позиция {pos2}', 
                       color='coral', alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Ожидаемая частота
        expected_freq = total_hashes / 32
        ax.axhline(y=expected_freq, color='green', linestyle='--', linewidth=2, 
                   label=f'Ожидаемая частота ({expected_freq:.1f})')
        
        ax.set_xlabel('Символы алфавита', fontsize=12, fontweight='bold')
        ax.set_ylabel('Частота появления (из {:,} хешей)'.format(total_hashes), fontsize=12, fontweight='bold')
        ax.set_title(f'Сравнение распределения символов\nпозиция {pos1} vs позиция {pos2}', 
                     fontsize=14, fontweight='bold')
        
        ax.set_xticks(x)
        ax.set_xticklabels(self.alphabet, fontsize=9, rotation=45, ha='right')
        
        # Статистика для двух позиций
        unique1 = len([f for f in frequencies1 if f > 0])
        unique2 = len([f for f in frequencies2 if f > 0])
        
        stats_text = f'Позиция {pos1}: {unique1}/32 символов ({unique1/32*100:.1f}%)\n'
        stats_text += f'Позиция {pos2}: {unique2}/32 символов ({unique2/32*100:.1f}%)'
        
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=11,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        ax.legend(loc='upper right')
        ax.grid(axis='y', alpha=0.3)
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"  Сравнительная гистограмма сохранена: {filename}")
    
    def run(self, seed="ХОРОШО_БЫТЬ_ВАМИ", num_hashes=10000, positions=[0, 31]):
        """Запускает анализ и создаёт гистограммы."""
        
        print("=" * 60)
        print("ГИСТОГРАММА РАСПРЕДЕЛЕНИЯ СИМВОЛОВ")
        print("=" * 60)
        
        # Генерируем хеши
        hashes = self.generate_hashes(seed, num_hashes)
        
        # Анализируем каждую позицию
        counters = {}
        for pos in positions:
            print(f"\nАнализ позиции {pos}...")
            counters[pos] = self.analyze_position(hashes, pos)
        
        # Создаём гистограммы
        print("\nСоздание гистограмм...")
        
        results = {}
        for pos in positions:
            filename = f"histogram_position_{pos}.png"
            results[pos] = self.plot_histogram(counters[pos], pos, num_hashes, filename)
        
        # Сравнительная гистограмма
        if len(positions) == 2:
            self.plot_comparison_histogram(counters[positions[0]], counters[positions[1]], 
                                          positions[0], positions[1], num_hashes,
                                          "histogram_comparison.png")
        
        # Вывод результатов
        print("\n" + "=" * 60)
        print("РЕЗУЛЬТАТЫ")
        print("=" * 60)
        
        for pos in positions:
            print(f"\nПозиция {pos}:")
            print(f"  Уникальных символов: {results[pos]['unique']}/32 ({results[pos]['coverage']:.1f}%)")
            print(f"  Максимальная частота: {results[pos]['max_freq']}")
            print(f"  Минимальная частота: {results[pos]['min_freq']}")
            print(f"  Среднее отклонение: {results[pos]['deviation']:.2f} ({results[pos]['deviation']/results[pos]['expected']*100:.1f}%)")
        
        print("\n" + "=" * 60)
        print("СОЗДАННЫЕ ФАЙЛЫ:")
        for pos in positions:
            print(f"  - histogram_position_{pos}.png")
        if len(positions) == 2:
            print("  - histogram_comparison.png")
        print("=" * 60)


if __name__ == '__main__':
    # Создаём гистограммы для позиций 0 (начало) и 31 (середина)
    plotter = PositionHistogramPlot()
    plotter.run("ХОРОШО_БЫТЬ_ВАМИ", num_hashes=10000, positions=[0, 31])