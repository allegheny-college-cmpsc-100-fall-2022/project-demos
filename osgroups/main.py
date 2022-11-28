import subprocess

def main():
    groupscmd = subprocess.getoutput("groups")
    groupslist = groups.split()
    if "Muufo" in groups:
        print(f"You're allowed.")
    else:
        print(f"You're not allowed.")

if __name__ == "__main__":
    main()