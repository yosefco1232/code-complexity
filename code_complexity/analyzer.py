import ast
from radon.complexity import cc_visit, cc_rank
from radon.metrics import h_visit
from radon.visitors import ComplexityVisitor

def custom_rank(complexity):
    """Stricter complexity thresholds"""
    if complexity <= 3: return "A (Low)"
    elif complexity <= 6: return "B (Moderate)"
    elif complexity <= 10: return "C (High)"
    elif complexity <= 15: return "D (Very High)"
    else: return "E/F (Extreme)"

def analyze_file(filepath):
    """Process a single Python file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        return {
            'file': filepath,
            'error': f"Could not read file: {str(e)}"
        }

    # Cyclomatic Complexity
    cc_results = []
    try:
        for func in cc_visit(code):
            # Calculate nesting complexity
            try:
                visitor = ComplexityVisitor.from_code(func.source)
                nested_count = len([f for f in visitor.functions if f != func.name])
                complexity = func.complexity * (1 + (nested_count * 0.2))
            except:
                complexity = func.complexity
            
            cc_results.append({
                'name': func.name,
                'complexity': round(complexity, 1),
                'rank': custom_rank(complexity),
                'line': func.lineno,
                'type': 'method' if 'self' in func.name else 'function'
            })
    except Exception as e:
        return {
            'file': filepath,
            'error': f"Complexity analysis failed: {str(e)}"
        }

    # Halstead Metrics
    halstead = h_visit(code) if code else None
    
    return {
        'file': filepath,
        'cyclomatic': cc_results,
        'halstead': {
            'volume': halstead.total.volume if halstead else 0,
            'difficulty': halstead.total.difficulty if halstead else 0,
            'bugs': halstead.total.bugs if halstead else 0
        },
        'loc': len(code.splitlines()) if code else 0
    }