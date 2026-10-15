import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from organize_downloads import category_for, main, plan_moves


class OrganizeDownloadsTests(unittest.TestCase):
    def test_common_extensions_are_classified_case_insensitively(self):
        self.assertEqual(category_for(Path("photo.JPG")), "圖片")
        self.assertEqual(category_for(Path("notes.txt")), "文件")
        self.assertEqual(category_for(Path("table.csv")), "試算表")

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

    def test_preview_does_not_move_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            source = folder / "photo.jpg"
            source.write_text("image-data", encoding="utf-8")

            with patch(
                "sys.argv", ["organize_downloads.py", str(folder)]
            ), redirect_stdout(StringIO()):
                self.assertEqual(main(), 0)

            self.assertEqual(source.read_text(encoding="utf-8"), "image-data")
            self.assertFalse((folder / "圖片").exists())

    def test_apply_preserves_files_when_numbered_name_is_another_source(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / "report.txt").write_text("new-report", encoding="utf-8")
            (folder / "report_1.txt").write_text("numbered-source", encoding="utf-8")
            (folder / "文件").mkdir()
            (folder / "文件" / "report.txt").write_text("old-report", encoding="utf-8")

            with patch(
                "sys.argv", ["organize_downloads.py", str(folder), "--apply"]
            ), redirect_stdout(StringIO()):
                self.assertEqual(main(), 0)

            self.assertEqual(
                (folder / "文件" / "report.txt").read_text(encoding="utf-8"),
                "old-report",
            )
            self.assertEqual(
                (folder / "文件" / "report_1.txt").read_text(encoding="utf-8"),
                "new-report",
            )
            self.assertEqual(
                (folder / "文件" / "report_1_1.txt").read_text(encoding="utf-8"),
                "numbered-source",
            )

    def test_subdirectories_are_not_moved(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / "圖片").mkdir()
            (folder / "圖片" / "photo.jpg").touch()
            self.assertEqual(plan_moves(folder), [])


if __name__ == "__main__":
    unittest.main()
