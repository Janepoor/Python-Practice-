
def main():
    outputString = ""
    inputString = "(S (NP (NNP James)) (VP (VBZ is) (NP (NP (DT a) (NN boy)) (VP (VBG eating) (NP (NNS sausages))))))"
    inputString = inputString.strip().split(' ')
    print (inputString)
    for word in inputString:
        if word.endswith(')'):
            outputString = outputString + str(word.strip(')')) + " "

    print(outputString)

main()