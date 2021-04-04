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
      challenges: ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
      completedLessons: [],
      firstCo: "false"
    }
    member.updateMetaData(memberProgress)
  })
}

function getCurrentChallenge() {
  MemberStack.onReady.then(async function(member) {
    var metadata = await member.getMetaData();
    for (let i = 0; i < metadata["challenges"].length; i++) {
      if (metadata["challenges"][i] == "1") {
        var tmp = i + 1
        editCurrentChallenge("Défi " + tmp)
      }
    }
  })
}

function editCurrentChallenge(challenge) {
  var divs = document.getElementsByClassName("display_none")

  Array.from(divs).forEach((div) => {
    if (div.innerHTML.includes(challenge))
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

  document.getElementById("nomcours-2").value = document.getElementsByClassName("titre-ressource")[0].innerHTML
  document.getElementById("evalcours-2").value = document.getElementsByClassName("titre-ressource")[0].innerHTML
}

setupIfFirstConnection()
getCurrentChallenge()
