function show18plus () {
	/* Вызывает предупреждение 18+ о переходе на страницу со стримом */
	var result = confirm("На стриме может присутствовать контент 18+. Вы действительно хотите перейти к просмотру?");
	if (result) {
		window.open("./live.html");
	}
}