> DRAFT, not ready. Refresh against the current server state before use.

# Codex kickoff (draft): Immich go-live + photo sorting
Bring up stacks/immich per its README (first-run.sh), attach existing photo folders as read-only external libraries, and write scripts/immich-sort.py: after faces are named, COPY (never move) assets with persons Michael+Alicia and Alicia-only into /mnt/user/photos/sorted/<group>/, and split by EXIF Make/Model into /mnt/user/photos/by-camera/. Dry-run first, print counts, then wait for Michael's go.
