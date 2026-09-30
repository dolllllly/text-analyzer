from analyzer import generate_report

def main():
    text=input("enter text: ")
    report=generate_report(text)
    print(report)

if __name__=="__main__":
    main()