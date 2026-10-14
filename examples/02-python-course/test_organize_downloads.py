import tempfile
import unittest
from pathlib import Path

from organize_downloads import category_for, plan_moves


class OrganizeDownloadsTests(unittest.TestCase):
    def test_common_extensions_are_classified_case_insensitively(self):
        self.assertEqual(category_for(Path("photo.JPG")), "圖片")
        self.assertEqual(category_for(Path("notes.txt")), "文件")

    def test_no_extension_goes_to_other(self):
        self.assertEqual(category_for(Path("README")), "其他")

    def test_empty_folder_has_no_moves(self):
        with tempfile.TemporaryDirectory() as temporary:
            self.assertEqual(plan_moves(Path(temporary)), [])

    def test_collision_gets_numbered_destination(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / "report.txt").write_text("new", encoding="utf-8")
            (folder / "文件").mkdir()
            (folder / "文件" / "report.txt").write_text("old", encoding="utf-8")
            moves = plan_moves(folder)
            self.assertEqual(moves[0][1].name, "report_1.txt")

    def test_subdirectories_are_not_moved(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / "圖片").mkdir()
            (folder / "圖片" / "photo.jpg").touch()
            self.assertEqual(plan_moves(folder), [])


if __name__ == "__main__":
    unittest.main()
