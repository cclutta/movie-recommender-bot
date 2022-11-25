function update() {
		var userMessage = document.getElementById("user_message");
		var para = document.createElement("div");
		para.classList.add("chat-box-body-send");
		var p_message = document.createElement("p"); 		
		var node = document.createTextNode(userMessage.value);
		p_message.appendChild(node);
		para.appendChild(p_message);
		document.getElementById("chat-box-body").appendChild(para);
		return false;
	}
function get_response() {
	    var userMessage = document.getElementById("user_message");
	    console.log("The user message: " + userMessage.value);
	    update();
	    var xhttp = new XMLHttpRequest();
	    xhttp.onreadystatechange = function() {
              if (this.readyState == 4 && this.status == 200) {
                var rec_div = document.createElement("div");
		rec_div.classList.add("chat-box-body-receive");
		var p_message = document.createElement("p");
		var node = document.createTextNode(this.responseText);
		p_message.appendChild(node);
		rec_div.appendChild(p_message);
		document.getElementById("chat-box-body").appendChild(rec_div);
              }
           };
           var url = "http://127.0.0.1:5000/movie-bot-app/chat/"+userMessage.value;
           console.log("The url is: " + url);
           xhttp.open("GET", url);
           xhttp.send();
           userMessage.value= "";
           return false;
	}
