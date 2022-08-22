"""
First we must find the target because the name will change.
For example, right now it's `worker.a1038a5f.js`.
But next build it won't be the same.

Though it will always starter with `worker` and end with `.js`
"""
from pathlib import Path

asset_folder = Path('.') / "frontend" / "dist" / "assets"

for f in asset_folder.iterdir():
    print(f.name);
"""
Once the target is found, we'll need to locate in the file the placeholder for the payload.
Currently, it looks like this:

In the file `frontend/dist/assets/worker.a1038a5f.js`
```javascript
var e={beginPayload:!0,prefix:"AS IN THE SOURCE",endPayload:!0};
```
So the idea is:
1. to locate the strings `{begingPayload:!0,` and `endPayload:!0}`,
2. to delete what is in between
3. to inject the data we want to use in the frontend
"""

