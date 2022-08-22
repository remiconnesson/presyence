"""
First we must find the target because the name will change.
For example, right now it's `worker.a1038a5f.js`.
But next build it won't be the same.

Though it will always starter with `worker` and end with `.js`

Once the target is found, we'll need to locate in the file the placeholder for the payload.
Currently, it looks like this:

In the file `frontend/dist/assets/worker.a1038a5f.js`
```javascript
var e={beginPayload:!0,prefix:"AS IN THE SOURCE",endPayload:!0};
```
So the idea is:
1. to locate the strings `{beginPayload:!0,` and `endPayload:!0}`,
2. to delete what is in between
3. to inject the data we want to use in the frontend
"""

from pathlib import Path

asset_folder = Path('.') / "frontend" / "dist" / "assets"

for f in asset_folder.iterdir():
    if f.name.startswith("worker"):
        with open(f) as target_file:
            content = target_file.read()
            print(content);


        # insert a place holder easier to replace
        begin_payload, end_payload = "beginPayload:!0,", ",endPayload:!0"
        start_placeholder = content.index(begin_payload) + len(begin_payload)
        end_placeholder = content.index(end_payload)
        content = list(content)
        new_placeholder = str(hash("REPLACEMEPLEASE")) * 10
        content[start_placeholder:end_placeholder] = list(new_placeholder)
        content = "".join(content)

        print(content)

        """
        with open(f, 'w') as target_file:
            content = content.replace('AS IN THE SOURCE', 'PYTHON WAS HERE')
            target_file.write(content);
        """
