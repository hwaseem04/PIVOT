#!/usr/bin/env bash
set -euo pipefail

REMOTE="gdrive"
SRC="${REMOTE}:Paper2VideoV2"
DEST="${REMOTE}:final"

echo "Creating destination folder: ${DEST}"
rclone mkdir "${DEST}"

echo "Listing all PDF/MP4 files under ${SRC} ..."
# rclone lsf outputs file paths relative to SRC.
# --filter keeps it deterministic and avoids the include/exclude warning.
rclone lsf "${SRC}" -R --files-only \
  --filter "+ *.pdf" \
  --filter "+ *.mp4" \
  --filter "- *" \
  > /tmp/rclone_paper2video_files.txt

count=$(wc -l < /tmp/rclone_paper2video_files.txt | tr -d ' ')
if [ "$count" -eq 0 ]; then
  echo "No .pdf or .mp4 files found under ${SRC}."
  exit 0
fi

echo "Found ${count} files. Copying into ${DEST} with collision-safe names..."

copied=0
failed=0

while IFS= read -r rel; do
  # Skip empty lines just in case
  [ -z "$rel" ] && continue

  base="$(basename "$rel")"
  dir="$(dirname "$rel")"

  # Make destination name collision-safe by prefixing folder path
  if [ "$dir" = "." ]; then
    out="$base"
  else
    safe_prefix=$(printf "%s" "$dir" | tr '/' '_' )
    out="${safe_prefix}__${base}"
  fi

  src_path="${SRC}/${rel}"
  dest_path="${DEST}/${out}"

  echo "  -> $rel  ==>  $out"

  if rclone copyto "${src_path}" "${dest_path}" \
      --ignore-existing \
      --drive-server-side-across-configs; then
    copied=$((copied+1))
  else
    echo "     WARNING: failed copying: ${rel}"
    failed=$((failed+1))
  fi
done < /tmp/rclone_paper2video_files.txt

echo "Done. Copied: ${copied}, Failed: ${failed}"
echo "Destination: ${DEST}"

