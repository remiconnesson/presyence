import json


def inject_payload(content, payload):
    # insert a place holder easier to replace
    begin_payload, end_payload = "beginPayload:!0,", ",endPayload:!0"
    start_placeholder = content.index(begin_payload) + len(begin_payload)
    end_placeholder = content.index(end_payload)
    content = list(content)
    new_placeholder = "REPLACEMEPLEASE"
    content[start_placeholder:end_placeholder] = list(new_placeholder)
    content = "".join(content)

    new_payload = json.dumps(
        payload, separators=(",", ":")
    )  # separators with out whitespace
    trim_first_and_last_character = lambda s: s[1:-1]  # remove `{` and `}`
    new_payload = trim_first_and_last_character(new_payload)

    # inject the string in place of the placeholder
    content = content.replace(new_placeholder, new_payload)

    return content
