import xml.etree.ElementTree as ET
from datetime import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.root = ET.Element("log")

    def log_action(self, user, action):
        entry = ET.SubElement(self.root, "entry")
        user_elem = ET.SubElement(entry, "user")
        user_elem.text = user
        action_elem = ET.SubElement(entry, "action")
        action_elem.text = action
        time_elem = ET.SubElement(entry, "time")
        time_elem.text = datetime.now().isoformat()

    def save(self):
        tree = ET.ElementTree(self.root)
        tree.write(self.log_file)
