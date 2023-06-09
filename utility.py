from config_parser import *

user_config_file = get_attr('user_config.ini', 'user_config_file')

print(f"{'-' * 15} Running test.py {'-' * 15}")
print(user_config_file)
