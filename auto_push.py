import time
import subprocess
import sys

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8', errors='ignore').strip()

def has_changes():
    status = run_cmd("git status --porcelain")
    return len(status) > 0

print("Auto-Push Watcher Started. Polling for changes...")

while True:
    try:
        if has_changes():
            print("Changes detected! Staging files...")
            run_cmd("git add .")
            print("Committing changes...")
            run_cmd('git commit -m "Auto update: saved changes"')
            print("Pushing to GitHub...")
            run_cmd("git push origin main")
            print("Pushed successfully!")
        time.sleep(5)
    except KeyboardInterrupt:
        print("Watcher stopped.")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
