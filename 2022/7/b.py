from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Dir:
    parent: Dir | None
    files: dict[str, int] = field(default_factory=dict)
    dirs: dict[str, Dir] = field(default_factory=dict)


with open(Path(__file__).parent.joinpath("input.txt")) as f:
    fs = Dir(parent=None)
    current = fs

    for line in f:
        first, *rest = line.rstrip("\n").split(" ")
        if first == "$":
            cmd = rest[0]
            if cmd == "cd":
                dirname = rest[1]
                if dirname == "..":
                    assert current.parent is not None, "current.parent is None"
                    current = current.parent
                elif dirname == "/":
                    current = fs
                else:
                    assert current is not None, "current is None"
                    current = current.dirs.setdefault(dirname, Dir(parent=current))
        elif first != "dir":
            fname = rest[0]
            assert current is not None, "current is None"
            current.files.setdefault(fname, int(first))

    dir_sizes: list[int] = []

    def compute_size(directory: Dir) -> int:
        size = sum(directory.files.values())

        for dir_ in directory.dirs.values():
            dir_size = compute_size(dir_)
            dir_sizes.append(dir_size)
            size += dir_size

        return size

    root_size = compute_size(fs)
    needed_size = 30_000_000 - (70_000_000 - root_size)

    dir_size = min([size for size in dir_sizes if size >= needed_size])
    assert dir_size == 7991939
    print(dir_size)
