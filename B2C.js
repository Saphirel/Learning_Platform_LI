<script>

function setupIfFirstConnection() {
  console.log("Checking first co...");

  MemberStack.onReady.then(async function(member) {
    var metadata = await member.getMetaData();
    if (res = (typeof metadata["firstCo"] == 'undefined'))
      setDefaultMetadataValues();
  })
}

function setDefaultMetadataValues() {
  console.log("First co, setting up default values...");
  MemberStack.onReady.then(function(member) {
    var memberProgress = {
      completedLessons: [],
      firstCo: "false"
    }
    member.updateMetaData(memberProgress)
  })
}

function getCurrentChallenge() {
  MemberStack.onReady.then(function(member) {
    var challenge_name = member["dfi-en-cours"]
    editCurrentChallenge(challenge_name)
  })
}

function editCurrentChallenge(challenge) {
  var divs = document.getElementsByClassName("display_none")

  Array.from(divs).forEach((div) => {
    if (div.innerHTML.includes(challenge + "<"))
      div.style.display = "block"
  });
}

function presetForm() {
  MemberStack.onReady.then(function(member) {   
	  if (member.loggedIn) {
		  document.getElementById("emailuser-2").value = member["email"]
		  document.getElementById("evaluseremail-2").value = member["email"]
	  }
  })

  document.getElementById("nomcours-2").value = document.getElementById("cours_id").innerHTML
  document.getElementById("evalcours-2").value = document.getElementById("cours_id").innerHTML
}

function checkIfLessonCompleted() {
	MemberStack.onReady.then(function(member) {   
	  if (member.loggedIn) {
	    var lessons = member["cours-finis"].split(", ")
	    var current_lesson = document.getElementById("cours_id").innerHTML
	    if (lessons.includes(current_lesson)) {
	      document.getElementById("cta_terminer").style.display = "none"
	      document.getElementById("cours_ok").style.display = "block"
	    }
	 }
  })
}

</script>

<script>

setupIfFirstConnection()
getCurrentChallenge()

checkIfLessonCompleted()

</script>
