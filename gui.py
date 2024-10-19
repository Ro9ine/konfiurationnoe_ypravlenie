import tkinter as tk

class ShellEmulatorGUI:
    def __init__(self, vfs, logger, username, hostname):
        self.vfs = vfs
        self.logger = logger
        self.username = username
        self.hostname = hostname
        self.root = tk.Tk()
        self.root.title("Shell Emulator")

        self.output = tk.Text(self.root, height=20, width=80)
        self.output.pack()

        self.input = tk.Entry(self.root, width=80)
        self.input.pack()
        self.input.bind("<Return>", self.handle_command)

        self.prompt()

    def prompt(self):
        self.input.delete(0, tk.END)
        self.input.insert(0, f"{self.username}@{self.hostname}:{self.vfs.get_current_directory()}$ ")

    def handle_command(self, event):
        command_input = self.input.get()
        self.output.insert(tk.END, command_input + '\n')  # Вывод команды в окно вывода
        command = command_input.split()[1:]  # Парсинг команды

        if command:
            if command[0] == "ls":
                self.ls()
            elif command[0] == "cd":
                if len(command) > 1:
                    self.cd(command[1])
                else:
                    self.output.insert(tk.END, "cd: missing argument\n")
            elif command[0] == "pwd":
                self.pwd()
            elif command[0] == "exit":
                self.root.quit()
            elif command[0] == "chmod":
                if len(command) > 2:
                    self.chmod(command[1], command[2])
                else:
                    self.output.insert(tk.END, "chmod: missing argument(s)\n")
            else:
                self.output.insert(tk.END, f"Command not found: {command[0]}\n")

        self.prompt()
        self.logger.log_action(self.username, ' '.join(command))

    def ls(self):
        files = self.vfs.list_files(self.vfs.get_current_directory())
        for file in files:
            self.output.insert(tk.END, file + '\n')

    def cd(self, path):
        try:
            self.vfs.change_directory(path)
            self.output.insert(tk.END, f"Changed directory to {self.vfs.get_current_directory()}\n")
        except FileNotFoundError as e:
            self.output.insert(tk.END, str(e) + '\n')

    def pwd(self):
        self.output.insert(tk.END, self.vfs.get_current_directory() + '\n')

    def chmod(self, path, mode):
        print(path)
        if self.vfs._path_exists(path):
            self.output.insert(tk.END, f"Changed mode for {path} to {mode}\n")
        else:
            self.output.insert(tk.END, f"No such file or directory: {path}\n")
