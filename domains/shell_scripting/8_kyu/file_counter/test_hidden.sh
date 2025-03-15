#!/bin/bash

# Test 1: Empty directory
EMPTY_DIR="test_empty"
rm -rf "$EMPTY_DIR" 2>/dev/null
mkdir -p "$EMPTY_DIR"

echo "Test 1: Empty directory"
RESULT=$(./file_counter.sh "$EMPTY_DIR")
if [ -z "$RESULT" ]; then
  echo "PASS: Correctly handled empty directory"
else
  echo "FAIL: Expected no output for empty directory, got: $RESULT"
fi

# Test 2: Directory with only files without extensions
NO_EXT_DIR="test_no_ext"
rm -rf "$NO_EXT_DIR" 2>/dev/null
mkdir -p "$NO_EXT_DIR"
touch "$NO_EXT_DIR/file1"
touch "$NO_EXT_DIR/file2"
touch "$NO_EXT_DIR/file3"

echo "\nTest 2: Files without extensions"
RESULT=$(./file_counter.sh "$NO_EXT_DIR")
EXPECTED="(no extension): 3"
if [ "$RESULT" == "$EXPECTED" ]; then
  echo "PASS: Correctly counted files without extensions"
else
  echo "FAIL: Expected '$EXPECTED', got: '$RESULT'"
fi

# Test 3: Directory with files that have same name but different cases in extensions
MIXED_CASE_DIR="test_mixed_case"
rm -rf "$MIXED_CASE_DIR" 2>/dev/null
mkdir -p "$MIXED_CASE_DIR"
touch "$MIXED_CASE_DIR/file1.txt"
touch "$MIXED_CASE_DIR/file2.TXT"
touch "$MIXED_CASE_DIR/file3.Txt"

echo "\nTest 3: Mixed case extensions"
RESULT=$(./file_counter.sh "$MIXED_CASE_DIR" | sort)
EXPECTED=$(echo -e "TXT: 1\nTxt: 1\ntxt: 1" | sort)
if [ "$RESULT" == "$EXPECTED" ]; then
  echo "PASS: Correctly handled case-sensitive extensions"
else
  echo "FAIL: Expected case sensitivity in extensions"
  echo "Expected: $EXPECTED"
  echo "Got: $RESULT"
fi

# Test 4: Directory with files that have multiple dots in filename
MULTI_DOT_DIR="test_multi_dot"
rm -rf "$MULTI_DOT_DIR" 2>/dev/null
mkdir -p "$MULTI_DOT_DIR"
touch "$MULTI_DOT_DIR/file.tar.gz"
touch "$MULTI_DOT_DIR/archive.tar.bz2"
touch "$MULTI_DOT_DIR/script.v1.2.sh"

echo "\nTest 4: Multiple dots in filenames"
RESULT=$(./file_counter.sh "$MULTI_DOT_DIR" | sort)
EXPECTED=$(echo -e "bz2: 1\ngz: 1\nsh: 1" | sort)
if [ "$RESULT" == "$EXPECTED" ]; then
  echo "PASS: Correctly handled multiple dots in filenames"
else
  echo "FAIL: Expected to count only the last extension in files with multiple dots"
  echo "Expected: $EXPECTED"
  echo "Got: $RESULT"
fi

# Test 5: Nonexistent directory
echo "\nTest 5: Nonexistent directory"
./file_counter.sh "nonexistent_directory" 2>&1 | grep -q "Error"
if [ $? -eq 0 ]; then
  echo "PASS: Error message shown for nonexistent directory"
else
  echo "FAIL: No appropriate error handling for nonexistent directory"
fi

# Clean up test directories
rm -rf "$EMPTY_DIR" "$NO_EXT_DIR" "$MIXED_CASE_DIR" "$MULTI_DOT_DIR"
