import click
import os
from .analyzer import analyze_file
from .visualizer import plot_complexity, generate_html_report

@click.command()
@click.argument('path')
@click.option('--output', default='text', 
              type=click.Choice(['text', 'json', 'plot', 'html']),
              help='Output format')
def analyze(path, output):
    """Analyze code complexity of Python files."""
    if os.path.isfile(path) and path.endswith('.py'):
        results = [analyze_file(path)]
    elif os.path.isdir(path):
        results = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.py'):
                    results.append(analyze_file(os.path.join(root, file)))
    else:
        raise click.BadParameter('PATH must be a Python file or directory')

    if output == 'text':
        for res in results:
            click.echo(f"\nFile: {res['file']}")
            for func in res['cyclomatic']:
                click.echo(f"  {func['name']}: {func['complexity']} ({func['rank']})")
    elif output == 'json':
        click.echo(json.dumps(results, indent=2))
    elif output == 'plot':
        plot_complexity(results)
        click.echo("Generated complexity_plot.png")
    elif output == 'html':
        generate_html_report(results)
        click.echo("Generated report.html")

if __name__ == '__main__':
    analyze()