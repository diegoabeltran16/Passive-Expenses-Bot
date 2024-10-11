import yaml
import os

# Define the path to the config file relative to this script
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.yaml')

# Cache the config data to avoid loading it multiple times
_config_data = None

def load_config():
    """
    Loads the configuration file into memory if it hasn't been loaded yet.
    """
    global _config_data
    if _config_data is None:
        with open(CONFIG_PATH, 'r') as config_file:
            _config_data = yaml.safe_load(config_file)
    return _config_data

def get_config(key, default=None):
    """
    Fetches a configuration value from the config file based on the provided key.
    """
    config = load_config()
    keys = key.split('.')
    value = config
    try:
        for k in keys:
            value = value[k]
        return value
    except KeyError:
        return default
