# condition: like this syntexes it's not expression

    syntex-1:
        if condition:
            do this
        else:
            do this

![](<flowchart.drawio.png>)

    syntex-2:
        if condition:
            do this
        elif condition:
            do this
        else:
            do this

# nested condition

    syntex:
        if condition:
            if condition:
                do this
            else:
                do this
        else:
            do this
    
# multiple if :(we use it for many condition is true)

    syntex:

        if condition:
            do this
        if condition:
             do this

# ternary operator : with this syntex it becomes expression

    value1 if condition else value2

    we can store it in a variable
    
    z=value1 if condition else value2

    example:

        v=5 if 5>3 else 3



