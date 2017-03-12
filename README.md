# Script to find orphaned Zotero attachments
Zotero Often leaves files attatched to none of the database entries (due to connectivity issues during sync or other problems). This script finds these entries and prints their names to stdout.

## Usage
The script only prints the orphaned directory names. To actually purge them, run in the zotero/storage directory
`python path-to-script/ZoteroCleanOrphanedFiles.py | xargs rm -r`

## History
I initially posted the script [on the Zotero forum](https://forums.zotero.org/discussion/comment/215096/#Comment_215096).
