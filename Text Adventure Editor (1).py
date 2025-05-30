import json

def main():
    game = getDefaultGame()
    while True:
        choice = getMenuChoice()
        if choice == "0":
            print("Goodbye!")
        elif choice == '1':
            playGame(game)
        elif choice == '2':
            game = loadGame()
        elif choice == '3':
            saveGame(game)
        elif choice == '4':
            game = editNode(game)
        elif choice == '5':
            game = getDefaultGame()
            print("Default game loaded.")
        else:
            print("Invalid choice. Please select a valid option.")

        
def getMenuChoice():
    print("\nMenu:")
    print("0) Exit")
    print("1) Play current game")
    print("2) Load a game file")
    print("3) Save the current game")
    print("4) Edit or add a node")
    print("5) Load default game")
    return input("What will you do? ").strip()

def playGame(game):
    current_node = "start"
    while current_node != "quit":
        current_node = playNode(game, current_node)
        
def playNode(game, node_name):
    node = game.get(node_name)
    for option_key, (desc, _) in node["choices"].items():
        print(f"{option_key}. {desc}")
    
    while True:
        choice = input("Choose an option: ").strip()
        if choice in node["choices"]:
            return node["choices"][choice][1]
        else:
            print("Invalid choice. Try again.")

def getDefaultGame():
    return {
        "start": {
            "text": "Do you want to win or lose?",
            "choices": {
                "1": ("I want to win", "win"),
                "2": ("I'd rather lose", "lose"),
            }
        },
        "win": {
            "text": "You win!",
            "choices": {
                "1": ("Start over", "start"),
                "2": ("Quit", "quit"),
            }
        },
        "lose": {
            "text": "You lose!",
            "choices": {
                "1": ("Start over", "start"),
                "2": ("Quit", "quit"),
            }
        }
    }

def editNode(game):
    print("\nCurrent game nodes:")
    print(json.dumps(game, indent=2))
    
    node_name = input("\nEnter node name to edit or create: ").strip()
    
    if node_name in game:
        node = game[node_name]
        print(f"Editing existing node '{node_name}'.")
    else:
        node = {"text": "", "choices": {}}
        print(f"Creating new node '{node_name}'.")
    
    node["text"] = editField("Node text", node.get("text", ""))
    
    for i in range(2):
        desc = input(f"Enter description for choice {i}: ").strip()
        dest = input(f"Enter destination node for choice {i}: ").strip()
        node["choices"][str(i)] = (desc, dest)
    
    game[node_name] = node
    print(f"Node '{node_name}' updated.")
    return game

def editField(field_name, current_value):
    print(f"{field_name} (current): {current_value}")
    new_val = input(f"Enter new {field_name} (or Enter to keep current): ")
    return new_val

def saveGame(game):
    filename = 'game.dat'
    with open(filename, 'w') as f:
        json.dump(game, f, indent=2)
    print(f"Game saved to {filename}. Current game data:")
    print(json.dumps(game, indent=2))


def loadGame():
    filename = 'game.dat'
    with open(filename, 'r') as f:
        game = json.load(f)
    print(f"Game loaded from {filename}.")
    return game

main()