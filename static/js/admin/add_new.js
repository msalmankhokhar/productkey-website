let addKeyBtns = document.querySelectorAll(".addKeyBtn");

function removeSubstring(str, substring) {
    if (str.endsWith(substring)) {
        return str.slice(0, str.lastIndexOf(substring));
    } else {
        return str;
    }
}

function addkey(keyText, platform, kind){
    console.log(`platform is ${platform}`);
    let keyBoxContainer = document.getElementById(`${kind}BoxContainer${platform}`);
    let keyInput = document.getElementById(`${kind}inputfor${platform}`);
    let keyBox = document.createElement('p');
    let div = document.createElement('div');
    keyBox.classList.add(`${kind}Box`);
    div.classList.add(`${kind}Boxholder`);
    div.setAttribute("style", "display: flex; align-items:center; column-gap:10px;");
    keyBox.innerText = keyText;
    keyInput.value += `${keyText},`;
    let delBtn = document.createElement('button');
    delBtn.setAttribute("type", "button");
    delBtn.setAttribute("onclick", "delKey(this)");
    delBtn.classList.add("delKeyBtn", "btn", "btn-primary");
    delBtn.innerText = "Delete";
    div.appendChild(keyBox);
    div.appendChild(delBtn);
    keyBoxContainer.appendChild(div);
}

function delKey(btn){
    let keyText = btn.previousElementSibling.innerText + ",";
    let keyInput = btn.parentElement.parentElement.nextElementSibling.nextElementSibling;
    let keyInputSmall = btn.parentElement.parentElement.nextElementSibling.nextElementSibling.nextElementSibling;
    keyInput.value = removeSubstring(keyInput.value, keyText);
    let keysContainer = btn.parentElement.parentElement;
    keysContainer.removeChild(btn.parentElement);
    console.log(`${keysContainer.children.length} childs inside keysContainer`);
    if (keysContainer.children.length == 0) {
        keyInputSmall.required = true;
        keyInputSmall.classList.add("requiredInput");
        console.log("set keyIput required att. true")
    }
}

// document.querySelectorAll(".delKeyBtn").forEach(btn => {
//     btn.addEventListener("click", (e)=>{
//     })
// });

addKeyBtns.forEach(addKeyBtn => {
    addKeyBtn.addEventListener("click", (e)=>{
        let keyText = addKeyBtn.previousElementSibling.value;
        let platform = addKeyBtn.getAttribute("platform");
        let kind = addKeyBtn.getAttribute("kind");
        if (keyText.length > 0 && keyText.length != "") {
            addkey(keyText, platform, kind);
            addKeyBtn.previousElementSibling.value = "";
            addKeyBtn.previousElementSibling.required = false;
        }
    })
});