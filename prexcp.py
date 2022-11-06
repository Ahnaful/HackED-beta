def print_exc(e):
    #    [start red][\n][**] {[error type]}     {[error]} [end red]
    print(f"\033[91m\n** {repr(e).split('(')[0]}: {e}   \033[00m \n")
