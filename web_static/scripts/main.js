const myImage = document.querySelector("img");
myImage.onclick = ()=>{
    const mySrc = myImage.getAttribute("src");
    if (mySrc === "images/abnb_logo.png"){
        myImage.setAttribute("src", "images/icon_pets.png");
    }else{
        myImage.setAttribute("src", "images/abnb_logo.png");
    }
};