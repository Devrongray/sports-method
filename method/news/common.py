from __future__ import annotations

import gzip
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

UA = "sports-method/0.1 (research recorder; https://github.com/Devrongray/sports-method)"


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def stamp(dt: datetime) -> str:
    return dt.strftime("%Y%m%dT%H%M%SZ")


def digest(obj) -> str:
    raw = obj if isinstance(obj, (bytes, bytearray)) else json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def write_gz_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        json.dump(obj, f, separators=(",", ":"), default=str)


def write_gz_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wb") as f:
        f.write(data)


def session() -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = UA
    return s


def robots_allows(sess: requests.Session, base: str, path: str, timeout: float = 10) -> bool:
    """Minimal robots.txt check for the '*' agent: False if any Disallow
    prefix matches the path (Allow lines are honoured when more specific)."""
    try:
        r = sess.get(base.rstrip("/") + "/robots.txt", timeout=timeout)
        if r.status_code != 200:
            return True
    except requests.RequestException:
        return True
    applies = False
    allow, disallow = [], []
    for line in r.text.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, val = [x.strip() for x in line.split(":", 1)]
        key = key.lower()
        if key == "user-agent":
            applies = val == "*"
        elif applies and key == "disallow" and val:
            disallow.append(val)
        elif applies and key == "allow" and val:
            allow.append(val)
    best_allow = max((a for a in allow if path.startswith(a)), key=len, default="")
    best_dis = max((d for d in disallow if path.startswith(d)), key=len, default="")
    return len(best_allow) >= len(best_dis)
