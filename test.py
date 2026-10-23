from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# results = tavily_search("Tell me about Hotel Raindew in Ranchi, India")
# print(results);

results = search_flights("Plan a 7 days Japan trip from India");
print(results);