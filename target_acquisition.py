print("--- TARGET ACQUISITION SYSTEM ---")

password = input("enter the password: ")

if password == "l023r123":
    print("access granted. welcome to mainframe")
    user_id = input("what is your alias: ")
    target_ip = input("what is the ip address: ")
    print(user_id, "is attacking", target_ip)
else:
    print("access denied. alerting user.")
