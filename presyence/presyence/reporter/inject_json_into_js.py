import json


def inject_payload(
    content,
    payload,
    begin_payload="beginPayload:!0,",
    end_payload=",endPayload:!0"
):
    """inject into `content` a json dumps of the `payload` between `begin_payload` and `end_payload`"""
    # locate the start and end of the placeholder
    start_placeholder = content.index(begin_payload) + len(begin_payload)
    end_placeholder = content.index(end_payload)
    # insert a place holder easier to replace instead of the current placeholder
    content = list(content)
    new_placeholder = "REPLACEMEPLEASE"
    content[start_placeholder:end_placeholder] = list(new_placeholder)
    content = "".join(content)
    # transform the payload into json to be inserted in the middle of another json string
    new_payload = json.dumps(
        payload, separators=(",", ":")  # separators with out whitespace to minify it
    )
    trim_first_and_last_character = lambda s: s[1:-1]  # remove `{` and `}`
    new_payload = trim_first_and_last_character(new_payload)

    # inject the stringfied payload in place of the placeholder
    content = content.replace(new_placeholder, new_payload)

    return content
