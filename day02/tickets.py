class SupportTicket:
    def __init__(self, ticket_id: int, user_id: int, message: str) -> None:
        self.ticket_id = ticket_id
        self.user_id = user_id
        self.message = message
        self.__status = "open"

    def get_status(self) -> str:
        return self.__status

    def close(self) -> None:
        self.__status = "closed"
