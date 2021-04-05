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
      checkedTodoItems: [],
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

function checkCompletedLessons() {
	MemberStack.onReady.then(function(member) {   
	  if (member.loggedIn) {
	    var lessons = member["cours-finis"].split(", ")
        var displayed_lessons = document.getElementsByClassName("ressource-collection-item")

        for (var i = 0; i < displayed_lessons.length; ++i) {
            if (lessons.includes(displayed_lessons[i].getElementsByClassName("cours_id")[0].innerHTML)) {
              displayed_lessons[i].getElementsByClassName("pastille_cours_fini")[0].style.display = "block"
            }
        }
	 }
  })
}

function updateChallengesDisplay() {
	var tmp = []
	for (var i = 1; i < 6; ++i) {
	    tmp[i -1] = document.getElementById("bloc_" + i)
	}

var found_ongoing_challenge = false

MemberStack.onReady.then(function(member) {
    var challenge_name = member["dfi-en-cours"].split(" ").join("&nbsp;")
    for (var i = 0; i < tmp.length; ++i) {
        if (tmp[i].innerHTML.includes(challenge_name)) {
           found_ongoing_challenge = true
        } else {
            if (found_ongoing_challenge) {
                var challenges = tmp[i].getElementsByClassName("container-defi-et-detail")
                for (var j = 0; j < challenges.length; ++j) {
                    challenges[j].classList.add("unavailable")
                }
            }
        }
        
    }
  })
}

function hideFormButton() {
	var tmp = 0
var i = 0
var blocks = [2, 3, 3, 2, 2]
var displayed_challenge_id = parseInt(document.getElementById("defi_id").innerHTML)

while (blocks[i] + tmp < displayed_challenge_id) {
  tmp += blocks[i]
  i += 1
}
var displayed_challenge_block = i +1

tmp = 0
i = 0

MemberStack.onReady.then(function(member) {
    var tmp_array = member["dfi-en-cours"].split(" ")
    var current_challenge = parseInt(tmp_array[tmp_array.length -1])

    while (blocks[i] + tmp < current_challenge) {
      tmp += blocks[i]
      i += 1
    }
    var current_challenge_block = i +1

    if (displayed_challenge_block > current_challenge_block) {
        document.getElementById("submit_defi").style.display = "none"
        document.getElementById("submit_defi_responsive").style.display = "none"
    }
  })
	
}



</script>

<script>

setupIfFirstConnection()
getCurrentChallenge()

checkIfLessonCompleted()
checkCompletedLessons()

updateChallengesDisplay()
hideFormButton()

</script>
