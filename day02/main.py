from day02.users import find_user, build_stats
from day02.tickets import SupportTicket

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

result_find = find_user(users, 101)
print(result_find)

result_stats = build_stats(users)
print(result_stats)


ticket = SupportTicket(1, 101, "I can't sign in account")

print(ticket.get_status())

ticket.close()

print(ticket.get_status())

ticket.close()

print(ticket.get_status())