import os
import tempfile
import unittest
import logging
from io import StringIO
from config_parser import parse_config

class TestConfigParserAdvanced(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        
        # Set up logging capture
        self.log_capture = StringIO()
        self.log_handler = logging.StreamHandler(self.log_capture)
        logging.getLogger().addHandler(self.log_handler)
        logging.getLogger().setLevel(logging.WARNING)
    
    def tearDown(self):
        # Clean up temporary file
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
            
        # Clean up logging
        logging.getLogger().removeHandler(self.log_handler)
    
    def test_whitespace_handling(self):
        # Test handling of whitespace
        with open(self.temp_file.name, 'w') as f:
            f.write("key1 = value1\n")
            f.write("  key2  =  value2  \n")
            f.write("key3=value3\n")
        
        config = parse_config(self.temp_file.name)
        self.assertEqual(config['key1'], "value1")
        self.assertEqual(config['key2'], "value2")
        self.assertEqual(config['key3'], "value3")
    
    def test_data_type_conversion(self):
        # Test data type conversion
        with open(self.temp_file.name, 'w') as f:
            f.write("string = hello\n")
            f.write("integer = 42\n")
            f.write("float = 3.14159\n")
            f.write("true_value = true\n")
            f.write("false_value = false\n")
            f.write("mixed_case_bool = True\n")
        
        config = parse_config(self.temp_file.name)
        self.assertEqual(config['string'], "hello")
        self.assertEqual(config['integer'], 42)
        self.assertEqual(config['float'], 3.14159)
        self.assertEqual(config['true_value'], True)
        self.assertEqual(config['false_value'], False)
        self.assertEqual(config['mixed_case_bool'], True)
    
    def test_invalid_lines(self):
        # Test handling of invalid lines
        with open(self.temp_file.name, 'w') as f:
            f.write("valid = value\n")
            f.write("invalid line\n")
            f.write("also invalid\n")
            f.write("valid2 = value2\n")
        
        config = parse_config(self.temp_file.name)
        self.assertEqual(len(config), 2)
        self.assertEqual(config['valid'], "value")
        self.assertEqual(config['valid2'], "value2")
        
        # Check for warning logs
        log_content = self.log_capture.getvalue()
        self.assertIn("invalid format", log_content.lower())
    
    def test_multiple_equals_signs(self):
        # Test handling of lines with multiple equals signs
        with open(self.temp_file.name, 'w') as f:
            f.write("key = value = with = equals\n")
        
        config = parse_config(self.temp_file.name)
        self.assertEqual(config['key'], "value = with = equals")
    
    def test_invalid_number_conversion(self):
        # Test handling of invalid number conversions
        with open(self.temp_file.name, 'w') as f:
            f.write("invalid_int = 42a\n")
            f.write("invalid_float = 3.14.15\n")
        
        config = parse_config(self.temp_file.name)
        # Should keep as strings if conversion fails
        self.assertEqual(config['invalid_int'], "42a")
        self.assertEqual(config['invalid_float'], "3.14.15")
        
        # Check for warning logs
        log_content = self.log_capture.getvalue()
        self.assertIn("convert", log_content.lower())

if __name__ == '__main__':
    unittest.main()
