import yaml
import pprint

def read_yaml():
    """ A function to read YAML file"""
    with open('config.yml') as f:
        config = yaml.safe_load(f)

    return config


def write_yaml(data):
    """ A function to write YAML file"""
    with open('toyaml.yml', 'w') as f:
        yaml.dump(data, f)


if __name__ == "__main__":

    # read the config yaml
    my_config = read_yaml()

    # pretty print my_config
    pprint.pprint(my_config)

    # write A python object to a file
    write_yaml(my_config)
