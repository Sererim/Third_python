def clean() -> None:
    n_s: str = ""
    i: int = 0
    
    f = open("wiki_raw.txt", "r")
    s = f.read()
    n_f = open("wiki.txt", "w")
    
    
    while i < len(s):
        if s[i] == "[":
            while s[i - 1] != "]":
                i += 1
        else:
            n_s += s[i]
            i += 1
    
    n_f.write(n_s)
    n_f.close()
    f.close()
    
    
if __name__ == "__main__":
    clean()
