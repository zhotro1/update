<script type="text/javascript">
		function support_mp3() {
			var a = document.createElement('audio');
			return !!(a.canPlayType && a.canPlayType('audio/mpeg;').replace(/no/, ''));	
		}
		var soundarray = 0;
		
		function checkfors3(s3file, silent) {
			var s3checkreq = new XMLHttpRequest();
			s3checkreq.open("POST", 'https://ttsmp3.com/inc/checks3.php?id=' + s3file, true);
			s3checkreq.send( null );
			s3checkreq.onreadystatechange = function (e) {
				if (this.readyState == 4 && this.status == 200) {
					s3checker = this.responseText;
					if (s3checker == 0) {
						setTimeout(function(){
							checkfors3(s3file, silent);
						}, 2000);
						
					}
					else {
						var s3filepath = "https://s3.ca-central-1.amazonaws.com/ttsmp3files/" + s3file + ".mp3";
						
						var myaudio = new Audio(s3filepath);
						document.getElementById("s3loader").style.display = "none"; 
						myaudio.addEventListener("playing", function() 
						 {
							document.getElementById("vorlesenbutton").disabled = false; 
							document.getElementById("vorlesenbutton").value = "Reading...";
						 });
						myaudio.addEventListener("ended", function() 
						 {
							document.getElementById("vorlesenbutton").disabled = false; 
							document.getElementById("vorlesenbutton").value = "Read";
						 });
						myaudio.addEventListener('error', function failed(e) {
							switch (e.target.error.code) {
							 case e.target.error.MEDIA_ERR_SRC_NOT_SUPPORTED:
							   alert('Your audio file was created but is corrupt. Please check your message for invalid characters.');
							   enablebuttons();
							   break;
						   }
						 }, true);
						if (silent == 0) {
							myaudio.play();
						}
						else {
							godownload(s3file, "s3");
							enablebuttons();
						}
					}
				}
			}			

		}

		

		function escapeRegExp(str) {
			return str.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1");
		}
		function replaceAll(str, find, replace) {
			return str.replace(new RegExp(escapeRegExp(find), 'g'), replace);
		}
		function enablebuttons() {
			document.getElementById("vorlesenbutton").disabled = false;
			document.getElementById("vorlesenbutton").value = "Read";
		}
		function playsound(silent) {
			if (!support_mp3()) {
				alert("Sorry, your current browser does not support playing MP3 files, please switch to a different browser, i.e. Chrome, Firefox. Thank you");
			}
			else {
				document.getElementById("vorlesenbutton").disabled = true; 
				document.getElementById("vorlesenbutton").value = "Creating...";
				var voicetext = document.getElementById('voicetext').value;
				if (voicetext == "") { alert("Please input text."); document.getElementById("vorlesenbutton").disabled = false; }
				var e = document.getElementById("sprachwahl");
				var lang = e.options[e.selectedIndex].value;
				var httpreq = new XMLHttpRequest();
				voicetext = encodeURIComponent(replaceAll(voicetext, "&"," and "));
				var params = "msg="+voicetext+"&lang="+lang+"&source=ttsmp3";
				httpreq.open("POST", 'https://ttsmp3.com/makemp3_new.php', true);
				httpreq.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
				httpreq.overrideMimeType("application/json");
				httpreq.onreadystatechange = function (e) {
					if (this.readyState == 4 && this.status == 200) {
						try {
							soundarray = JSON.parse(this.responseText);
							if (soundarray["Error"] == 0) {
								if (soundarray["tasktype"] != "s3") {
									console.log("direct processing");
									var myaudio = new Audio(soundarray["URL"]);
									myaudio.addEventListener("playing", function() 
									 {
										document.getElementById("vorlesenbutton").disabled = false; 
										document.getElementById("vorlesenbutton").value = "Reading...";
									 });
									myaudio.addEventListener("ended", function() 
									 {
										document.getElementById("vorlesenbutton").disabled = false; 
										document.getElementById("vorlesenbutton").value = "Read";
									 });
									myaudio.addEventListener('error', function failed(e) {
										switch (e.target.error.code) {
										 case e.target.error.MEDIA_ERR_SRC_NOT_SUPPORTED:
										   alert('Your audio file was created but is corrupt. Please check your message for invalid characters.');
										   enablebuttons();
										   break;
									   }
									 }, true);
									if (silent == 0) {
										myaudio.play();
									}
									else {
										godownload(soundarray["MP3"], "direct");
										enablebuttons();
									}
								}
								else {
									console.log("task processing");
									document.getElementById("s3loader").style.display = "block"; 
									checkfors3(soundarray["s3task"], silent);
									
								}
							}
							else {
								alert(soundarray['Error']);
								if (soundarray['Error'] == "Usage Limit exceeded") {
									var d = Math.random();
										if (d < 1) {
											window.location = "https://ttsmp3.com/register?click=jsredirect";
										//	window.open("https://ttsmp3.com/register?click=jsredirect", "_blank");
										}
										else {
											$("#sprachwahl").fadeOut("slow");
											$("#vorlesenbutton").fadeOut("slow");
											$("#downloadenbutton").fadeOut("slow");
											$("#limitannounce").fadeIn("slow");
										}
										
								}
								enablebuttons();
							}
						}
						catch (err) {
							alert("Something went wrong... please contact support@ttsmp3.com for support");
							enablebuttons();
						}
					}
				}
				httpreq.send(params);				
			}
		}
		function godownload(playthis, location) {
			if (!support_mp3()) {
				alert("Sorry, your current browser does not support playing MP3 files, please switch to a different browser, i.e. Chrome, Firefox. Thank you :-)");
			}
			else {
				// alert(playthis);
				playthis = playthis || "";
				var voicetext = document.getElementById('voicetext').value;
				if (voicetext == "") { alert("Please input text."); die; }
				var e = document.getElementById("sprachwahl");
				var lang = e.options[e.selectedIndex].value;
				if (((soundarray != 0) && (soundarray["Text"] == voicetext)) || (playthis != "")) {

					if (playthis != "") { soundarray["MP3"] = playthis; }
					if (typeof location === "undefined") { location = soundarray["tasktype"]; }
					var httpreq = new XMLHttpRequest();
					httpreq.open("GET", 'https://ttsmp3.com/dlmp3.php?mp3='+soundarray["MP3"] + "&location=" + location, true);
					httpreq.responseType = "blob";
					httpreq.onreadystatechange = function (e) {
						if (this.readyState == 4 && this.status == 200) {
							try {
								var blob = new Blob([this.response], {type:'audio/mp3'});
								var today = new Date();
								var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
								var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
								saveAs(blob, "ttsMP3.com_VoiceText_"+date+"_"+time+".mp3");
							}
							catch (err) {
								alert("Something went wrong... please contact support@ttsmp3.com for support");
							}
						}
					}
					httpreq.send();
				}
				else {
					playsound(1);
				}
			}
		}
				
		function dontsubmit() {
			return false;
		}

	</script>