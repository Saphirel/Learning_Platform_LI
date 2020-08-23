<noscript>
<meta http-equiv="refresh" content="0; url=objectif2k30.kedge.edu/enable-js" />
</noscript>

<script>

function fancyTimeFormat(duration) {
    var hrs = ~~(duration / 3600);
    var mins = ~~((duration % 3600) / 60);
    var secs = ~~duration % 60;
   
    var ret = "";
    if (hrs > 0) {
      ret += "" + hrs + ":" + (mins < 10 ? "0" : "");
    }
   
    ret += "" + mins + ":" + (secs < 10 ? "0" : "");
    ret += "" + secs;
    return ret;
}

function timer(end, field_id) {
  var start = Date.now() /1000 | 0;
 
  setTimeout(() => {
    ttl = end - start;
   
    if (ttl > 0) {
      document.getElementById(field_id).innerHTML = fancyTimeFormat(ttl);
      timer(end, field_id);
    } else {
      console.log("Time's up");
      updateStepsStatus();
    }
  }, 1000);
}

///////// MEMBER STACK STUFF

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
        currentProjectStep: ["1", "0", "0", "0", "0"],
        currentProjectTimers: ["1598961600-1598977800", "1599030000-1599042600", "1599048000-1599064200", "1599134400-1599150600", "1599202800-1599215400"],
        firstCo: "false"
    }
    member.updateMetaData(memberProgress)
  })
}

function setTestingMetadataValues() {
  console.log("Setting up testing values...");
 
  var start = (Date.now() /1000 | 0) + 60;
  var timers = [];
  for (let i = 0; i < 5; ++i) {
  timers[i] = start + "-" + (start + 60);
    start += 60;
  }
 
  MemberStack.onReady.then(function(member) {
    var memberProgress = {
        currentProjectStep: ["1", "0", "0", "0", "0"],
        currentProjectTimers: timers,
        firstCo: "false"
    }
    member.updateMetaData(memberProgress)
  })
}

/////////// Update main menu

function beforeEventStuff(startTime) {
  timer(startTime, "decompte_etape0");
  console.log("En avance")
  updateProgressBar(0);
  for (let i = 0; i < 6; ++i) {
   hideElement("etape_" + (i +1));
  }
 
  showElement("etape_0");
}

/////////// Update Panels on step

function updateStepsStatus() {
  MemberStack.onReady.then(async function(member) {
    var metadata = await member.getMetaData();
    var timers = metadata["currentProjectTimers"];
var now = parseInt(Date.now() /1000 | 0);
   
    if (parseInt(timers[0].split("-")[0]) > now) {
    beforeEventStuff(parseInt(timers[0].split("-")[0]))
    } else if (parseInt(timers[timers.length -1].split("-")[1]) < now) {
    afterEventStuff();
    } else {
    doStuffForCurrentStep(timers, now);
    }
  })
}

function afterEventStuff() {
for (let i = 0; i < 6; ++i) {
   hideElement("etape_" + i);
  }
  showElement("etape_6");
  updateProgressBar(6)
}

function doStuffForCurrentStep(timers, now) {
hideElement("etape_0");
for (let i = 0; i < timers.length; ++i) {
    if ((parseInt(timers[i].split("-")[0]) < now) && (parseInt(timers[i].split("-")[1]) > now)) {
      timer(timers[i].split("-")[1], "decompte_etape" + (i +1));
      updateProgressBar(i +1);
      showElement("etape_" + (i +1));
    } else {
      hideElement("etape_" + (i +1));
    }
  }
}

function hideElement(id) {
console.log("Close " + id);
document.getElementById(id).style.display = "none";
}

function showElement(id) {
console.log("Show " + id);
document.getElementById(id).style.display = "";
}

function updateProgressBar(step) {
  var percentages = [5, 12, 31, 52, 72, 91, 100]
  console.log("pb " + step)
  document.getElementById("progressbar").style.width = percentages[step] + "%";
}

</script>
