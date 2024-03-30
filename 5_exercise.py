def f(text):
    if not text or len(text)>140 or not text.startswith("#"):
        return f"{text} there is mistake PLease try later"
    words=text.split()
    new_text=""
    for i in words:
        if i[words].islower():
            return "Error in words "
        else:
            new_text  = + i.capitalize() +""
            return new_text.strip()
text="# Hllo World Thanks Tor Pou"
result=f(text)
if result:
    print(result)
else:
    False
