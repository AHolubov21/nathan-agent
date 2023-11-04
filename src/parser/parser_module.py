import json

class Parser:
    def __init__(self):
        pass

    def parse_event(self, event):
        """
        Parse the input event.

        Args:
        - event (str): The input event as a string.

        Returns:
        - dict: Parsed event as a dictionary.
        """
        try:
            parsed_event = json.loads(event)
            return parsed_event
        except json.JSONDecodeError:
            raise ValueError("Unable to parse the event.")

    def extract_key_values(self, parsed_event, keys):
        """
        Extract specific key-values from the parsed event.

        Args:
        - parsed_event (dict): The parsed event.
        - keys (list): List of keys to extract values for.

        Returns:
        - dict: Dictionary containing the extracted key-value pairs.
        """
        extracted_data = {}
        for key in keys:
            if key in parsed_event:
                extracted_data[key] = parsed_event[key]
        return extracted_data

    def transform_event(self, extracted_data):
        """
        Transform the extracted data if necessary.

        Args:
        - extracted_data (dict): Extracted data from the parsed event.

        Returns:
        - dict: Transformed data.
        """
        # Sample transformation: convert all strings to upper case.
        transformed_data = {k: v.upper() if isinstance(v, str) else v for k, v in extracted_data.items()}
        return transformed_data

if __name__ == "__main__":
    parser = Parser()
    event = '{"id": "123", "name": "Nathan", "status": "active"}'
    parsed_event = parser.parse_event(event)
    extracted_data = parser.extract_key_values(parsed_event, ["id", "name"])
    transformed_data = parser.transform_event(extracted_data)
    print(transformed_data)
