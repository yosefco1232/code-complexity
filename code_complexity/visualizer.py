import matplotlib.pyplot as plt
from jinja2 import Template

def plot_complexity(results, output_file='complexity_plot.png'):
    """Improved visualization with severity coloring"""
    colors = {
        'A (Low)': 'green',
        'B (Moderate)': 'yellow',
        'C (High)': 'orange',
        'D (Very High)': 'red',
        'E/F (Extreme)': 'purple'
    }
    
    plt.figure(figsize=(12, 8))
    for file_data in results:
        for func in file_data['cyclomatic']:
            plt.barh(
                f"{func['name']} (Line {func['line']})",
                func['complexity'],
                color=colors.get(func['rank'], 'gray')
	    )
    
    plt.title('Code Complexity Analysis (Strict Mode)')
    plt.xlabel('Adjusted Complexity Score')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file, dpi=120)
    plt.close()

def generate_html_report(results, output_file='report.html'):
    """HTML report with class/method breakdown"""
    template = Template('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Enhanced Complexity Report</title>
        <style>
            body { font-family: Arial; margin: 20px; }
            .func { margin: 5px 0; padding: 10px; border-radius: 4px; }
            .A { background: #d4edda; border-left: 4px solid #28a745; }
            .B { background: #fff3cd; border-left: 4px solid #ffc107; }
            .C { background: #ffe8d1; border-left: 4px solid #fd7e14; }
            .D { background: #f8d7da; border-left: 4px solid #dc3545; }
            .EF { background: #e2d4f0; border-left: 4px solid #6f42c1; }
            .class-header { background: #f8f9fa; padding: 10px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Enhanced Code Complexity Report</h1>
        {% for file in results %}
        <div class="file-section">
            <h2>{{ file.file }}</h2>
            <p>Lines: {{ file.loc }} | Halstead Volume: {{ file.halstead.volume | round(2) }}</p>
            
            {% for func in file.cyclomatic %}
            <div class="func {{ func.rank.split()[0] }}">
                <strong>{{ func.name }}</strong> (Line {{ func.line }}):
                <span>{{ func.complexity }} ({{ func.rank }})</span>
                {% if func.type == 'method' %}<em> [Method]</em>{% endif %}
            </div>
            {% endfor %}
        </div>
        {% endfor %}
    </body>
    </html>
    ''')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template.render(results=results))