#
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

# metacount = 0


class MyHTMLParser(HTMLParser):
    # function to handle an opening tag in the doc
    # this will be called when the closing ">" of the tag is reached
    def handle_comment(self, data):
        # global metacount
        # if tag == "meta":
        #     metacount += 1

        print("Encountered comment:", data)
        pos = self.getpos()  # returns a tuple indication line and character
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    # instantiate the parser and feed it some HTML

    parser = MyHTMLParser()

    # open the sample HTML file and read it
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)

    # print("%d meta tags encountered" % metacount)


if __name__ == "__main__":
    main()
