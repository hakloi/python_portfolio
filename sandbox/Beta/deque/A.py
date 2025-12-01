from collections import deque

class Deque:
    def __init__(self):
        self.dq = deque()

    def execute(self, command):
        parts = command.strip().split()
        cmd = parts[0]

        if cmd == "push_front":
            self.dq.appendleft(parts[1])
            return "ok"
        elif cmd == "push_back":
            self.dq.append(parts[1])
            return "ok"
        elif cmd == "pop_front":
            return self.dq.popleft() if self.dq else "error"
        elif cmd == "pop_back":
            return self.dq.pop() if self.dq else "error"
        elif cmd == "front":
            return self.dq[0] if self.dq else "error"
        elif cmd == "back":
            return self.dq[-1] if self.dq else "error"
        elif cmd == "size":
            return str(len(self.dq))
        elif cmd == "clear":
            self.dq.clear()
            return "ok"
        elif cmd == "exit":
            return "bye"
        else:
            return "unknown command"

def main():
    d = Deque()
    while True:
        try:
            command = input().strip()
            result = d.execute(command)
            print(result, flush=True)
            if result == "bye":
                break
        except EOFError:
            break

if __name__ == "__main__":
    main()
