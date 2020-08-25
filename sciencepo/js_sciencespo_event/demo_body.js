<script>

setTestingMetadataValues()
updateStepsStatus()

var checkExist = setInterval(function() {
   if (document.getElementsByClassName("crisp-kquevr").length) {
      document.getElementsByClassName("crisp-kquevr")[0].style="margin-bottom:75px !important;"
      clearInterval(checkExist);
   }
}, 100);

</script>