PromptMsg  = "1: Create user and update PIN\n2: Read Bitcoin balance \n3: Read Bitcoin Address\n4: Read EOS balance\n"
PromptMsg += "5: Read EOS address\n6: Transfer Bitcoin from bot to new user\n7: Transfer Bitcoin from new user to Master\n"
PromptMsg += "8: Withdraw bot's Bitcoin\n"
PromptMsg += "9: Exit \nMake your choose:"
while ( 1 > 0 ):
    x = input(PromptMsg)
    if (x == '9' ):
        exit()
    print(x)
