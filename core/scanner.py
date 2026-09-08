import os

def scan_project_files(root_dir: str, suffix_list: list) -> list:
    """
    Scan project code files recursively
    Skip hidden dirs, venv, node_modules and cache dirs
    """
    ignore_dirs = {".git", "venv", ".venv", "node_modules", "__pycache__", "build", "dist"}
    target_files = []

    for root, dirs, files in os.walk(root_dir):
        # Filter ignore dir
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for fname in files:
            for suf in suffix_list:
                if fname.endswith(suf):
                    full_path = os.path.abspath(os.path.join(root, fname))
                    target_files.append(full_path)
                    break
    return target_files