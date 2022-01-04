let Data = {"Title": "", "URL": ""}

function clickHandler(e) {
    let req = new XMLHttpRequest();
    req.open('GET', "http://localhost:8000/save?p=https://zenn.dev/catnose99", true);
    req.onload = function() {
        console.log("保存に成功しました");
    }
    req.send();
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.btn-save').addEventListener('click', clickHandler);
});