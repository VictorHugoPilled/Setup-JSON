# Basic setup config file for a project.
import json
import logging
from typing import IO, Tuple


def setup_configs(my_config: dict,
                  file_name: str = 'config',
                  file_mode: str = 'w+') -> None:
    'Setup the config file'
    with open(file=f'{file_name}.json',
              mode=file_mode, encoding='utf-8') as my_file:
        json.dump(obj=my_config, fp=my_file)


def load_json(file_name: str = 'config.json', file_mode: str = 'r') -> dict:
    'Load json file.'
    # set type of the config file
    config_file: IO[bytes]
    # load the config file
    with open(file=file_name, mode=file_mode, encoding='utf-8') as config_file:
        return json.load(fp=config_file)


def setup_logging(log_file: str, 
                  level: logging = logging.INFO,
                  filemode: str = 'w') -> logging.Logger:
    'Setup logging'
    logging.basicConfig(filename=log_file,
                        level=level,
                        filemode=filemode)  
    return logging.getLogger(__name__)


if __name__ == '__main__':

    MY_OPTION: str = 'Option'

    config: dict = {
        'dict_name': 'config',
        'email': 'echase3@gmail.com',
        'chrome_options_10': MY_OPTION, }

    experimental_options: dict = {
        'dict_name': 'experimental_options'}

    personal_info: dict = {
        'dict_name': 'personal_info',
        'first name': 'Earl',
        'last name': 'Chase'}

    config_dict: Tuple[dict, ...] = (config,
                                     experimental_options, personal_info)

    _: list = [setup_configs(dict, dict['dict_name']) for dict in config_dict]
    logger: logging.Logger = setup_logging('mybasic.log')
    logger.info('Config files setup.')