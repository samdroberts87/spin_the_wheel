import json
import random
import re

def lambda_handler(event, context):
    # Get query string parameters
    params = event.get("queryStringParameters", {})
    items_str = params.get("items", "")

    # Convert comma-separated string to list
    items_list = [item.strip() for item in re.split(r"[,\s]+", items_str) if item.strip()]

    # Common headers (including CORS)
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"  # Enable CORS
    }

    # Check if list is not empty
    if not items_list:
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({ "error": "You must enter at least 1 name" })
        }

    # Choose a random item
    chosen = random.choice(items_list).title()

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({ "random_item": f"{chosen} has been selected" })
    }
