def is_clean(status):
  return status[room_a] and status[room_b]


def simulate(state, choice, status, cost, do_clean=True):
    if is_clean(status):
        print("All rooms are clean")
        return cost

    if choice != 1 and choice != -1:
        print("Invalid choice")
        return cost

    # Vacuum in room A
    if state[0][0]:
        if choice == -1:
            if do_clean and not state[0][1]:
                state[0][1] = True
                status[room_a] = True
                print("Cleaned room A")
                cost += 1  # Cost of cleaning
            else:
                print("No cleaning in room A")
        elif choice == 1:
          state[0][0] = False
          state[1][0] = True
          print("Moved vacuum from A to B")
        else:
            print("Cannot move from A to B")

    # Vacuum in room B
    elif state[1][0]:
        if choice == 1:
            if do_clean and not state[1][1]:
                state[1][1] = True
                status[room_b] = True
                print("Cleaned room B")
                cost += 1  # Cost of cleaning
            else:
                print("No cleaning in room B")
        elif choice == -1:
            state[1][0] = False
            state[0][0] = True
            print("Moved vacuum from B to A")
        else:
            print("Cannot move from B to A")
    else:
        print("Vacuum is not in any room!")

    return cost


if __name__ == "__main__":
    room_a = 'A'
    room_b = 'B'
    state = [[True, False], [False, False]]
    status = {room_a:False, room_b:False}
    total_cost = 0  # Initialize total cost

    while True:
      if is_clean(status):
        print("All rooms are clean. Exiting.")
        print(f"Total cost: {total_cost}") # Display total cost
        break

      choice = int(input("Enter -1 to act in Room A, 1 to act in Room B: "))
      action = input("Enter 'c' to clean, 'm' to move without cleaning: ").lower()

      if action == 'c':
          total_cost = simulate(state, choice, status, total_cost)
      elif action == 'm':
          total_cost = simulate(state, choice, status, total_cost, False)
      else:
          print("Invalid action choice")
