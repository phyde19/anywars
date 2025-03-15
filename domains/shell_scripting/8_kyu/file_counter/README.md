# File Counter (8 kyu)

## Challenge Description

Create a Bash script that counts the number of files in a directory, grouped by file extension. This is a common task when organizing files or analyzing directory contents.

## Requirements

1. Your script should accept a directory path as an argument
2. If no argument is provided, use the current directory
3. Count all files (not directories) and group them by their extension
4. Display the count for each extension, sorted alphabetically by extension
5. Files with no extension should be counted under the category "(no extension)"
6. Hidden files (starting with '.') should be included in the count
7. Subdirectories should NOT be traversed

## Input/Output Examples

Given a directory with these files:
```
example/
  ├── document1.txt
  ├── document2.txt
  ├── image.jpg
  ├── script.sh
  ├── notes
  ├── .hidden.txt
  └── subdir/
      └── file.txt
```

Your script should output:
```
jpg: 1
sh: 1
txt: 3
(no extension): 1
```

## Notes

- You can use standard Unix tools like `find`, `grep`, `sort`, `awk`, etc.
- Make sure your script handles errors gracefully
- Focus on readability and correctness first, then optimization
- Don't forget to make your script executable (`chmod +x file_counter.sh`)
