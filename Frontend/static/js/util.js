
function fetchAsync_json(url, method){
    let xhr = new XMLHttpRequest()
    xhr.open(method, url, false);
    xhr.onload = ()=>{
        let r_json = JSON.parse(xhr.responseText);
        console.log(`recived sw text is ${xhr.responseText}`)
        return r_json
    }
    xhr.send()
    return xhr.onload()
}

function getSoftwareInfo(sw_id){
//     fetch(`http://ec2-13-56-230-83.us-west-1.compute.amazonaws.com/api/getSoftwareInfo/${sw_id}`,
//     { 
//         method: "GET" 
//     }
// ).then((response)=>{ 
//     return response.json().then((jsonResponse)=>{
//         return jsonResponse
//     })
// })

return fetchAsync_json(`http://ec2-13-56-230-83.us-west-1.compute.amazonaws.com/api/getSoftwareInfo/${sw_id}`, "GET")
}

function gotoSwInfoPage(sw_id) {
     let sw = fetchAsync_json(`http://ec2-13-56-230-83.us-west-1.compute.amazonaws.com/api/getSoftwareInfo/${sw_id}`, "GET");
    //  let sw = getSoftwareInfo(sw_id);
    console.log(`software is ${sw}`)
    document.open()
    document.write(
    `
    <!doctype html>
    <html lang="en">
    
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Key.es</title>
        <meta name="description" content="We provide genuine activation keys of popular paid softwares">
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <!-- <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet"> -->
        <link rel="stylesheet" href="static/css/bg.css">
        <link rel="stylesheet" href="static/css/comman2.css">
        <link rel="stylesheet" href="static/css/home.css">
    </head>
    
    <!-- <div class="container">
      </div> -->
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
    *{
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
    }
    
    body{
      /* background: #f4f5;
      padding: 0 20px; */
    }
    
    ::selection{
      color: #fff;
      background: #664AFF;
    }
    
    #container{
      /* box-sizing: content-box; */
      max-width: 500px;
      margin: 10px auto;
      
    }
    
    .container .searchInput{
      background: #fff;
      width: 100%;
      border-radius: 5px;
      position: relative;
      box-shadow: 0px 1px 5px 3px rgba(0,0,0,0.12);
    }
    
    .searchInput input{
      height: 55px;
      width: 100%;
      outline: none;
      border: none;
      border-radius: 5px;
      padding: 0 60px 0 20px;
      font-size: 18px;
      box-shadow: 0px 1px 5px rgba(0,0,0,0.1);
    }
    
    .searchInput.active input{
      border-radius: 5px 5px 0 0;
    }
    
    .searchInput .resultBox{
      padding: 0;
      opacity: 0;
      pointer-events: none;
      max-height: 280px;
      overflow-y: auto;
      position: absolute;
      z-index: 1;
      width: 100%;
      background: #fff;
      box-shadow: 0px 1px 5px 3px rgba(0,0,0,0.12);
    }
    
    .searchInput.active .resultBox{
      padding: 10px 8px;
      opacity: 1;
      pointer-events: auto;
    }
    
    .resultBox li{
      list-style: none;
      padding: 8px 12px;
      display: none;
      width: 100%;
      cursor: default;
      border-radius: 3px;
    }
    
    .searchInput.active .resultBox li{
      display: flex;
      column-gap: 10px;
      align-items: center;
    }
    .resultBox li:hover{
      background: #efefef;
    }
    
    .searchInput .icon{
      position: absolute;
      right: 0px;
      top: 0px;
      height: 55px;
      width: 55px;
      text-align: center;
      line-height: 55px;
      font-size: 20px;
      color: #644bff;
      cursor: pointer;
    }
    </style>
    
    <style>
        #main{
            height: 100%;
            display: flex;
            flex-direction: column;
            row-gap: 20px;
            padding: 20px 20px;
        }
        #itemThumbnail{
            width: 100px;
        }
        #desc{
            font-size: 0.85rem;
            color: #545454;
        }
        </style>
    
    <body>
    
      <div>
        <div class="wave"></div>
        <div class="wave"></div>
        <div class="wave"></div>
     </div>
    
    <div class="container" id="container">
    
      
      <div id="header">
        <h1 class="text-center">Keeys.site</h1>
        <p class="text-center">Online Product keys Archive</p>
      </div>
      <div id="contentWrapper">
        <img id="itemThumbnail" src="${sw["imgSrc"]}" alt="thumbnail">
        <p id="desc">${sw["desc"]}</p>
        <button class="mybtn" href="/get_key/${sw["id"]}" onclick="gotoGetKeyPage(${sw["id"]})">Get license key</button>
        </div>
        
    </div>
    </body>
    <script src="static/js/util.js"></script>
    
    </html>
    `
    );
    document.close()
}







function gotoGetKeyPage(sw_id) {
     let sw = fetchAsync_json(`http://ec2-13-56-230-83.us-west-1.compute.amazonaws.com/api/getSoftwareInfo/${sw_id}`, "GET");
    //  let sw = getSoftwareInfo(sw_id);
    // console.log(`software is ${sw}`)
    document.open()
    document.write(
    `
    <!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Key.es</title>
    <meta name="description" content="We provide genuine activation keys of popular paid softwares">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <!-- <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet"> -->
    <link rel="stylesheet" href="static/css/bg.css">
    <link rel="stylesheet" href="static/css/comman2.css">
    <link rel="stylesheet" href="static/css/home.css">
</head>

<!-- <div class="container">
  </div> -->
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
*{
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

body{
  /* background: #f4f5;
  padding: 0 20px; */
}

::selection{
  color: #fff;
  background: #664AFF;
}

#container{
  /* box-sizing: content-box; */
  max-width: 500px;
  margin: 10px auto;
  
}

.container .searchInput{
  background: #fff;
  width: 100%;
  border-radius: 5px;
  position: relative;
  box-shadow: 0px 1px 5px 3px rgba(0,0,0,0.12);
}

.searchInput input{
  height: 55px;
  width: 100%;
  outline: none;
  border: none;
  border-radius: 5px;
  padding: 0 60px 0 20px;
  font-size: 18px;
  box-shadow: 0px 1px 5px rgba(0,0,0,0.1);
}

.searchInput.active input{
  border-radius: 5px 5px 0 0;
}

.searchInput .resultBox{
  padding: 0;
  opacity: 0;
  pointer-events: none;
  max-height: 280px;
  overflow-y: auto;
  position: absolute;
  z-index: 1;
  width: 100%;
  background: #fff;
  box-shadow: 0px 1px 5px 3px rgba(0,0,0,0.12);
}

.searchInput.active .resultBox{
  padding: 10px 8px;
  opacity: 1;
  pointer-events: auto;
}

.resultBox li{
  list-style: none;
  padding: 8px 12px;
  display: none;
  width: 100%;
  cursor: default;
  border-radius: 3px;
}

.searchInput.active .resultBox li{
  display: flex;
  column-gap: 10px;
  align-items: center;
}
.resultBox li:hover{
  background: #efefef;
}

.searchInput .icon{
  position: absolute;
  right: 0px;
  top: 0px;
  height: 55px;
  width: 55px;
  text-align: center;
  line-height: 55px;
  font-size: 20px;
  color: #644bff;
  cursor: pointer;
}
</style>
<style>
    #contentWrapper{
        display: flex;
        flex-direction: column;
        row-gap: 20px;
        padding: 20px 20px;
        justify-content: space-evenly;
        align-items: center;
    }
    #main{
        height: 100%;
        display: flex;
        flex-direction: column;
        row-gap: 20px;
        padding: 20px 20px;
    }
    #itemThumbnail{
        width: 75px;
    }
    #swWrapper{
        display: flex;
        flex-direction: column;
        row-gap: 10px;
        align-items: center;
    }
    #procInfo{
        font-size: 140%;
        text-align: center;
        line-height: 0px;
    }
    #swname{
        font-size: 120%;
    }
    #procContainer{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: stretch;
        row-gap: 22px;
    }
    #keyCont{
        align-self: center;
        box-shadow: 1px 1px 6px gray;
        padding: 15px;
        border-radius: 5px;
        /* font-weight: bold; */
        color: #5a5a5a;
    }
    #spinner{
        align-self: center;
    }
    </style>

<body>

  <div>
    <div class="wave"></div>
    <div class="wave"></div>
    <div class="wave"></div>
 </div>

<div class="container" id="container">

  
  <div id="header">
    <h1 class="text-center">Key.es</h1>
    <p class="text-center">Online Product keys Archive</p>
  </div>
  <div id="contentWrapper">

    <div id="swWrapper">
        <img id="itemThumbnail" src="${sw["imgSrc"]}" alt="thumbnail">
        <span id="swname">${sw["name"]}</span>
    </div>
    <div id="procContainer">
        <p id="procInfo">Processing your request</p>
        <!-- <div class="text-center"> -->
            <div id="spinner" class="spinner-border text-secondary" style="width: 3rem; height: 3rem;" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        <!-- </div> -->
        <div id="keyCont" style="display: none;">
            3AVVC-2JBOF-BXN1D-YN9E6
        </div>
        <div class="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
            <div id="pBar" class="progress-bar progress-bar-striped progress-bar-animated" style="width: 0%"></div>
        </div>
    </div>        

    </div>
    
</div>
</body>

<script>
    let keys_list = [
        "0TD7R-Y3KMG-HU2A7-F4C5J",
        "NVFMH-W1HYN-Y60O9-7WMCL",
        "A6HVX-BQVSH-X22H7-WTBDR",
        "O6TFU-9E2RS-NCL6T-0DMTY",
        "7P5WO-LIKUR-ZS3V7-DI0GP",
        "Q3MX5-Z71RD-D1X8P-CYPR1",
        "1V134-Q244Y-DJ2QP-2BX8N",
        "V7L9T-TEGWK-W6LOV-Z0CG3",
        "SZMAQ-JUE2N-G6PQX-I1QE9",
        "M1CSY-4TM6Y-S1HWQ-AR8VL",
        "ASNKY-P0W1C-LO9GL-P9F42",
        "ATE4N-ET1EP-X2ENR-QX9C9",
        "P0MI8-5UR11-94IU4-1SKFF",
        "12CFU-TOBNF-E5VRE-8O71Y",
        "9SY3A-3QGUP-984FM-XMGNS",
        "WZVSB-BGW30-O4YRB-4A9T7",
        "E2EMR-JNAWP-1FEPH-YVGIN",
        "1NJMA-X4S6W-BEAUB-Z3U0B",
        "UKYI4-4SFOH-VVASQ-3IXIB",
        "UKYI4-4SFOH-VVASQ-3IXIB",
        "ZMCG8-1M8Z9-ET06R-Y4I1K",
        "NP12R-UOG6K-048T6-ETIDQ",
        "K0YI2-ZM354-SR7A5-4QEDD",
    ]

    function generate_random_key(){
        const randomIndex = Math.floor(Math.random() * keys_list.length);
        keyCont.innerHTML = keys_list[randomIndex];
    }


	function getRandomInt( min, max ) {
         return Math.floor( Math.random() * ( max - min + 1 ) ) + min;
    }
    
	function generateProductKey() {
		var tokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
			chars = 5,
			segments = 4,
			keyString = "";
			
		for( var i = 0; i < segments; i++ ) {
			var segment = "";
			
			for( var j = 0; j < chars; j++ ) {
			    var k = getRandomInt( 0, 35 );
				segment += tokens[ k ];
			}
			
			keyString += segment;
			
			if( i < ( segments - 1 ) ) {
				keyString += "-";
			}
		}
		
		// return keyString;
        keyCont.innerHTML = keyString;

	}
</script>

<script>
   let info = document.getElementById("procInfo");
   let pBar = document.getElementById("pBar");
   let spinner = document.getElementById("spinner");
   let keyCont = document.getElementById("keyCont");
   let pBar_length = 0;
   let infoList = [
    "Connecting to server",
    "Fetching required data",
    "Performing Auto-Unlock",
    "Fetching product key"
];
   let currentIndex = 0;
   
   let progress_interval = setInterval(updateInfo, 2000);
   
   function showFinalKey(key){
    spinner.style.display = "none";
    info.innerHTML = "Congrats! Your key is";
    keyCont.innerHTML = key;
    keyCont.style.backgroundColor = "green";
    keyCont.style.color = "white";
   }
   
   function updateInfo(){
    let txt = infoList[currentIndex];
    pBar_length += 25;
    pBar.style.width = pBar_length.toString() + "%";
    info.innerHTML = txt;
    console.log(txt);
    currentIndex++;

    if (currentIndex === infoList.length){
        clearInterval(progress_interval);
        keyCont.style.display = "block";
        let suffleKeyInterval = setInterval(generate_random_key, 200);
        setTimeout(() => {
            fetch("http://ec2-13-56-230-83.us-west-1.compute.amazonaws.com/product_key/${sw["id"]}", { 
                method: "GET" }).then((resp)=>{
                    return resp.json().then((respText)=>{
                        clearInterval(suffleKeyInterval);
                        showFinalKey(respText["key"]);
                        pBar.parentElement.style.display = "none";
                    })
                })
        }, 5000);
    }
   }
   
</script>
</html>

    `
    );
    document.close()
}