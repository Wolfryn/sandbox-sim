import os
import time

def main():
    # Create a folder and file to simulate behavior
    target = os.path.join(os.getcwd(), "sandbox_test_dir")
    os.makedirs(target, exist_ok=True)
    fname = os.path.join(target, "hello.txt")
    with open(fname, "w") as f:
        f.write("Hello from benign test.\n")
    time.sleep(0.05)

if __name__ == "__main__":
    main()
