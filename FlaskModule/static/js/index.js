function Enable(button) {
	button.removeAttribute("disabled");
	button.classList.remove("btn-secondary");
}

function Off(button) {
	Enable(button);
	button.classList.remove("btn-success");
	button.classList.add("btn-danger");
}

function On(button) {
	Enable(button);
	button.classList.remove("btn-danger");
	button.classList.add("btn-success");
}

function InitStatusButtons() {
	var xmlHttpRequest = new XMLHttpRequest();
	xmlHttpRequest.onreadystatechange = function () {
		if (this.readyState === 4 && this.status === 200) {
			var jsonData = JSON.parse(xmlHttpRequest.responseText);
			for (var i = 0; i < jsonData.length; i++) {
				var jsonPinNumber = jsonData[i].pinNumber;
				var jsonState = jsonData[i].state;
				var currentButton = document.getElementById("btn" + jsonPinNumber);
				if (jsonState === 0) {
					Off(currentButton);
				}
				else if (jsonState === 1) {
					On(currentButton);
				}
				else if (jsonState === "You must setup() the GPIO channel first"){
					SetupPins();
					break;
				}
			}
		}
	};
	xmlHttpRequest.open("GET", "/states");
	xmlHttpRequest.send();
}

function SetupPins(){
	var xmlHttpRequest = new XMLHttpRequest();
	xmlHttpRequest.onreadystatechange = function () {
		if (this.readyState === 4 && this.status === 200) {
			var jsonData = JSON.parse(xmlHttpRequest.responseText);
			for (var i = 0; i < jsonData.length; i++) {
				var jsonPinNumber = jsonData[i].pinNumber;
				var jsonState = jsonData[i].state;
				var currentButton = document.getElementById("btn" + jsonPinNumber);
				if (jsonState === 0) {
					Off(currentButton);
				}
				else if (jsonState === 1) {
					On(currentButton);
				}
			}
		}
	};
	xmlHttpRequest.open("GET", "/setup?asType=output");
	xmlHttpRequest.send();
}

function TogglePin(pinNumber) {
	var xmlHttpRequest = new XMLHttpRequest();
	xmlHttpRequest.onreadystatechange = function () {
		if (this.readyState === 4 && this.status === 200) {
			var jsonData = JSON.parse(xmlHttpRequest.responseText);
			var currentButton = document.getElementById("btn" + jsonData.pinNumber);
			if (jsonData.state === 0) {
				Off(currentButton);
			}
			else if (jsonData.state === 1) {
				On(currentButton);
			}
		}
	};
	xmlHttpRequest.open("GET", "/toggle/" + pinNumber);
	xmlHttpRequest.send();
}

InitStatusButtons();
