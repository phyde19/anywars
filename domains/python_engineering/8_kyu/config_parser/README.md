# Config Parser (8 kyu)

## Challenge Description

Create a simple, robust configuration file parser that loads settings from a basic config file format. This is a common task in applications that need to store user preferences, application settings, or environment-specific configurations.

## Requirements

1. Create a function `parse_config(file_path: str) -> dict[str, Any]` that reads a configuration file and returns its contents as a dictionary (using `Any` from the `typing` module)
2. The configuration file format is a simple key-value pair per line, separated by `=`
3. Handle basic data types:
   - Strings (default, no special handling needed)
   - Integers (convert string like "42" to integer 42)
   - Floats (convert string like "3.14" to float 3.14)
   - Booleans (convert "true"/"false" to True/False, case-insensitive)
4. Skip empty lines and lines starting with `#` (comments)
5. Handle whitespace gracefully (trim whitespace around keys and values)
6. Implement proper error handling for missing files or parsing errors

Note: Use modern Python type annotations (Python 3.10+) as shown in the function signature.

## Input/Output Examples

Given a config file `settings.conf` with these contents:

```
# Application settings
app_name = My Application
version = 1.2
debug_mode = true
max_connections = 10

# User preferences
theme = dark
font_size = 12.5
```

Your function should return:

```python
{
    "app_name": "My Application",
    "version": 1.2,
    "debug_mode": True,
    "max_connections": 10,
    "theme": "dark",
    "font_size": 12.5
}
```

## Error Handling

1. If the file doesn't exist, raise a `FileNotFoundError` with a helpful message
2. If a line has an invalid format (doesn't contain `=`), ignore it and continue
3. Log a warning for ignored lines (but don't halt execution)

## Notes

- Focus on readability and robustness
- Handle edge cases gracefully
- Use proper error handling techniques
- Consider how the function would be used in a real application

## Testing

Your solution will be tested with different configuration files including edge cases like:
- Empty files
- Files with only comments
- Lines with multiple `=` characters
- Invalid data type conversions
