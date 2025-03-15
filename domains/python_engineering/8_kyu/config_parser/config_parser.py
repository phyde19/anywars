from typing import Any
from enum import Enum
import logging
import re

class ValueType(str, Enum):
    SINGLE_QUOTE = "SINGLE_QUOTE"
    DOUBLE_QUOTE = "DOUBLE_QUOTE"
    STRING = "STRING"
    INT = "INT"
    FLOAT = "FLOAT"
    BOOL = "BOOL"
    INVALID = "INVALID"

def get_value_type(value_token: str) -> ValueType:
    if not len(value_token):
        # handle empty line
        return ValueType.STRING
    
    # check for literal
    quote_types = [("\"", ValueType.DOUBLE_QUOTE), ("'", ValueType.SINGLE_QUOTE)]
    for quote_token, quote_value_type in quote_types:
        if value_token[0] == quote_token:
            # quote string detected
            if value_token.count(quote_token) != 2 or value_token[-1] != quote_token:
                # invalid quote parity or syntax, Interpret as string
                return ValueType.STRING
            return quote_value_type
    
    # check for bool
    value_lower = value_token.lower()
    if value_lower == "true" or value_lower == "false":
        return ValueType.BOOL
    
    # check for int
    if re.match(r"^-?\d+$", value_token):
        return ValueType.INT
    
    # check for float
    if value_token != "." and re.match(r"^-?\d*\.\d*$", value_token):
        return ValueType.FLOAT
    
    # default assume string type
    return ValueType.STRING


def log_invalid_format(line: str):
    msg = f"invalid format for line: {line}"
    logging.warning(msg)

def parse_line_tokens(line: str):
    split_index = line.index("=")
    key = line[:split_index].strip()
    value = line[split_index+1:].strip()
    return key, value


def parse_config(file_path: str) -> dict[str, Any]:
    """Parse a configuration file and return its contents as a dictionary.
    
    Args:
        file_path: Path to the configuration file
        
    Returns:
        Dictionary containing the parsed configuration with values converted to 
        appropriate types (str, int, float, bool)
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    config_dict = {}
    with open(file_path) as file:
        raw_lines = file.readlines()
        for raw_line in raw_lines:
            line = raw_line.strip()
            # skip if line is empty or comment
            if line == "" or line[0] == "#":
                continue
            # log if = not present in line
            if "=" not in line:
                log_invalid_format(line)
                continue
            # parse key, value tokens
            key_token, value_token = parse_line_tokens(line)
            match get_value_type(value_token):
                case ValueType.SINGLE_QUOTE | ValueType.DOUBLE_QUOTE:
                    # remove leading and trailing quotes ""
                    value = value_token[1:-1]
                case ValueType.STRING:
                    value = value_token
                case ValueType.INT:
                    value = int(value_token)
                case ValueType.FLOAT:
                    value = float(value_token)
                case ValueType.BOOL:
                    value = True if value_token.lower() == "true" else False
                case ValueType.INVALID:
                    log_invalid_format(line)
            # key is just the key_token
            # value is the parsed value based on matched value type
            key, value = key_token, value
            config_dict[key] = value
    return config_dict
