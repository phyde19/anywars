import os
import tempfile
import unittest
from config_parser import parse_config

class TestConfigParser(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
    
    def tearDown(self):
        # Clean up temporary file
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_basic_parsing(self):
        # Write test config to file
        with open(self.temp_file.name, 'w') as f:
            f.write("# Application settings\n")
            f.write("app_name = My Application\n")
            f.write("version = 1.2\n")
            f.write("debug_mode = true\n")
            f.write("max_connections = 10\n")
            f.write("\n")
            f.write("# User preferences\n")
            f.write("theme = dark\n")
            f.write("font_size = 12.5\n")
        
        # Parse the config file
        config = parse_config(self.temp_file.name)
        
        # Check that all values were parsed correctly
        self.assertEqual(config['app_name'], "My Application")
        self.assertEqual(config['version'], 1.2)
        self.assertEqual(config['debug_mode'], True)
        self.assertEqual(config['max_connections'], 10)
        self.assertEqual(config['theme'], "dark")
        self.assertEqual(config['font_size'], 12.5)
    
    def test_empty_file(self):
        # Test with an empty file
        with open(self.temp_file.name, 'w') as f:
            f.write("")
        
        config = parse_config(self.temp_file.name)
        self.assertEqual(config, {})
    
    def test_comments_only(self):
        # Test with a file containing only comments
        with open(self.temp_file.name, 'w') as f:
            f.write("# This is a comment\n")
            f.write("# Another comment\n")
        
        config = parse_config(self.temp_file.name)
        self.assertEqual(config, {})
    
    def test_file_not_found(self):
        # Test handling of non-existent file
        with self.assertRaises(FileNotFoundError):
            parse_config("non_existent_file.conf")

if __name__ == '__main__':
    unittest.main()
