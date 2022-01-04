function clickHandler(e) {
    let url = document.getElementById("url").value;
    let req = new XMLHttpRequest();
    req.open('GET', `http://localhost:8000/save?p=${url}`, true);
    req.onload = function() {
        console.log("保存に成功しました");
    }
    req.send();
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.btn-save').addEventListener('click', clickHandler);
});