from config_parser import *

user_config_file = get_attr('user_config.ini', 'user_config_file')

print(f"{'-' * 25} Running utility.py {'-' * 25}")
print(user_config_file)
print(f"{'-' * 70}")
