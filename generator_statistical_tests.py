import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from alphabet_cipher import AlphabetCipher
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
import random

class GeneratorStatisticalTests:
    def __init__(self):
        self.cipher = AlphabetCipher()
        
        # Параметры генераторов (из файла, стр. 55)
        self.sets = [
            [self.cipher.taps2bin([19, 18]), self.cipher.taps2bin([18, 7]), self.cipher.taps2bin([17, 3])],
            [self.cipher.taps2bin([19, 18]), self.cipher.taps2bin([18, 7]), self.cipher.taps2bin([16, 14, 13, 11])],
            [self.cipher.taps2bin([19, 18]), self.cipher.taps2bin([18, 7]), self.cipher.taps2bin([15, 13, 12, 10])],
            [self.cipher.taps2bin([19, 18]), self.cipher.taps2bin([18, 7]), self.cipher.taps2bin([14, 5, 3, 1])]
        ]
    
    def generate_bits_from_generator(self, seed, num_bits=4000, use_sequential=False, prev_state=None):
        """
        Генерирует битовую последовательность из композиционного генератора.
        
        Args:
            seed: Начальное значение (строка 16 символов)
            num_bits: Количество бит для генерации
            use_sequential: Если True, использует последовательные вызовы
            prev_state: Предыдущее состояние (если есть)
        """
        bits = []
        
        if use_sequential and prev_state is not None:
            # Продолжаем с предыдущего состояния
            result = self.cipher.C_AS_LFSR_next("down", prev_state, -1, self.sets)
        else:
            # Начинаем с нового seed
            result = self.cipher.C_AS_LFSR_next("up", -1, seed, self.sets)
        
        current_state = result[1]
        
        while len(bits) < num_bits:
            output = result[0]
            
            for char in output:
                if len(bits) < num_bits:
                    num = self.cipher.get_number_by_symbol(char)
                    bin_str = format(num, '05b')
                    for b in bin_str:
                        if len(bits) < num_bits:
                            bits.append(int(b))
            
            if len(bits) < num_bits:
                result = self.cipher.C_AS_LFSR_next("down", current_state, -1, self.sets)
                current_state = result[1]
        
        return bits, current_state
    
    def generate_bits_for_replication(self, seed, replication_index, num_bits=4000):
        """
        Генерирует биты для одной репликации.
        Каждая репликация использует свой seed (seed + индекс).
        """
        # Модифицируем seed для каждой репликации
        modified_seed = list(seed)
        # Изменяем последние 4 символа в зависимости от индекса репликации
        idx_str = f"{replication_index:04d}"
        for i, ch in enumerate(idx_str):
            pos = len(modified_seed) - 4 + i
            if pos < len(modified_seed):
                # Преобразуем цифру в символ алфавита (0→А, 1→Б, ...)
                new_char = self.cipher.get_symbol_by_number(int(ch) + 1)
                modified_seed[pos] = new_char
        
        new_seed = ''.join(modified_seed)
        
        bits, _ = self.generate_bits_from_generator(new_seed, num_bits, use_sequential=False)
        return bits
    
    def frequency_monobit_test(self, bits):
        """Частотный монобитный тест."""
        n = len(bits)
        n1 = sum(bits)
        n0 = n - n1
        
        p1 = n1 / n
        p0 = n0 / n
        
        s = math.sqrt(n * p1 * p0) / n if p1 * p0 > 0 else 0.001
        x = abs(p0 - p1) / s if s > 0 else 100
        
        passed = x < 3
        
        return {
            'n': n,
            'n1': n1,
            'n0': n0,
            'x': x,
            'passed': passed
        }
    
    def max_series_length_test(self, bits):
        """Тест на максимальную длину серии единиц."""
        max_series = 0
        current_series = 0
        
        for bit in bits:
            if bit == 1:
                current_series += 1
                max_series = max(max_series, current_series)
            else:
                current_series = 0
        
        passed = 10 <= max_series <= 15
        
        return {
            'max_series': max_series,
            'passed': passed
        }
    
    def run_tests(self, base_seed="ХОРОШО_БЫТЬ_ВАМИ", num_replications=200, bits_per_replication=4000):
        """Запускает оба теста на 200 репликациях."""
        print("=" * 70)
        print("СТАТИСТИЧЕСКИЕ ТЕСТЫ ГЕНЕРАТОРА СЛУЧАЙНЫХ КОДОВ")
        print("=" * 70)
        
        print(f"\nПараметры тестирования:")
        print(f"  - Количество репликаций: {num_replications}")
        print(f"  - Длина каждой репликации: {bits_per_replication} бит")
        print(f"  - Начальное значение (seed): {base_seed}")
        
        freq_results = []
        series_results = []
        
        print("\nЗапуск тестов...")
        
        for i in range(num_replications):
            # Генерируем биты для репликации (каждая со своим seed)
            bits = self.generate_bits_for_replication(base_seed, i, bits_per_replication)
            
            freq_result = self.frequency_monobit_test(bits)
            freq_results.append(freq_result)
            
            series_result = self.max_series_length_test(bits)
            series_results.append(series_result)
            
            if (i + 1) % 50 == 0:
                print(f"  Выполнено {i + 1} репликаций...")
        
        print("  Готово!")
        
        # Анализ результатов
        freq_passed = sum(1 for r in freq_results if r['passed'])
        freq_failed = num_replications - freq_passed
        freq_x_values = [r['x'] for r in freq_results]
        avg_x = sum(freq_x_values) / len(freq_x_values)
        
        series_passed = sum(1 for r in series_results if r['passed'])
        series_failed = num_replications - series_passed
        series_max_values = [r['max_series'] for r in series_results]
        avg_max_series = sum(series_max_values) / len(series_max_values)
        
        print("\n" + "=" * 70)
        print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
        print("=" * 70)
        
        print("\n1. ЧАСТОТНЫЙ МОНОБИТНЫЙ ТЕСТ")
        print(f"   Критерий: x < 3")
        print(f"   Прошло тест: {freq_passed} репликаций ({freq_passed/num_replications*100:.1f}%)")
        print(f"   Не прошло: {freq_failed} репликаций ({freq_failed/num_replications*100:.1f}%)")
        print(f"   Среднее значение x: {avg_x:.4f}")
        print(f"   Минимальное x: {min(freq_x_values):.4f}")
        print(f"   Максимальное x: {max(freq_x_values):.4f}")
        
        print("\n2. ТЕСТ НА МАКСИМАЛЬНУЮ ДЛИНУ СЕРИИ ЕДИНИЦ")
        print(f"   Критерий: максимальная длина серии ∈ [10, 15]")
        print(f"   Прошло тест: {series_passed} репликаций ({series_passed/num_replications*100:.1f}%)")
        print(f"   Не прошло: {series_failed} репликаций ({series_failed/num_replications*100:.1f}%)")
        print(f"   Средняя максимальная длина серии: {avg_max_series:.2f}")
        print(f"   Минимальная максимальная длина: {min(series_max_values)}")
        print(f"   Максимальная максимальная длина: {max(series_max_values)}")
        
        # Создаём гистограммы
        self.plot_frequency_histogram(freq_x_values, num_replications, avg_x)
        self.plot_series_histogram(series_max_values, num_replications, avg_max_series)
        
        return {
            'freq': freq_results,
            'series': series_results,
            'freq_passed': freq_passed,
            'freq_failed': freq_failed,
            'avg_x': avg_x,
            'series_passed': series_passed,
            'series_failed': series_failed,
            'avg_max_series': avg_max_series
        }
    
    def plot_frequency_histogram(self, x_values, num_replications, avg_x):
        """Гистограмма для частотного монобитного теста."""
        fig, ax = plt.subplots(figsize=(12, 7))
        
        n_bins = min(30, len(set(x_values)))
        counts, bins, patches = ax.hist(x_values, bins=n_bins, color='steelblue', 
                                        edgecolor='black', alpha=0.8, rwidth=0.95)
        
        ax.axvline(x=3, color='red', linestyle='--', linewidth=2, label='Критический порог (x = 3)')
        ax.axvline(x=avg_x, color='green', linestyle='-', linewidth=2, label=f'Среднее значение (x = {avg_x:.4f})')
        
        ax.set_xlabel('Статистика x', fontsize=14, fontweight='bold')
        ax.set_ylabel('Количество репликаций', fontsize=14, fontweight='bold')
        ax.set_title(f'Частотный монобитный тест\n(всего репликаций: {num_replications})', 
                     fontsize=16, fontweight='bold')
        
        passed = sum(1 for x in x_values if x < 3)
        failed = num_replications - passed
        
        stats_text = f'Прошло тест: {passed} ({passed/num_replications*100:.1f}%)\n'
        stats_text += f'Не прошло: {failed} ({failed/num_replications*100:.1f}%)\n'
        stats_text += f'Среднее x: {avg_x:.4f}'
        
        ax.text(0.98, 0.97, stats_text, transform=ax.transAxes, fontsize=11,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))
        
        ax.legend(loc='upper left')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        plt.savefig('frequency_monobit_test.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print("\n  Гистограмма сохранена: frequency_monobit_test.png")
    
    def plot_series_histogram(self, max_series_values, num_replications, avg_max_series):
        """Гистограмма для теста на максимальную длину серии единиц."""
        fig, ax = plt.subplots(figsize=(12, 7))
        
        bins = range(min(max_series_values) - 1, max(max_series_values) + 2)
        counts, bins_edges, patches = ax.hist(max_series_values, bins=bins, color='coral',
                                               edgecolor='black', alpha=0.8, rwidth=0.9)
        
        # Закрашиваем допустимый интервал [10, 15]
        for i, patch in enumerate(patches):
            bin_center = (bins_edges[i] + bins_edges[i+1]) / 2
            if 10 <= bin_center <= 15:
                patch.set_facecolor('lightgreen')
                patch.set_alpha(0.8)
        
        ax.axvline(x=10, color='green', linestyle='--', linewidth=2, label='Нижняя граница (10)')
        ax.axvline(x=15, color='green', linestyle='--', linewidth=2, label='Верхняя граница (15)')
        ax.axvline(x=avg_max_series, color='blue', linestyle='-', linewidth=2, 
                   label=f'Среднее значение ({avg_max_series:.2f})')
        
        ax.set_xlabel('Максимальная длина серии единиц (бит)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Количество репликаций', fontsize=14, fontweight='bold')
        ax.set_title(f'Тест на максимальную длину серии единиц\n(всего репликаций: {num_replications})', 
                     fontsize=16, fontweight='bold')
        
        passed = sum(1 for m in max_series_values if 10 <= m <= 15)
        failed = num_replications - passed
        
        stats_text = f'Прошло тест: {passed} ({passed/num_replications*100:.1f}%)\n'
        stats_text += f'Не прошло: {failed} ({failed/num_replications*100:.1f}%)\n'
        stats_text += f'Среднее значение: {avg_max_series:.2f}'
        
        ax.text(0.98, 0.97, stats_text, transform=ax.transAxes, fontsize=11,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))
        
        ax.legend(loc='upper left')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        plt.savefig('max_series_test.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print("  Гистограмма сохранена: max_series_test.png")


if __name__ == '__main__':
    tester = GeneratorStatisticalTests()
    
    results = tester.run_tests(
        base_seed="ХОРОШО_БЫТЬ_ВАМИ",
        num_replications=200,
        bits_per_replication=4000
    )
    
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 70)
    print("\nСозданные файлы:")
    print("  - frequency_monobit_test.png")
    print("  - max_series_test.png")
    print("=" * 70)