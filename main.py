import subprocess

print("pipLinux v1.0")
while True:
    packageName = input("Enter python library/package name:")
    codeDown = 1
    try:
        print(f"Downloading library/package {packageName} has started")
        result = subprocess.run(
            ["sudo", "apt", "install", f"python3-{packageName}"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            codeDown = 0
        else:
            print(f"Error downloading: {result.stderr}")
    except Exception as e:
        print(f"Error downloading: {e}")
    finally:
        if codeDown == 0:
            print(f"library/package {packageName} installed successfully")
        else:
            print(f"library/package {packageName} not installed")
        while True:
            again = input("Do you want to download another library/package? (y/n): ").strip().lower()
            if again == 'y':
                break
            elif again == 'n':
                print("Exiting pipLinux")
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")