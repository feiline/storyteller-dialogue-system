import logging
import os


def set_logger(level, output_filename=None):
    # remove all existing handlers associated with the root logger object
    # useful to avoid using the formatting options picked by imported libraries (e.g tensorflow)
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    # configure new logger
    if output_filename is not None:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    formatting_string = '%(levelname)s - %(asctime)s - %(process)d - ' \
                        '%(filename)s - %(message)s'
    logging.basicConfig(filename=output_filename, level=level,
                        format=formatting_string)
    # configure logging to console alongside with logging file
    if output_filename is not None:
        console = logging.StreamHandler()
        console.setLevel(level)
        formatter = logging.Formatter(formatting_string)
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)