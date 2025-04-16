
# Sample Message Parser

MHE_DELIMITER = '^'
MHE_PREFIX = '<STX>'
MHE_SUFFIX = '<ETX>'

MHE_FIELDS_REQUIRED = []
MHE_FIELDS_ALLOWED = ["TEST", "TEST2"]

def parse_message(message: str, delimiter: str = None, prefix: str = None, suffix: str = None) -> dict:

    delimiter = MHE_DELIMITER
    prefix = MHE_PREFIX
    suffix = MHE_SUFFIX

    message = message.strip()

    # Validate prefix/suffix.
    if not (message.startswith(prefix) and message.endswith(suffix)):
        raise ValueError(f"Message must start with {prefix} and end with {suffix}: {message}")
    
    # Strip prefix/suffix.
    content = message[len(prefix):-len(suffix)].strip()
    fields = content.split(delimiter)

    # Otherwise, continue to parse message.
    response = {}

    for i in range(0, len(fields), 2):
        key = fields[i].strip()
        value = fields[i + 1].strip()

        # Validate if keyword is valid and is in the allowed list.
        if key not in MHE_FIELDS_ALLOWED:
            raise ValueError(f"Invalid keyword '{key}' found in message: {message}")

        # Add to the response dictionary.
        response[key] = value

    # Validate if all required fields are present.
    missing_fields = [field for field in MHE_FIELDS_REQUIRED if field not in response]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    return response
