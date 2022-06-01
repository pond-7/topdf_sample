import pdfkit


def main():
    pdfkit.from_file("src/html.html", output_path="html_test.pdf")

if __name__ == "__main__":
    main()