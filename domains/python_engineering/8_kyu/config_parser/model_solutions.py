"""
Model solutions for the Config Parser challenge.
This file contains different approaches to solving the challenge,
from straightforward to more advanced techniques.
"""

from typing import Any, Dict, Union, Callable, TypeVar
import re
import logging


# Solution 1: Simple and Straightforward
def parse_config_simple(file_path: str) -> dict[str, Any]:
    """A simple, straightforward solution using basic string operations."""
    result = {}
    
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                # Check for key-value separator
                if '=' not in line:
                    logging.warning(f"Line {line_num} has invalid format (missing '='): {line}")
                    continue
                
                # Split into key and value
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Handle quoted values
                if (value.startswith('"') and value.endswith('"')) or \
                   (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]
                else:
                    # Convert to appropriate type if not quoted
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    else:
                        # Try to convert to int or float
                        try:
                            if '.' in value:
                                value = float(value)
                            else:
                                value = int(value)
                        except ValueError:
                            # Keep as string if conversion fails
                            pass
                
                result[key] = value
                
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {file_path}")
        
    return result


# Solution 2: Using Regular Expressions
def parse_config_regex(file_path: str) -> dict[str, Any]:
    """A solution using regular expressions for more robust parsing."""
    result = {}
    # Pattern to match key-value pairs with proper handling of quotes
    pattern = r'^\s*([^#=\s][^=]*?)\s*=\s*(.*?)\s*$'
    
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                # Try to match the pattern
                match = re.match(pattern, line)
                if not match:
                    logging.warning(f"Line {line_num} has invalid format: {line}")
                    continue
                
                key, value = match.groups()
                
                # Handle quoted values
                if re.match(r'^["\'](.*)["\']$', value):
                    # Remove the quotes and keep as string
                    value = re.match(r'^["\'](.*)["\'](.*?)$', value).group(1)
                else:
                    # Type conversion for unquoted values
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    else:
                        # Try numeric conversion
                        try:
                            if '.' in value:
                                value = float(value)
                            else:
                                value = int(value)
                        except ValueError:
                            pass
                
                result[key] = value
                
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {file_path}")
        
    return result


# Solution 3: Using a Parser Combinators Approach
T = TypeVar('T')

def parse_config_functional(file_path: str) -> dict[str, Any]:
    """A more functional approach using parser combinators pattern."""
    # Type converters
    def try_convert(value: str) -> Any:
        """Try to convert a string to a more specific type."""
        # Check for quoted values
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            return value[1:-1]
        
        # Boolean conversion
        if value.lower() == 'true':
            return True
        if value.lower() == 'false':
            return False
        
        # Numeric conversion
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value
    
    # Line parsers
    def parse_line(line: str, line_num: int) -> tuple[bool, tuple[str, Any] | None]:
        """Parse a single line of the config file."""
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            return (True, None)
        
        # Check for key-value separator
        if '=' not in line:
            logging.warning(f"Line {line_num} has invalid format (missing '='): {line}")
            return (True, None)
        
        # Split and process
        key, value = line.split('=', 1)
        return (True, (key.strip(), try_convert(value.strip())))
    
    # Main function logic
    result = {}
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                success, parsed = parse_line(line, line_num)
                if success and parsed:
                    key, value = parsed
                    result[key] = value
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {file_path}")
        
    return result


# Solution 4: Using a Class-Based Approach
class ConfigParser:
    """Class-based implementation of a config parser."""
    
    def __init__(self):
        self.config: dict[str, Any] = {}
    
    def parse(self, file_path: str) -> dict[str, Any]:
        """Parse a configuration file and return its contents."""
        try:
            with open(file_path, 'r') as file:
                self._parse_file(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {file_path}")
        
        return self.config
    
    def _parse_file(self, file) -> None:
        """Process the file contents line by line."""
        for line_num, line in enumerate(file, 1):
            self._parse_line(line, line_num)
    
    def _parse_line(self, line: str, line_num: int) -> None:
        """Parse a single line from the config file."""
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            return
        
        # Check for key-value separator
        if '=' not in line:
            logging.warning(f"Line {line_num} has invalid format (missing '='): {line}")
            return
        
        # Split into key and value
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()
        
        # Process value
        value = self._process_value(value)
        
        # Store in config
        self.config[key] = value
    
    def _process_value(self, value: str) -> Any:
        """Convert the value to the appropriate type."""
        # Handle quoted values
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            return value[1:-1]
        
        # Handle boolean values
        if value.lower() == 'true':
            return True
        if value.lower() == 'false':
            return False
        
        # Handle numeric values
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            # If conversion fails, keep as string
            return value


def parse_config_class_based(file_path: str) -> dict[str, Any]:
    """Wrapper function for the class-based implementation."""
    parser = ConfigParser()
    return parser.parse(file_path)


# Solution 5: A more pythonic solution using list comprehensions
def parse_config_pythonic(file_path: str) -> dict[str, Any]:
    """A more concise, pythonic solution using list comprehensions."""
    
    def convert_value(value: str) -> Any:
        """Convert a string value to the appropriate type."""
        value = value.strip()
        
        # Handle quoted values
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            return value[1:-1]
        
        # Handle boolean values
        if value.lower() == 'true':
            return True
        if value.lower() == 'false':
            return False
        
        # Handle numeric values
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value
    
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file]
            
            # Filter out empty lines and comments
            lines = [line for line in lines if line and not line.startswith('#')]
            
            # Process valid lines
            result = {}
            for i, line in enumerate(lines):
                if '=' in line:
                    key, value = line.split('=', 1)
                    result[key.strip()] = convert_value(value)
                else:
                    logging.warning(f"Line {i+1} has invalid format (missing '='): {line}")
            
            return result
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {file_path}")