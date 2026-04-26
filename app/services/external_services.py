import requests

def call_payment_service(patient_id, amount):
    url = "http://localhost:8002/v1/payments/"
    
    payload = {
        "patient_id": patient_id,
        "amount": amount,
        "idempotency_key": f"txn_{patient_id}"
    }

    try:
        response = requests.post(url, json=payload)

        print("PAYMENT STATUS:", response.status_code)
        print("PAYMENT RESPONSE:", response.text)

        return response.json()
    
    except Exception as e:
        print("PAYMENT ERROR:", str(e))
        return {"error": "Payment service failed"}


def call_notification_service(email, message):
    url = "http://localhost:8001/v1/notifications/"

    payload = {
        "recipient": email,
        "message": message,
        "type": "EMAIL"
    }

    try:
        response = requests.post(url, json=payload)

        print("NOTIFICATION STATUS:", response.status_code)
        print("NOTIFICATION RESPONSE:", response.text)

        return response.json()
    
    except Exception as e:
        print("NOTIFICATION ERROR:", str(e))
        return {"error": "Notification service failed"}