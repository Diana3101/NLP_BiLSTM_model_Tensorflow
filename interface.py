from tkinter import Tk, Text, BOTH, W, N, E, S, Frame, Button, Label, INSERT


def read_data(file_path):
    tokens = []
    tags = []
    tweet_tokens = []
    tweet_tags = []
    for line in open(file_path, encoding='utf-8'):
        line = line.strip()
        if not line:
            if tweet_tokens:
                tokens.append(tweet_tokens)
                tags.append(tweet_tags)
            tweet_tokens = []
            tweet_tags = []
        else:
            token, tag = line.split()
            tweet_tokens.append(token)
            tweet_tags.append(tag)

    return tokens, tags


f = open('text.txt', 'w')
tokens, tags = read_data('data_for_interface.txt')
str1 = ""
for i in range(len(tokens)):
    str1 = ' '.join(tokens[i])
    f.write(str1)
f = open('text.txt', 'r')


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("NER from Twitter")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Category")
        lbl.grid(sticky=W, pady=4, padx=5)

        text = Text(self)
        text.grid(row=1, column=0, columnspan=2, rowspan=4,
                  padx=5, sticky=N + E + W + S)

        text2 = Text(self)
        text2.grid(row=1, column=2, columnspan=2, rowspan=4,
                   padx=5, sticky=W + N + E + S)

        abtn = Button(self, text="Open file")
        abtn.grid(row=1, column=4)

        def change():
            text2.insert(INSERT, f.read())

        abtn.config(command=change)

        cbtn = Button(self, text="Do NER")
        cbtn.grid(row=2, column=4, pady=4)

        def change_s():
            text.insert(INSERT, "           - sportsteam\n")
            text.insert(INSERT, "\n           - faculty\n")
            text.insert(INSERT, "\n           - company\n")
            text.insert(INSERT, "\n           - geo-loc\n")
            text.tag_add("here", "1.0", "1.10")
            text.tag_add("heres", "3.0", "3.10")
            text.tag_add("heress", "5.0", "5.10")
            text.tag_add("heresss", "7.0", "7.10")
            text.tag_config("here", background="green")
            text.tag_config("heres", background="red")
            text.tag_config("heress", background="blue")
            text.tag_config("heresss", background="pink")
            text2.tag_add("here", "1.123", "1.136")
            text2.tag_add("here", "1.182", "1.188")
            text2.tag_config("here", background="green")
            text2.tag_add("heres", "1.587", "1.604")
            text2.tag_add("heres", "1.665", "1.685")
            text2.tag_config("heres", background="red")
            text2.tag_add("heress", "1.759", "1.767")
            text2.tag_config("heress", background="blue")
            text2.tag_add("heresss", "1.808", "1.818")
            text2.tag_add("heresss", "1.821", "1.823")
            text2.tag_config("heresss", background="pink")

        cbtn.config(command=change_s)


def main():
    root = Tk()
    root.geometry("900x500+500+500")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
