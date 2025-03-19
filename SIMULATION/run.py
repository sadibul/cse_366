from agent import Agent
from enviourment import Environment

def main():
    # Create an environment with dimensions 10x10
    env = Environment(width=10, height=10)
    env.display()
    
    # Create agents within the environment
    agent_a = Agent(name="Agent A", environment=env)
    agent_b = Agent(name="Agent B", environment=env)
    
    agent_a.status()
    agent_b.status()
    
    # Simulate agent movement for Agent A
    movements_a = ["up", "up", "right", "down", "left", "left", "up", "right"]
    for move in movements_a:
        print(f"Moving {move} for Agent A...")
        agent_a.move(move)
    
    # Simulate agent movement for Agent B
    movements_b = ["down", "down", "left", "up", "right", "right", "down", "left"]
    for move in movements_b:
        print(f"Moving {move} for Agent B...")
        agent_b.move(move)
    
    agent_a.status()
    agent_b.status()

if __name__ == "__main__":
    main()

