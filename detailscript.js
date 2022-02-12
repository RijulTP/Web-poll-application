var url_string = window.location.href;

var url = new URL(url_string);
var qsno = url.searchParams.get("value");
var votepagelink="Votepage.html?value="+qsno
window.onload = function(){ 
    var onclickvalue="window.location.href="+"'"+votepagelink+"'"
    console.log(onclickvalue)
    
    document.getElementById("QuestionTitle").innerHTML = questiondict["Question"];
    function NewLink(){
        window.location.href="Votepage.html?value="+qsno
    }
    document.getElementById("Votebutton").onclick=NewLink
};

getlistreq=$.getJSON("http://127.0.0.1:8000/polls/GET/",function(data){
    questiondict=data[qsno]
    console.log(questiondict)
    
    tableBody = $("table")
    Choices=questiondict['OptionVote']
    tags=questiondict['Tags']
    console.log(Object.keys(Choices).length)
    for (i=0;i<Object.keys(Choices).length;i++){
        console.log('Choice added')
        quesno=i+1
        choice=Object.keys(Choices)[i]
        vote=Choices[choice]
        markup = "<tr class='Content'><td class='No'>"+quesno.toString()+"</td><td class='Question'>"+choice+"</td><td class='Votes'>"+vote+"</td></tr>"
        tableBody.append(markup);
    }
    document.getElementById("Tags").innerHTML = "Tags:"+tags;

    totalvotes=0
    votecontainer=Object.values(questiondict["OptionVote"])
    for (let j = 0; j < votecontainer.length; j++) {
            totalvotes +=votecontainer[j];
    }
    console.log("Total votes are",totalvotes)
    document.getElementById("TotalVotes").innerHTML = "Total Votes:"+totalvotes;

    var data = [];

    for (i=0;i<Object.keys(Choices).length;i++){
        choice=Object.keys(Choices)[i]
        vote=Choices[choice]
        newObj={}
        newObj.x = choice;
        newObj.value=vote;
        data.push(newObj)

    };

   
    var chart = anychart.pie();
  
    // add the data
    chart.data(data);
  
    // display the chart in the container
    chart.container('Container');
    chart.draw();

});