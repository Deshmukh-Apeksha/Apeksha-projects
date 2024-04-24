console.log=alert("something went wrong!")

const hour=document.getElementById("Hours");
const minute=document.getElementById("Minutes");
const second=document.getElementById("Seconds");
const ampm=document.getElementById("ampm");

function updateClock()
{
    let h =new Date().getHours();
    let m =new Date().getMinutes();
    let s=new Date().getSeconds();
    let ampm ="AM";
    if(h>12)
    {
        h=h-12;
        ampm="PM";
    }
    h = h < 10 ? '0'+ h : h ; 
    m = h < 10 ? '0'+ m : m;
    s = h < 10 ? '0'+ s: s;
    hour.innerText = h;
    minute.innerText=m;
    second.innerText=s;
    ampm,(innerText=ampm);
    setTimeout(()=>{
        updateClock();
    }
    ,1000);
}
updateClock();