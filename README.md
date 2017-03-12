# Script to find orphaned Zotero attachments
Often Zotero leaves files attached to none of the entries in the database due to connectivity issues during sync or other problems. This script finds these entries and prins theire names to stdout.

## Usage
The script only prints the orphaned dirnames. To actually purge them, run in the zotero/storage directory

`python path-to-script/ZoteroCleanOrphanedFiles.py | xargs rm -r`

## History
I initially posted the script [on the Zotero forum](https://forums.zotero.org/discussion/comment/215096/#Comment_215096).
