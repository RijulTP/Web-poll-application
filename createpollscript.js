function AddOption(){
    markup='<input type="text" name="Option" style="width: 400px;border: 2px solid rgb(189, 189, 189);"><br><br>'
    optionform=$('form')
    console.log("adding option")
    Optionbody=document.getElementById('Options')
    $('#Options').append(markup)

}

function AddQuestion(){
    console.log("AddingQuestion")
    quesfield=document.getElementById('QuestionField')
    console.log("Question is",quesfield.value)
    currentquestion=quesfield.value
    choiceform=document.getElementById("Options")
    choiceobject={}
    for (let i = 0; i < choiceform.length; i++){
        currentchoice=choiceform[i].value
        currentdict={currentchoice:0}
        choiceobject[currentchoice] = 0
    }
    console.log("Choices are",choiceobject)
    tagform=document.getElementById("tagform")
    
    tags=tagform.value.split(',')
    console.log("Tags are",tags)
    data={
        "Question": currentquestion,
        "OptionVote":choiceobject,
        "Tags": tags
     }
     
    $.post("http://127.0.0.1:8000/polls/POST/",JSON.stringify(data))

    window.location.href="index.html"



}