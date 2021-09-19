// Add class to element listed in Memberstack field "defis-termines"
function checkCompletedDefis() {
	MemberStack.onReady.then(function(member) {
	  if (member.loggedIn) {
	    var defis = member["defis-termines"].split(", ")
            for (var i = 0; i < defis.length; ++i) {
              document.getElementById("defi_"+ defis[i]).className += "rendu"            }
            }
	 }
  })
}
