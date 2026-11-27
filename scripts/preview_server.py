"""Local static preview with extensionless Jekyll URLs. No production use."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
import argparse

class PreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        original = Path(super().translate_path(path))
        root = Path(self.directory).resolve()
        if not original.resolve().is_relative_to(root):
            return str(root / '__invalid_preview_path__')
        if not original.exists() and not original.suffix and not urlsplit(path).path.endswith('/'):
            candidate = original.with_suffix('.html')
            if candidate.is_file() and candidate.resolve().is_relative_to(root):
                return str(candidate)
        return str(original)

def make_server(directory, port=8080):
    return ThreadingHTTPServer(('127.0.0.1', port), partial(PreviewHandler, directory=str(Path(directory).resolve())))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--directory', default=str(Path(__file__).resolve().parent))
    args = parser.parse_args()
    with make_server(args.directory, args.port) as server:
        print(f'Preview: http://127.0.0.1:{server.server_port}/preview-v2/', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
