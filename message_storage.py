# Message storage implementation
# I'm implementing different ways to store messages to compare their performance

from collections import defaultdict
from datetime import datetime
import time

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = datetime.now()

# First approach: using a simple list
class ListStorage:
    def __init__(self):
        self.messages = []
    
    def add_message(self, message):
        self.messages.append(message)
    
    def get_message(self, index):
        if 0 <= index < len(self.messages):
            return self.messages[index]
        return None

# Second approach: using a hash table (dictionary)
class DictionaryStorage:
    def __init__(self):
        # Using defaultdict to automatically create lists for new conversations
        self.messages = defaultdict(list)
    
    def add_message(self, conversation_id, message):
        self.messages[conversation_id].append(message)
    
    def get_messages(self, conversation_id):
        return self.messages.get(conversation_id, [])

def test_performance():
    print("\nTesting Different Storage Methods:")
    print("-" * 40)
    
    # Test list storage
    list_storage = ListStorage()
    start = time.time()
    for i in range(1000):
        list_storage.add_message(Message("me", f"test message {i}"))
    list_time = (time.time() - start) * 1000
    
    # Test dictionary storage
    dict_storage = DictionaryStorage()
    start = time.time()
    for i in range(1000):
        dict_storage.add_message("chat1", Message("me", f"test message {i}"))
    dict_time = (time.time() - start) * 1000
    
    print(f"List Storage Time: {list_time:.2f}ms")
    print(f"Dictionary Storage Time: {dict_time:.2f}ms")

if __name__ == "__main__":
    print("My Message Storage Analysis")
    print("\nI implemented two different approaches:")
    print("1. List Storage:")
    print("   - Simple array-like storage")
    print("   - Good for small number of messages")
    print("   - Easy to implement")
    
    print("\n2. Dictionary Storage:")
    print("   - Hash table based")
    print("   - Better for organizing by conversation")
    print("   - Faster lookups")
    
    test_performance()
    
    print("\nConclusion:")
    print("- List storage is simpler but slower for large datasets")
    print("- Dictionary storage is better for real chat apps")
    print("- I'd choose dictionary storage for a real app")
