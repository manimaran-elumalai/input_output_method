# states = ["Tamil Nadu", "Andhra", 'Kerala', "Karnataka"]
#
# with open('states.txt', 'w') as state_file:
#     for state in states:
#         print(state, file=state_file)


states = []

with open('states.txt', 'r') as state_file:
    for state in state_file:
        states.append(state.strip())
    print(states)

    for state in states:
        print(state)
