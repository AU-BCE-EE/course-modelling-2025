
#!/bin/bash

generated=0
skipped=0

# Use process substitution to keep variables in this shell
while read -r file; do
  pdf="${file%.xopp}.pdf"   # replace .xopp with .pdf

  if [ ! -f "$pdf" ] || [ "$file" -nt "$pdf" ]; then
    echo "Generating $pdf from $file"
    xournalpp -p "$pdf" "$file" 2>/dev/null
    generated=$((generated + 1))
  else
    echo "Skipping $file (up-to-date)"
    skipped=$((skipped + 1))
  fi
done < <(find . -type f -name "*.xopp")

echo
echo "Summary:"
echo "  PDFs generated: $generated"
echo "  Files skipped:  $skipped"

