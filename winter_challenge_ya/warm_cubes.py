import sys


def main():
    
    r, b = map(int, input().split())
    
    for inner_h in range(1, int(b ** 0.5) + 1):
        if b % inner_h == 0:
            inner_w = b // inner_h
            
            h = inner_h + 2
            w = inner_w + 2
            
            if r == (h * 2 + w * 2 - 4):
                print(w, h)
                break
            


if __name__ == '__main__':
    main()
