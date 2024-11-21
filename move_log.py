class MoveLog:
    def __init__(self):

        "An empty list to store moves."

        self.log = []

    def add_move(self, move):
        """
        Adds a move to the log.
        A string or object representing the move (e.g., 'e2 to e4').
        """
        self.log.append(move)

    def get_log(self):
        """
        Returns the current move log.
        A list of moves.
        """
        return self.log

    def undo_last_move(self):
        
        "Removes the last move from the log."
        
        if self.log:
            return self.log.pop()
        return None

    def clear_log(self):
       
        "Clears all moves from the log."
        
        self.log = []

    def display_log(self):
        
        "Displays the move log in a readable format."
        
        print("Move Log:")
        for i, move in enumerate(self.log, start=1):
            print(f"{i}. {move}")
