import json
import random

def lambda_handler(event, context):
    """AWS Lambda function to randomly pick a name from a list."""
    
    try:
        # Parse request body
        body = json.loads(event.get("body", "{}"))

        # Validate input
        if "names" not in body or not isinstance(body["names"], list):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Please provide a list of names."}),
            }

        names_list = body["names"]

        if not names_list:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Name list cannot be empty."}),
            }

        # Pick a random name
        chosen_name = random.choice(names_list).upper()

        return {
            "statusCode": 200,
            "body": json.dumps({"chosen": chosen_name}),
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON format."}),
        }
