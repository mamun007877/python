import random as r
word_list=["ardvark","baboon","camel"]
chosen_word=r.choice(word_list)
display=[]
print(chosen_word)



for i in chosen_word:
    display.append("_")
count=3
while count>0:
    
    if "_"  in display:
        guess=input("guess a letter in lowercase: ").lower()
        if guess in chosen_word:
            for j in range(len(chosen_word)):
                if guess==chosen_word[j]:
                    display[j]=guess        
        else:
            count-=1
        if count==0:
            print("lost")
            break
    else:
                print("won")
                print(display)
                break

    

    