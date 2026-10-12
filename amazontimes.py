import math 
 
# Given response times (in milliseconds) 
response_times = [245, 312, 189, 276, 298, 234, 389, 267, 301, 223] 
 
# Calculate Mean (Average) 
mean = sum(response_times) / len(response_times) 
 
# Calculate Standard Deviation 
variance = sum((x - mean) ** 2 for x in response_times) / len(response_times) 
std_deviation = math.sqrt(variance) 
 
# Display Results 
print("Response Times (ms):", response_times) 
print("Average Response Time (Mean):", round(mean, 2), "ms") 
print("Standard Deviation:", round(std_deviation, 2), "ms") 