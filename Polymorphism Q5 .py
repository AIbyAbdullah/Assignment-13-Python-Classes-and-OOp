'''
Q5. Notification Dispatcher | Beginner
Create EmailNotification, SMSNotification, and PushNotification classes. Each must implement send(message)
with output specific to its channel. Write a single function notify_all(notifications, message) that iterates through
different notification objects and invokes send(). Add a WhatsAppNotification class without changing the
dispatcher. Explain where polymorphism occurs.
'''
class EmailNotification:
    def send(self, message):
        return f"Email Sent: {message}"

class SMSNotification:
    def send(self, message):
        return f"SMS Sent: {message}"
class PushNotification:
    def send(self, message):
        return f"Push Notification: {message}"

class WhatsAppNotification:
    def send(self, message):
        return f"WhatsApp Sent: {message}"

def notify_all(notifications, message):
    for n in notifications:
        print(n.send(message))

# --- Demo ---
print("--- Notification Dispatcher ---")
notification = [
    EmailNotification(),
      SMSNotification(), 
      PushNotification(), 
      WhatsAppNotification()
      ]
notify_all(notification, "Your order is confirmed.")

