#File
    there are two types file

        1.text file
            ->data of sequence of character
            ->such as .text,.py,.dat etc
        
        2.binary file
            ->data of sequence of bytes
            ->such as audio ,video, image etc

#step of file handling
    
        1.open file
            ->to open file we use open() function and store in a var
            ->var=open("file_name","mode"); here all parameter are string
            ->mode :text file=r,w,a,r+,w+,a+,x. binary file=rb,wb,ab,r+b,w+b,a+b,xb. use of them are same

                "r" refers read only.if there is no file it gives error like File not found error

                "w" refers write only. if no file then it creates file. if there is file then it will erase prev data and start fresh writing

                "a" refers append.no read.writing from prev data. if no file it creates

                "r+" refers reading and writing. if we 1st read ,it starts from 1st letter.after reading fully it starts writing from the last letter. if we 1st write ,it starts from 1st letter it will replcae them and then reading the full file. better to read 1st. if there is no file it gives file not found error.it use for modify data

                "w+" reading and writing. if no file it will creats. it erase prev data.1st write then read.it not use for modify data

                "a+" reading and writing.if no file it will creats. it is not erase prev data.1st write then read.it not use for modify data

                "x" exclusive write mode.always create new file.it is used for fresh writing.it will give error if same file already exist

            ->such as inf=open("input.txt","r"), inf1=open("video.mp4","rb")
            
        2.processing task of file like read or write

            inf=open("filename","r")
            inf1=open("filename","w")

            #property of open()

                inf.name->it gives file name

                inf.mode->it gives file mode

                inf.closed->it gives file closed or not

                inf.readable->it gives file readable or not

                inf.writable->it gives file writable or not

            #writing a file
                ->function for writing
                    1.write(single string)

                    2.writelines(list of lines)
                ->such as
                    text=input()

                    inf1.write(text) [ekhane ja likhbo ta file a dekha jabe terminal a na]

                    inf1.close()
            #reading a file
                ->function for reading
                    1.read() [all data read]

                    2.read(n) [1st n characters read]

                    3.readline() [read one line]

                    4.readlines() [all lines]
                ->such as
                    s=inf1.read()
                    s1=s=inf1.read(5)
                    s3=inf.readline()



        3.close file
            -> to close file we use close() function with refer of var
            ->var.close()
            ->such as inf.close()