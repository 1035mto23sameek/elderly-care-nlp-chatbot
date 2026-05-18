# SIMPLE IN-MEMORY CONVERSATION STORAGE

conversation_memory = {}


def save_message(session_id, role, message):

    if session_id not in conversation_memory:

        conversation_memory[session_id] = []

    conversation_memory[session_id].append({

        "role": role,

        "message": message
    })


def get_conversation_history(session_id):

    return conversation_memory.get(session_id, [])


def get_last_messages(session_id, limit=5):

    history = get_conversation_history(session_id)

    return history[-limit:]