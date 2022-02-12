var url_string = window.location.href;

var url = new URL(url_string);
var qsno = url.searchParams.get("value");

getlistreq=$.getJSON("http://127.0.0.1:8000/polls/GET/",function(data){
    questiondict=data[qsno]
    document.getElementById("QuestionTitle").innerHTML = questiondict["Question"]
    console.log(questiondict)
    Choices=questiondict['OptionVote']
    var markup='<form id="Choiceform">'
    console.log("Choices are",Choices[Object.keys(Choices)[0]])

    for(let i=0; i<Object.keys(Choices).length; i++){
        currenttopic="topic"+i
        choice=Object.keys(Choices)[i]
        currentinput='<input type="radio" id='+ currenttopic+ ' value='+choice+'>'
        currentindex='<label for="topic'+i+'"'+'>'+Object.keys(Choices)[i];+'</label><br>'
        markup+=currentinput
        markup+=currentindex
        markup+='<br>'
    }
    markup+='<br>'
    markup+='<input type="button" value="Vote" id=submitbutton onclick="VoteFunction()";>'
    markup+="</form>"
    choicebody=$('div.ex3')
    choicebody.append(markup)
    document.getElementById("submitbutton").click(function(e){
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        return false;
    })
});

function VoteFunction(){
    Choiceform=document.getElementById('Choiceform')
    postlink="http://127.0.0.1:8000/polls/"+(qsno+1)
    getlistreq=$.getJSON("http://127.0.0.1:8000/polls/GET/",function(data){
        questiondict=data[qsno]
        document.getElementById("QuestionTitle").innerHTML = questiondict["Question"]
        Choices=questiondict['OptionVote'];
        for(let i=0; i<Choiceform.length-1; i++){
            if (Choiceform[i].checked){
                Choiceincrement=Object.keys(Choices)[i]
                break
            };
        };
        console.log("Choiceincrement is",Choiceincrement)
        payload={'incrementOption':Choiceincrement}
        $.post(postlink, payload)
        //window.location.href="index.html"
    }) 
}
