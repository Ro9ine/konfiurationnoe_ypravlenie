def ls_command(vfs):
    files = vfs.list_files(vfs.get_current_directory())
    for file in files:
        print(file)

def cd_command(vfs, path):
    try:
        vfs.change_directory(path)
    except FileNotFoundError as e:
        print(e)

def pwd_command(vfs):
    print(vfs.get_current_directory())

def exit_command():
    import sys
    sys.exit(0)

def chmod_command(vfs, path, mode):
    # Учет текущей директории
    if not path.startswith("/"):
        path = vfs.get_current_directory().rstrip('/') + '/' + path
    print(path)
    # Проверка существования пути
    if vfs._path_exists(path):
        vfs.set_file_permissions(path, mode)  # Установка прав
        print(f"Changed mode for {path} to {mode}")
    else:
        print(f"No such file or directory: {path}")
