import subprocess
from rich import print
from rich.console import Console

console = Console()

print("[bold magenta]pipLinux v1.0[/bold magenta]")
while True:
    packageName = console.input("[bold cyan]Enter python library/package name: [/bold cyan]")
    codeDown = 1
    try:
        print(f"[bold yellow]Downloading library/package {packageName} has started[/bold yellow]")
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
            print(f"[bold red]Error downloading: {result.stderr}[/bold red]")
    except Exception as e:
        print(f"Error downloading: {e}")
    finally:
        if codeDown == 0:
            print(f"[bold green]library/package {packageName} installed successfully[/bold green]")
        else:
            print(f"[bold red]library/package {packageName} not installed[/bold red]")
        while True:
            again = console.input("[bold cyan]Do you want to download another library/package? (y/n): [/bold cyan]").strip().lower()
            if again == 'y':
                break
            elif again == 'n':
                print("[bold magenta]Exiting pipLinux[/bold cyan]")
                exit()
            else:
                print("[bold red]Invalid input[/bold red]. [bold cyan]Please enter 'y' or 'n'.[/bold cyan]")