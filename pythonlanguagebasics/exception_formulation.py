



def elucidating_try_catch():

    try:

        10/0

    except ZeroDivisionError:
        print("Division by zero error")

    else:
        pass

    finally:
        print("All cases handled")


elucidating_try_catch()