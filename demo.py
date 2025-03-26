"""
demo.py - A script demonstrating different complexity levels
for testing the Code Complexity Visualizer
"""

import math
from typing import List, Dict, Optional

# Low complexity (Rank A)
def calculate_area(radius: float) -> float:
    """Calculate circle area."""
    return math.pi * radius ** 2

# Medium complexity (Rank B)
def process_data(data: List[float], threshold: float = 0.5) -> Dict[str, float]:
    """
    Process data list and return statistics.
    Filters values above threshold first.
    """
    filtered = [x for x in data if x > threshold]
    
    if not filtered:
        return {"average": 0, "max": 0}
    
    return {
        "average": sum(filtered) / len(filtered),
        "max": max(filtered),
        "items": len(filtered)
    }

# High complexity (Rank C/D)
def fibonacci_analysis(n: int, mod: Optional[int] = None) -> Dict[str, List[int]]:
    """
    Generate Fibonacci sequence with optional modulo,
    then analyze parity and digit patterns.
    """
    if n <= 0:
        return {"error": "n must be positive"}
    
    a, b = 0, 1
    sequence = [a]
    
    for _ in range(n - 1):
        a, b = b, a + b
        if mod:
            a %= mod
            b %= mod
        sequence.append(a)
    
    # Analyze parity
    parity = ["even" if x % 2 == 0 else "odd" for x in sequence]
    
    # Digit pattern analysis
    digit_counts = []
    for num in sequence:
        if num == 0:
            digit_counts.append(1)
        else:
            digit_counts.append(int(math.log10(abs(num))) + 1)
    
    return {
        "sequence": sequence,
        "parity": parity,
        "digit_counts": digit_counts
    }

# Very high complexity (Rank E/F)
class DataProcessor:
    """A class with complex stateful processing."""
    
    def __init__(self, initial_data: List[float]):
        self.data = initial_data
        self._cache = {}
    
    def analyze(self, window_size: int = 3) -> Dict[str, float]:
        """Running analysis with sliding window."""
        if window_size > len(self.data):
            raise ValueError("Window too large")
        
        results = []
        for i in range(len(self.data) - window_size + 1):
            window = self.data[i:i+window_size]
            stats = self._calculate_window_stats(window)
            results.append(stats)
        
        return {
            "overall_avg": sum(r["avg"] for r in results) / len(results),
            "trend": "increasing" if results[-1]["avg"] > results[0]["avg"] else "decreasing"
        }
    
    def _calculate_window_stats(self, window: List[float]) -> Dict[str, float]:
        """Helper method with nested complexity."""
        if len(window) == 0:
            return {"avg": 0, "stddev": 0}
        
        avg = sum(window) / len(window)
        variance = sum((x - avg) ** 2 for x in window) / len(window)
        
        return {
            "avg": avg,
            "stddev": math.sqrt(variance),
            "min_max_ratio": min(window) / max(window) if max(window) != 0 else 0
        }

if __name__ == "__main__":
    # Test cases
    print(calculate_area(5))
    print(process_data([0.1, 0.6, 0.7, 0.2]))
    print(fibonacci_analysis(10, mod=3))
    processor = DataProcessor([1.2, 3.4, 5.6, 7.8])
    print(processor.analyze(window_size=2))