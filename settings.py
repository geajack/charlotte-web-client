import yaml

def get_blog_url():
    with open("client.config", "r") as config_file:
        config = yaml.load(config_file)
    url = config["blog"]["url"]
    return url