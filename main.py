import easyocr
import g4f

ask = 0
def text_recognition(file_path):
    reader = easyocr.Reader(['uk'])
    result = reader.readtext(file_path, detail=0)
    
    return result

def main():
    # file_path = input("Enter a file path: ")
    file_path = '11.png'
    return text_recognition(file_path=file_path)
    
# if __name__ == "__main__":
#     main()



def ask_gpt(prompt):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        # model= "gpt-3.5-turbo",
        messages=[{"role": "user", "content":"Дай відповідь на питання, українською мовою " + str(prompt)}]
    )
    return response


# print(ask_gpt(main()))

for i in range(3):
    f = open( 'ansver'+str(i)+'.txt', 'w' )
    f.write(ask_gpt(main()))
    f.close()