from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# results = tavily_search("Tell me about Hotel Raindew in Ranchi, India")
# print(results);

# results = search_flights("Plan a 7 days Japan trip from India");
# print(results);

user_input = input("Enter  travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user",
)

print("\nFinal Response:\n")
print(response["answer"])