K = int(input())

hour = K // 60 + 21
minute = K % 60

print(f"{hour:02}:{minute:02}")
