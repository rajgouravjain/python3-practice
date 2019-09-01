import yaml
import argparse

def load_config(conf_file: str = 'alert_generator_config.yaml') -> dict :
    with open(conf_file,'r') as f:
        conf = yaml.safe_load(f)
    return conf

def parse_config():
    parsed_config = {}
    parser = argparse.ArgumentParser(description='Alert Generator config parser')
    parser.add_argument('--config', action='store',dest='config', help = "Configuration file for alert generator")

    parsed_args = parser.parse_args()

    if  parsed_args.config :
        return load_config(parsed_args.config)
    else :
        return load_config()
