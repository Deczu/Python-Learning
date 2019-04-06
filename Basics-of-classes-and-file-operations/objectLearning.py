


class TextSplitter:

    def __init__(self,text):
        self.text_data = text

    def count_words(self):
        txt = self.text_data;
        txt = txt.split();
        return int(len(txt));

    def specific_words(self):
        txt = self.text_data;
        dictionary = {}
        txt = txt.split();

        for i in txt:
            if i in dictionary:
                dictionary[i] +=1;
            else:
                dictionary[i] = 1;

        return dictionary

try:    
    with open("simple.txt") as fobj:
        txt = fobj.read();
except FileNotFoundError:
    text = "File not found or it does not exist in this directory"
    print(text)
else:
    new = TextSplitter(txt);
    num = new.count_words();
    specWords = new.specific_words();

    checksum=0;

    for value in specWords.values():
        checksum+=value;

    if checksum == num:
        print(new.text_data)
        print(num)
        print(specWords);
    else:
        print("Checksum invalid!")

    with open("result.txt","a") as f:
        f.write(str(num)+"\n")
        f.write(str(specWords)+"\n")
        f.write(40*"="+"\n")
        
finally:
    x = raw_input();
