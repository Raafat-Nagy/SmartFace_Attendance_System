import requests


def send_attendance(hall_id: int = 1, student_tag: str = "20812025000000"):
    """
    Sends a GET request to the attendance API with the given hall ID and student tag.

    Args:
        hall_id (int): The ID of the lecture hall.
        student_tag (str): The unique student identifier.

    Returns:
        dict | None: Response JSON if successful, otherwise None.
    """
    url = f"https://nextgenedu-database.azurewebsites.net/api/attendance/{hall_id}/{student_tag}"

    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print("Success:", response.json())
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None
