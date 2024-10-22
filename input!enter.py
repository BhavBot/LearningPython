import msvcrt
def get_key():
    while True:
        # Wait for a key press and decode it
        key = msvcrt.getch().decode("utf-8").upper()
        
        # Allow only valid keys (W, A, S, D, Q)
        if key in ['W', 'A', 'S', 'D', 'Q']:
            return key
def treasure_hunt_game():
    while True:
      #  print("\nCurrent Grid:")
       # print_grid(grid, player_pos)
        
        # Ask for a single key press
        print("Move (W: Up, S: Down, A: Left, D: Right, Q: Quit): ")
        move = get_key()
        print(f"\nYou pressed: {move}")  # Feedback for the pressed key
        
        if move == "Q":
            print("You quit the game.")
            break
treasure_hunt_game()
