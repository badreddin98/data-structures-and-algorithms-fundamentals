# Conversation management implementation
# Comparing different ways to manage chat conversations

from datetime import datetime
import heapq
from collections import OrderedDict

class Conversation:
    def __init__(self, id, participants):
        self.id = id
        self.participants = participants
        self.last_message = datetime.now()
        self.unread = 0

# First approach: simple list
class ListManager:
    def __init__(self):
        self.conversations = []
    
    def add_conversation(self, conv):
        self.conversations.append(conv)
        # Sort by most recent message
        self.conversations.sort(key=lambda x: x.last_message, reverse=True)
    
    def get_recent(self, limit=10):
        return self.conversations[:limit]

# Second approach: ordered dictionary
class DictManager:
    def __init__(self):
        self.conversations = OrderedDict()
    
    def add_conversation(self, conv):
        self.conversations[conv.id] = conv
    
    def get_conversation(self, id):
        return self.conversations.get(id)

# Third approach: priority queue
class PriorityManager:
    def __init__(self):
        self.conversations = []
    
    def add_conversation(self, conv):
        # Use negative count so higher counts are higher priority
        heapq.heappush(self.conversations, 
                      (-conv.unread, conv))
    
    def get_important(self, limit=10):
        return [conv for _, conv in 
                sorted(self.conversations)[:limit]]

def test_managers():
    print("\nTesting different managers:")
    print("-" * 40)
    
    # Create test conversations
    convs = [
        Conversation("1", ["Alice", "Bob"]),
        Conversation("2", ["Charlie", "Dave"]),
        Conversation("3", ["Eve", "Frank"])
    ]
    
    # Test list manager
    list_mgr = ListManager()
    for conv in convs:
        list_mgr.add_conversation(conv)
    print(f"List manager conversations: {len(list_mgr.get_recent())}")
    
    # Test dict manager
    dict_mgr = DictManager()
    for conv in convs:
        dict_mgr.add_conversation(conv)
    print(f"Dict manager has conv '1': {dict_mgr.get_conversation('1') is not None}")

if __name__ == "__main__":
    print("My Conversation Management Analysis")
    print("\nI tried three different approaches:")
    
    print("\n1. List Manager:")
    print("   - Simple list of conversations")
    print("   - Easy to sort by recent")
    print("   - Gets slow with many conversations")
    
    print("\n2. Dictionary Manager:")
    print("   - Hash table for quick lookups")
    print("   - Good for finding specific chats")
    print("   - Harder to keep sorted")
    
    print("\n3. Priority Queue Manager:")
    print("   - Keeps important chats at top")
    print("   - Good for unread messages")
    print("   - More complex to implement")
    
    test_managers()
    
    print("\nWhat I Learned:")
    print("- Different structures are good for different things")
    print("- I'd use Dictionary for most cases")
    print("- Priority Queue is good for notifications")
