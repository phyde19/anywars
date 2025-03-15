#!/bin/bash

# Create test directory structure
TEST_DIR="test_dir"
rm -rf "$TEST_DIR" 2>/dev/null
mkdir -p "$TEST_DIR/subdir"

# Create test files
touch "$TEST_DIR/document1.txt"
touch "$TEST_DIR/document2.txt"
touch "$TEST_DIR/image.jpg"
touch "$TEST_DIR/script.sh"
touch "$TEST_DIR/notes"
touch "$TEST_DIR/.hidden.txt"
touch "$TEST_DIR/subdir/file.txt"

# Make solution executable
chmod +x file_counter.sh

# Run the test
echo "Running test with test directory..."
echo "Expected output:"
cat << EOF
jpg: 1
sh: 1
txt: 3
(no extension): 1
EOF

echo "\nYour output:"
./file_counter.sh "$TEST_DIR"

# Clean up
rm -rf "$TEST_DIR"
