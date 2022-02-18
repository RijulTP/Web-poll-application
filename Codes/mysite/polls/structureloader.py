def optioncounter(text):
    c = 0
    for i in text:
        if i == "|":
            c += 1
    return c + 1  # 3 | symbols means 4 options


def collectoptions(text):
    optionAmount = optioncounter(text)
    # print("Option amount is",optionAmount)
    firstDividerLoc = text.find("|")
    firstOption = text[:firstDividerLoc]  # first option gets made
    optionlist = []
    if optionAmount == 1:
        optionlist = [text.strip(" ")]
        return optionlist
    elif optionAmount < 3:
        lastOption = text[firstDividerLoc + 1:]
        optionlist = [firstOption.strip(" "), lastOption.strip(" ")]
        return optionlist
    else:
        # lastDividerLoc = text.find("|", firstDividerLoc + 1)
        currentposition = firstDividerLoc + 1
        nextposition = text.find("|", firstDividerLoc + 1)
        optionlist.append(firstOption.strip(" "))
        c = optionAmount
        while c >= 2:
            if c == 2:
                option = text[currentposition:]
                optionlist.append(option.strip(" "))
            else:
                option = text[currentposition:nextposition]
                optionlist.append(option.strip(" "))
                currentposition = nextposition + 1
                nextposition = text.find("|", currentposition + 1)
            c -= 1

        return optionlist


def dictionarymaker(olist, vlist):
    noElements = len(olist)
    currentdict = {}
    for i in range(0, noElements):
        currentdict[olist[i]] = vlist[i]
    return currentdict


def loadquestion(txt):
    # print(txt)
    questionMarker = txt.find(":")
    question = txt[:questionMarker]
    noofOptions = optioncounter(txt)
    optionMarker1 = txt.find(":", questionMarker + 1)
    optionMarker2 = txt.find(":", optionMarker1 + 1)
    # print(questionMarker, optionMarker1, optionMarker2)
    optionBunch = txt[optionMarker1 + 1:optionMarker2 - 1]
    optionList = collectoptions(optionBunch)  # returns the list of options in a list

    voteMarker1 = txt.find(":", optionMarker2 + 1)
    voteMarker2 = txt.find(":", voteMarker1 + 1)
    voteBunch = txt[voteMarker1 + 1:voteMarker2 - 1]
    voteList = collectoptions(voteBunch)
    # print("Vote Bunch is", voteBunch)
    # print("vote list is", voteList)

    optionDictionary = dictionarymaker(optionList, voteList)

    # print("Option Dictionary is", optionDictionary)
    tagMarker1 = txt.find(":", voteMarker2 + 1)
    tagMarker2 = txt.find(":", tagMarker1 + 1)
    tagBunch = txt[tagMarker1 + 1:tagMarker2]
    finaltag = collectoptions(tagBunch)
    finalquestion = txt[:(txt.find(":"))]
    finaldict = {"Question": finalquestion.strip(" ")}
    finalList = [finaldict]
    finaldict["OptionVote"] = optionDictionary
    finaldict["Tags"] = finaltag
    # print(FinalList)
    # print(optionList)
    return finaldict


def load_fps(filepath):
    f = open(filepath)
    finalList = []
    totalquestions = f.readlines()[1:]
    # print("Length of ques is",len(f.readlines()))
    for i in totalquestions:
        currentques = i
        dict = loadquestion(currentques)
        finalList.append(dict)
    return finalList


# print("Final List is",finalList)
def filter_by_tags(polls_data, list_of_tags):
    FilteredList = []
    for i in polls_data:
        #print(i)
        for j in i["Tags"]:
            #print("j", j)
            for k in list_of_tags:
                #print("k", k)
                if j.lower() == k.lower():
                    for x in FilteredList:
                        if x==i:
                            break
                    FilteredList.append(i)
                    break
    print("Filtered List is ", FilteredList)
def listToString(l):
    finalstring=""
    for i in l:
        if finalstring=="":
            finalstring = finalstring+ i
        else:
            finalstring = finalstring + "," + i


    return  finalstring
def viewpoll(polls_data, pollno):
    datatobeviewed=polls_data[pollno-1]
    print(datatobeviewed["Question"])
    for i in datatobeviewed["OptionVote"]:
        print("*", i, datatobeviewed["OptionVote"].get(i))
    print()
    print("Tags:",listToString(datatobeviewed["Tags"]))
    print()


tobefiltered = load_fps("C:\\Files and Apps\\Pycharm\\Files\\polldata.fps")
#filter_by_tags(tobefiltered, ["programming"])
#viewpoll(tobefiltered,6)


def update_poll(polls_data, pollNumber, optionName):
    datatobeviewed = polls_data[pollNumber]
    votearea = datatobeviewed["OptionVote"]
    for i in votearea:
        if i.lower() == optionName.lower():
            votearea[i]=int(votearea.get(i))+1
def filestrconverter(structure):
    convertedstr=""
    convertedstr+="Questions :: Options :: Votes :: Tags\n"
    for i in structure:
        currentvotetructure=""
        votestring=""
        amtstring=""
        tagstring=""
        if len(i["OptionVote"])==2:
            first_value = list(i["OptionVote"].items())[0]
            last_value= list(i["OptionVote"].items())[1]
            votestring=votestring+first_value[0]+" | "+last_value[0]
            amtstring=amtstring+str(first_value[1])+" | "+str(last_value[1])
        else:
            for j in i["OptionVote"].items():
                #print("main j",j)
                votestring += j[0] + " | "
                #print("j is",j[1])
                amtstring += str(j[1]) + " | "
            votestring=votestring[:len(votestring)-2]
            amtstring=amtstring[:len(amtstring)-2]

        if len(i["Tags"])==1:
            tagstring=i["Tags"][0]
        else:
            for x in i["Tags"]:
                tagstring+=x+" | "
            tagstring = tagstring[:len(tagstring) - 2]

        currentvotetructure=i["Question"]+" :: "+votestring+" :: "+amtstring+" :: "+tagstring+"\n"
        convertedstr+=currentvotetructure

    #print(convertedstr)
    return convertedstr


def save_poll(polls_data,filepath):
    convertedfile=filestrconverter(polls_data)
    f=open(filepath,"w")
    f.write(convertedfile)
    print("===================")
    print("Successfully Saved!")
    print("===================")
'''while True:
    print("1.Convert to structure")
    print("2.Filter by tags")
    print("3.View Polls")
    print("4.Update Polls")
    print("5.Save Polls")
    print("6.Quit")
    choice = int(input("Choose your Option"))

    if choice == 1:
        print(load_fps("C:\\Files and Apps\\Pycharm\\Files\\polldata.fps"))
    elif choice == 2:
        taglist = []
        while True:
            tag = input("Enter tags.. press n when done")
            if tag.lower()=="n":
                filter_by_tags(tobefiltered, taglist)
                break
            else:
                taglist.append(tag)
    elif choice == 3:
        pollchoice=int(input("Enter Poll Number"))
        if pollchoice>6 or pollchoice<1:
            print("Invalid Choice")
            break
        else:
            viewpoll(tobefiltered, pollchoice)
    elif choice == 4:
        pollchoice = int(input("Enter Poll Number"))
        if pollchoice > 6 or pollchoice < 1:
            print("Invalid Choice")
            break
        else:
            voteoption=input("Enter Option Name")
            update_poll(tobefiltered, pollchoice-1, voteoption)
    elif choice==5:
        save_poll(tobefiltered,"C:\\Files and Apps\\Pycharm\\Files\\polldata.fps")
    elif choice == 6:
        break
    else:
        print("Invalid Choice")'''








