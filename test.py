def findMaxHealthSum(health_list, server_types, max_types):
    # Dictionary to group health values by server type
    server_health_map = {}
    
    for health, server in zip(health_list, server_types):
        if server not in server_health_map:
            server_health_map[server] = []
        server_health_map[server].append(health)
    
    # Calculate total health for each server type
    total_health_per_type = []
    for server in server_health_map:
        total_health_per_type.append(sum(server_health_map[server]))
    
    # Sort total health in descending order
    total_health_per_type.sort(reverse=True)
    
    # Pick the top max_types and calculate their total health
    max_health_sum = sum(total_health_per_type[:max_types])
    
    return max_health_sum


# Example usage
if __name__ == "__main__":
    health_list = [1, 2, 3, 10, 10]
    server_types = [3, 3, 1, 2, 5]
    max_types = 2
    print(findMaxHealthSum(health_list, server_types, max_types))  # Output: 20
