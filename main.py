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

with src_file.open("r", encoding="windows-1251") as src, out_file.open("w", encoding="utf-8") as out:
    for line in tqdm(src.readlines()):
        line = line.strip("- \n")
        out.write(line + "\n")
