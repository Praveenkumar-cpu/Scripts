import requests

# Function to delete resource
def delete_resource(resource_id):
    url = f"https://polar.creditsaison.in/api/v1/event/v2/{resource_id}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic QGRNMU46UEAkJFcwckQ='
    }

    response = requests.delete(url, headers=headers)

    print(f"Deleted: {resource_id}, Status Code: {response.status_code}, Response: {response.text}")

# List of resource IDs
resource_ids = ["IM101CID10687539", "IM101CID10687540", "IM101CID10687541"]  # Add more IDs

# Loop through the list and delete each resource
for resource_id in resource_ids:
    delete_resource(resource_id)