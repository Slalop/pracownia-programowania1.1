function validate() {
    var Old = document.getElementById("OldPrice").value;
    var New = document.getElementById("NewPrice").value;
    if (New >= Old+(0.3*Old)) {
		alert("cena jest za wysoka");
        return false;
    } else if (New <= (Old-0.7*Old)){
        alert("cena jest za niska");
        return false;
    } else {
		return true;
}
}