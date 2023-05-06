#Functions with Outputs
def format_name(first, last):
    #docstring : 선언 바로 아래, 함수 첫 줄에 """ 사이에 작성. 되도록 한 줄로
    #함수 문서화, 여러줄 주석 등에 사용
    """Take a first and last name and format it
  to return the title case version of the name."""

    #Return as an early exit
    if first == "" or last == "":
        return "You didn't provide valid inputs."
    f_name = first.title()
    l_name = last.title()
    return f"Result: {f_name} {l_name}"
    #(위와 같음) return f_name+" "+l_name


print(format_name("shin", "nAri"))

#Already used functions with outputs
length = len("hi")