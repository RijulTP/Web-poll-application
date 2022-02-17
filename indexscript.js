
getlistreq=$.getJSON("http://127.0.0.1:8000/polls/GET/",function(data){
    //len=getlist.length
    for (let i = 0; i < data.length; i++){
        currentques=data[i]
        quesno=i+1
        ques=currentques["Question"]
        
        votes=0
        votecontainer=Object.values(currentques["OptionVote"])
        for (let j = 0; j < votecontainer.length; j++) {
            votes +=votecontainer[j];
        }
        tags=currentques["Tags"]

        assignedhref="Detail.html?value="+currentques["QID"]

        markup = "<tr class='Content'><td class='No'>"+quesno.toString()+"</td><td class='Question'>"+"<a href="+assignedhref+">"+ques+"</a>"+"</td><td class='Votes'>"+votes+"</td><td class='Tags'>"+tags+"</td></tr>"
        tableBody = $("table")
        tableBody.append(markup)};
});

gettagsreq=$.getJSON("http://127.0.0.1:8000/polls/GET/tags/",function(data){
    markup='<form id="tagform">'
    for(let i=0; i<data.length; i++){
        currenttopic="topic"+i
        currentinput='<input type="checkbox" id='+ currenttopic+ ' value='+data[i]+'>'
        currentindex='<label for="topic'+i+'"'+'>'+data[i]+'</label><br>'
        markup+=currentinput
        markup+=currentindex
    }
    markup+='<br>'
    markup+='<input type="button" value="Filter by tags" id=submitbutton onclick="FilterData()";>'
    markup+='</form>'

    tagbody=$('div.ex3')
    tagbody.append(markup)
    tagsubmit=document.getElementById('submitbutton')
    console.log(tagsubmit)
    tagform=document.getElementById('tagform')
    console.log(tagform.firstchild)
    op1=tagform[0]

    console.log(tagform[1])

});



function FilterData(){
    console.log("Button Clicked")
    tagform=document.getElementById('tagform')
    var checklist=[]
    for(let i=0; i<tagform.length-1; i++){
        if (tagform[i].checked){
            checklist.push(tagform[i].value)
        }
    }
    console.log(document.getElementsByTagName("tr").length);
    $('table').detach();
    markup = "<table></table>";
    tablecontainer=$('div.ex1');
    tablecontainer.append(markup);
    tableBody = $("table")
    headermarkup='<tr class="Heading"><th>Number</th><th>Poll Question</th><th>Total Votes</th><th>Tags</th></tr>'
    tableBody.append(headermarkup)
    console.log(checklist)
    if (checklist.length==0){
        getlistreq=$.getJSON("http://127.0.0.1:8000/polls/GET/",function(data){
    //len=getlist.length
        for (let i = 0; i < data.length; i++){
            currentques=data[i]
            quesno=i+1
            ques=currentques["Question"]
            votes=0
            votecontainer=Object.values(currentques["OptionVote"])
            for (let j = 0; j < votecontainer.length; j++) {
                votes +=votecontainer[j];
            }
            tags=currentques["Tags"]

            assignedhref="Detail.html?value="+currentques["QID"]

            markup = "<tr class='Content'><td class='No'>"+quesno.toString()+"</td><td class='Question'>"+"<a href="+assignedhref+">"+ques+"</a>"+"</td><td class='Votes'>"+votes+"</td><td class='Tags'>"+tags+"</td></tr>"
            tableBody = $("table")
            tableBody.append(markup)};
    });
    }else{
    getfilterreq=$.getJSON("http://127.0.0.1:8000/polls/GET/?tags="+checklist,function(data){
        for (let i = 0; i < data.length; i++){
            currentques=data[i]
            quesno=i+1
            ques=currentques["Question"]
            votes=0
            votecontainer=Object.values(currentques["OptionVote"])
            for (let j = 0; j < votecontainer.length; j++) {
                votes +=votecontainer[j];
            };
            tags=currentques["Tags"]
            assignedhref="Detail.html?value="+currentques["QID"]
    
            markup = "<tr class='Content'><td class='No'>"+quesno.toString()+"</td><td class='Question'>"+"<a href="+assignedhref+">"+ques+"</a>"+"</td><td class='Votes'>"+votes+"</td><td class='Tags'>"+tags+"</td></tr>"
            tableBody = $("table")
            tableBody.append(markup);
        }
    });
}

    //tableBody = $("table");
    //tableBody.append(markup);


    //console.log(checklist);
};

