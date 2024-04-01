import shutil
from pathlib import Path, PurePath
from urllib import parse
import urllib3


def filename_from_url(url: str):
    tuples = parse.urlparse(url)
    parts = tuples.path.split('/')
    return parts[len(parts) - 1]


def copy_chunked(remote_url: str, local_dir: PurePath, chunk_kb=1000):
    http = urllib3.PoolManager()
    local_file = local_dir.joinpath(filename_from_url(remote_url))
    res = None
    try:
        Path(local_dir).mkdir(parents=True, exist_ok=True)
        res = http.request("GET", remote_url, preload_content=False)
        with open(local_file, 'wb') as f:
            while True:
                dat = res.read(chunk_kb * 1000)
                if not dat:
                    break
                f.write(dat)
    finally:
        if res is not None:
            res.release_conn()
    return local_file


def unpack_to_archive_dir(archive_path: PurePath):
    pp = PurePath(archive_path)
    dest_dir = pp.parent.joinpath(pp.stem)
    shutil.unpack_archive(archive_path, extract_dir=dest_dir)
    return dest_dir
