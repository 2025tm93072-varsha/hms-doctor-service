import requests
import os

# ✅ Dynamic URLs (local fallback + docker override)
PAYMENT_URL = os.getenv(
    "PAYMENT_URL",
    "http://localhost:9006/v1/payments/"
)

NOTIFICATION_URL = os.getenv(
    "NOTIFICATION_URL",
    "http://localhost:9007/v1/notifications/"
)


def call_payment_service(patient_id, amount):
    payload = {
        "patient_id": patient_id,
        "amount": amount,
        "idempotency_key": f"txn_{patient_id}"
    }

    try:
        response = requests.post(PAYMENT_URL, json=payload)

        print("PAYMENT URL:", PAYMENT_URL)
        print("PAYMENT STATUS:", response.status_code)
        print("PAYMENT RESPONSE:", response.text)

        # Raise error if response is not 200
        response.raise_for_status()

        return response.json()

    except Exception as e:
        print("PAYMENT ERROR:", str(e))
        return {"error": "Payment service failed"}


def call_notification_service(email, message):
    payload = {
        "recipient": email,
        "message": message,
        "type": "EMAIL"
    }

    try:
        response = requests.post(NOTIFICATION_URL, json=payload)

        print("NOTIFICATION URL:", NOTIFICATION_URL)
        print("NOTIFICATION STATUS:", response.status_code)
        print("NOTIFICATION RESPONSE:", response.text)

        response.raise_for_status()

        return response.json()

    except Exception as e:
        print("NOTIFICATION ERROR:", str(e))
        return {"error": "Notification service failed"}