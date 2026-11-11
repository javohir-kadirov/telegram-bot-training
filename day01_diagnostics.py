users = [
    {
        "user_id": 101,
        "name": "Ali",
        "is_active": True,
        "messages_count": 4,
    },
    {
        "user_id": 102,
        "name": "Malika",
        "is_active": False,
        "messages_count": 7,
    },
    {
        "user_id": 103,
        "name": "Sardor",
        "is_active": True,
        "messages_count": 2
    }
]

def find_user(users_list, user_id):
    for user in users_list:
        if user["user_id"] == user_id:
            return user
    return None

def build_stats(users_list):
    active_users = 0
    inactive_users = 0
    total_messages = 0

    max_messages = -1
    most_active_user_id = None

    total_users = len(users_list)

    for user in users_list:
        if user["is_active"]:
            active_users += 1
        else:
            inactive_users += 1
        total_messages += user["messages_count"]
        if user["messages_count"] > max_messages:
            max_messages = user["messages_count"]
            most_active_user_id = user["user_id"] 

    return {
        "total_users": total_users, 
        "active_users": active_users,
        "inactive_users": inactive_users,
        "total_messages": total_messages, 
        "most_active_user_id": most_active_user_id,
    }     


result_find = find_user(users, 000)
print(result_find)

result_stats = build_stats(users)
print(result_stats)


class SupportTicket:
    def __init__(self, ticket_id, user_id, message):
        self.ticket_id = ticket_id
        self.user_id = user_id
        self.message = message
        self.__status = "open"

    def get_status(self):
        return self.__status

    def close(self):
        self.__status = "closed"


ticket = SupportTicket(1, 101, "I can't sign in account")

print(ticket.get_status())

ticket.close()

print(ticket.get_status())

ticket.close()

print(ticket.get_status())