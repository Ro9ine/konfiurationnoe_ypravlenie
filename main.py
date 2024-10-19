from config_reader import read_config
from vfs import VirtualFileSystem
from logger import Logger
from gui import ShellEmulatorGUI

if __name__ == "__main__":
    config = read_config("C:\\Users\\ASUS\\PycharmProjects\\pythonProject\\project1\\config.csv")
    vfs = VirtualFileSystem('C:\\Users\\ASUS\\PycharmProjects\\pythonProject\\project1\\zipfile.tar')
    logger = Logger(config['log_path'])

    gui = ShellEmulatorGUI(vfs, logger, config['username'], config['hostname'])
    gui.root.mainloop()
    logger.save()
