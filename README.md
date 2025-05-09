﻿# Code Complexity Analyzer

A Python CLI tool that analyzes and visualizes code complexity metrics with Radon.

## Features
- Cyclomatic complexity analysis
- Halstead metrics
- HTML/Plot/JSON outputs
- Strict complexity ranking

## Installation

pip install git https://github.com/yosefco1232/code-complexity.git

## Usage

Analyze a single file:
```bash
code-complexity examples/sample.py --output html
```

Analyze a whole project:
```bash
code-complexity src/ --output json
```

Custom output locations:
```bash
code-complexity my_script.py --output plot --outfile report.png
```
