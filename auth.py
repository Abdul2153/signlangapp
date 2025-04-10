import requests
from firebase_config import WEB_API_KEY

# Firebase Login Endpoint
FIREBASE_LOGIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={WEB_API_KEY}"

def login_user(email, password):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    try:
        response = requests.post(FIREBASE_LOGIN_URL, json=payload)
        result = response.json()

        if "error" in result:
            error_msg = result["error"]["message"].replace("_", " ").capitalize()
            return {"success": False, "error": error_msg}
        else:
            return {
                "success": True,
                "idToken": result["idToken"],
                "refreshToken": result["refreshToken"],
                "email": result["email"],
                "uid": result["localId"]
            }

    except Exception as e:
        return {"success": False, "error": str(e)}
