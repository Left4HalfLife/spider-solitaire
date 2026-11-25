import unittest
from pathlib import Path

from app import app


class AppTest(unittest.TestCase):
    def test_index_serves_game(self):
        response = app.test_client().get("/")
        self.addCleanup(response.close)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "text/html")
        self.assertEqual(
            response.data, (Path(app.root_path) / "index.html").read_bytes()
        )

    def test_other_files_are_not_served(self):
        response = app.test_client().get("/app.py")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
