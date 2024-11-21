from move_log import MoveLog

def test_move_log():
    # Create an instance of MoveLog
    move_log = MoveLog()

    # Add some moves
    move_log.add_move("e2 to e4")
    move_log.add_move("e7 to e5")
    move_log.add_move("g1 to f3")

    # Display the current log
    print("\nTesting add_move and display_log:")
    move_log.display_log()

    # Test get_log
    log = move_log.get_log()
    print("\nTesting get_log:")
    print(log)

    # Undo the last move
    print("\nTesting undo_last_move:")
    undone_move = move_log.undo_last_move()
    print(f"Undone move: {undone_move}")
    move_log.display_log()

    # Clear the log
    print("\nTesting clear_log:")
    move_log.clear_log()
    move_log.display_log()

if __name__ == "__main__":
    test_move_log()
