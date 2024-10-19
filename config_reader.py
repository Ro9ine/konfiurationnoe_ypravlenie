import os ,csv

def read_config(config_file):
    config_file=os.path.join("./",config_file)
    config = {}
    with open(config_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            config['username'] = row['username']
            config['hostname'] = row['hostname']
            config['tar_path'] = row['tar_path']
            config['log_path'] = row['log_path']
            config['startup_script'] = row['startup_script']
    print(config)
    return config
