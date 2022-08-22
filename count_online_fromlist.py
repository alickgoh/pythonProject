def online_count(self):
    count = 0
    for a, b in statuses.items():
        if b == "online":
            count += 1
    return count


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))
