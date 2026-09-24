# Folder Size Report

[绠€浣撲腑鏂嘳(README.zh-CN.md)

Scan a folder and generate readable size summaries, top-file lists, JSON, and CSV reports.

## Highlights

- Python standard library only; no runtime dependencies.
- Command-line interface and automated tests included.
- Safe defaults and clear output.
- Windows, macOS, and Linux; Python 3.10+.

## Installation

```bash
git clone https://github.com/jellywong343-sys/folder-size-report.git
cd folder-size-report
python -m pip install -e .
```

Replace `jellywong343-sys` with your GitHub username.

## Usage

```bash
folder-report ~/Downloads --top 20
folder-report ~/Downloads --json report.json --csv extensions.csv
```

Run `folder-report --help` to see every option.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
folder-size-report/
鈹溾攢鈹€ src/folder_size_report/
鈹溾攢鈹€ tests/
鈹溾攢鈹€ README.md
鈹溾攢鈹€ README.zh-CN.md
鈹溾攢鈹€ pyproject.toml
鈹斺攢鈹€ LICENSE
```

## Safety

Review command output before applying changes to important files. Keep backups of irreplaceable data.

## License

MIT


