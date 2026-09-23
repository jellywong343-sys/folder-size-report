import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"src"))
from folder_size_report.cli import human_size,scan_folder
class Tests(unittest.TestCase):
 def test_scan(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp); (root/"a.txt").write_bytes(b"123"); (root/"b.bin").write_bytes(b"12345"); report=scan_folder(root)
   self.assertEqual(report["file_count"],2); self.assertEqual(report["total_bytes"],8); self.assertEqual(human_size(1024),"1.0 KB")
if __name__ == "__main__": unittest.main()
