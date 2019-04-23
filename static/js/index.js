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

InitStatusButtons();
