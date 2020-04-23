from pathlib import Path

try:
    from tqdm.auto import tqdm
except ModuleNotFoundError:
    tqdm = list

root_path = Path(__file__) / ".."
root_path = root_path.resolve()

src_file = root_path / "russian.txt"
out_file = root_path / "russian_utf-8.txt"

if out_file.exists():
    out_file.unlink()

with src_file.open("r", encoding="windows-1251") as in_file:
    for line in tqdm(in_file.readlines()):
        line = line.strip("- \n")
        with out_file.open("a", encoding="utf-8") as out:
            out.write(line + "\n")
