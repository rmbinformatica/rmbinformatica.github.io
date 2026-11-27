import tempfile
import unittest
import json
from pathlib import Path
from generate_redirects import load_redirects, ORIGIN

class RedirectTests(unittest.TestCase):
    def parse(self, rules):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "redirects.yml"
            path.write_text(json.dumps({"redirects": rules}))
            return load_redirects(path)

    def rule(self, source, dest, status=301):
        return {"from": source, "to": dest, "status": status}

    def test_empty(self):
        self.assertEqual(self.parse([]), {})

    def test_valid(self):
        self.assertEqual(self.parse([self.rule("/old", "/new/")]), {ORIGIN+"/old": ORIGIN+"/new/"})

    def test_invalid(self):
        for rules in [
            [self.rule("/a", "/a")],
            [self.rule("/a", "/b"), self.rule("/b", "/a")],
            [self.rule("/a", "/b"), self.rule("/b", "/c")],
            [self.rule("/a", "/b"), self.rule("/a", "/c")],
            [self.rule("/a", "//external.example")],
            [self.rule("/a", "/../b")],
            [self.rule("/a", "/b", 302)],
            [self.rule("/sitemap.xml", "/b")],
        ]:
            with self.subTest(rules=rules), self.assertRaises(ValueError):
                self.parse(rules)

if __name__ == "__main__":
    unittest.main()
