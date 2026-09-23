from __future__ import annotations
import argparse,csv,json
from collections import defaultdict
from pathlib import Path

def human_size(size):
 value=float(size)
 for unit in ("B","KB","MB","GB","TB"):
  if value<1024 or unit=="TB": return f"{value:.1f} {unit}"
  value/=1024

def scan_folder(root:Path,top=10):
 root=root.expanduser().resolve()
 if not root.is_dir(): raise ValueError(f"Not a directory: {root}")
 files=[]; extensions=defaultdict(lambda:{"files":0,"bytes":0})
 for path in root.rglob("*"):
  try:
   if path.is_file() and not path.is_symlink():
    size=path.stat().st_size; files.append((size,path)); ext=path.suffix.lower() or "[no extension]"
    extensions[ext]["files"]+=1; extensions[ext]["bytes"]+=size
  except OSError: continue
 files.sort(reverse=True,key=lambda item:item[0])
 return {"root":str(root),"file_count":len(files),"total_bytes":sum(size for size,_ in files),"top_files":[{"path":str(path),"bytes":size} for size,path in files[:top]],"extensions":dict(sorted(extensions.items(),key=lambda item:-item[1]["bytes"]))}

def main():
 parser=argparse.ArgumentParser(description="Report folder size, largest files, and extension totals."); parser.add_argument("directory"); parser.add_argument("--top",type=int,default=10)
 parser.add_argument("--json",dest="json_path"); parser.add_argument("--csv",dest="csv_path"); args=parser.parse_args(); report=scan_folder(Path(args.directory),args.top)
 print(f"Root: {report['root']}\nFiles: {report['file_count']}\nTotal: {human_size(report['total_bytes'])}\n\nLargest files:")
 for item in report["top_files"]: print(f"  {human_size(item['bytes']):>10}  {item['path']}")
 if args.json_path: Path(args.json_path).write_text(json.dumps(report,indent=2),encoding="utf-8")
 if args.csv_path:
  with Path(args.csv_path).open("w",encoding="utf-8",newline="") as handle:
   writer=csv.writer(handle); writer.writerow(["extension","files","bytes"])
   for ext,data in report["extensions"].items(): writer.writerow([ext,data["files"],data["bytes"]])
if __name__ == "__main__": main()
