import tarfile

class VirtualFileSystem:
    def __init__(self, tar_path):
        self.tar_path = tar_path
        self.fs = tarfile.open(tar_path)
        self.current_directory = "/"
        self.permissions = {}  # Словарь для хранения прав

    def list_files(self, path):
        """Вывод списка файлов"""
        path = path.lstrip('/')
        files = [f for f in self.fs.getnames() if f.startswith(path)]
        return files

    def change_directory(self, path):
        """Команда cd"""
        if path.startswith("/"):  # Абсолютный путь
            new_directory = path
        else:  # Относительный путь
            new_directory = self.current_directory.rstrip('/') + '/' + path

        if self._path_exists(new_directory):
            self.current_directory = new_directory
            print(self.current_directory)
        else:
            raise FileNotFoundError(f"No such directory: {new_directory}")

    def _path_exists(self, path):
        """Проверка, существует ли путь"""
        path =  path.lstrip('/')
        print(path)
        print(self.fs.getnames())
        return any(path in f for f in self.fs.getnames())

    def get_current_directory(self):
        return self.current_directory

    def set_file_permissions(self, path, mode):
        """Установка прав для файла"""
        self.permissions[path] = mode

    def get_file_permissions(self, path):
        """Получение прав для файла"""
        return self.permissions.get(path, "No permissions set")
