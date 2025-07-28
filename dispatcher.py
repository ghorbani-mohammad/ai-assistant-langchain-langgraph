from langgraph.graph import StateGraph, START
from typing import TypedDict

# Define the state schema
class State(TypedDict):
    name: str
    greeting: str

# Define two simple nodes
def greet(state: State) -> State:
    state["greeting"] = f"Hello, {state['name']}!"
    return state

def exclaim(state: State) -> State:
    state["greeting"] += " 👋"
    return state

# Create the state graph
g = StateGraph(State)
g.add_node("greet", greet)
g.add_node("exclaim", exclaim)
g.add_edge(START, "greet")
g.add_edge("greet", "exclaim")

# Compile the graph
app = g.compile()

# Run the graph
initial_state = {"name": "Mo"}
result = app.invoke(initial_state)
print(result["greeting"])  # Hello, Mo! 👋
