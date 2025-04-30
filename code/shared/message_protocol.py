# /code/shared/message_protocol.py

import datetime

def create_message(sender, recipient, intent, task, context=None):
    return {
        "sender": sender,
        "recipient": recipient,
        "intent": intent,
        "task": task,
        "context": context or {},
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

def parse_message(message):
    try:
        return {
            "from": message["sender"],
            "to": message["recipient"],
            "intent": message["intent"],
            "task": message["task"],
            "context": message.get("context", {}),
            "timestamp": message["timestamp"]
        }
    except KeyError as e:
        raise ValueError(f"Invalid message format: missing {e}")
