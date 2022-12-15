class FileSaver:

    def save(self, data: list = [], filename: str = "") -> None:
        """Saves arbitrary data to an arbitrary file.
        
        Keyword arguments:
        - data: list of strings save
        - filename: name of file to save to
        """
        fh = open(filename, "w")
        for item in data:
            fh.write(f"{item}")
        

def main():
    data = ["a\n", "b\n", "c\n", "1\n", "2\n", "3\n"]
    saver = FileSaver()
    saver.save(data, "first.dat")
    saver.save(data, "second.dat")

if __name__ == "__main__":
    main()