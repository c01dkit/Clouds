var url = window.location.href;

function delete_it(item, index) {
    try {
        item.parentNode.removeChild(item);
    } catch (error) {
        console.log(error);
    }
    
}
if (url.startsWith("https://www.baidu.com/s?")) {
    try {
        var child = document.getElementById("content_right");
        child.parentNode.removeChild(child);
    }
    catch (error) {
        console.log(error);
    }
}

else if (url.startsWith("https://www.jb51.net/")) {
    // 这个网站底部的广告好像删了以后会自动刷出来……算了不管了插个div完事
    try {
        var list = [];
        list.push(document.querySelector("#container > div.pt10.clearfix"));
        list.push(document.querySelector("#header"));
        list.push(document.querySelector("#main > div.main-right"));
  
        list.push(document.querySelector("#article > div.xgcomm.clearfix"));

        list.forEach(delete_it);
        var pad = document.createElement("div");
        pad.style.width = "100px";
        pad.style.height = "1400px";
        var final_item = document.querySelector("#content > div.art_xg");
        final_item.parentNode.appendChild(pad);
    } catch (error) {
        console.log(error);
    }
}
