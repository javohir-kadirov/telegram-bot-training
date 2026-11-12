def find_user(users_list: list[dict[str, int | str | bool]], user_id: int) -> dict[str, int | str | bool] | None:
    for user in users_list:
        if user["user_id"] == user_id:
            return user
    return None

def build_stats(users_list: list[dict[str, int | str | bool]]) -> dict[str, int | None] :
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