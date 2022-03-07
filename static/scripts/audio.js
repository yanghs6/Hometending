setCookie = (cookie_name, value, miuntes) => {
    const exdate = new Date();
    exdate.setMinutes(exdate.getMinutes() + miuntes);
    
    const domain = window.location.host;
    const cookie_value = escape(value) + ((miuntes == null) ? '' : '; expires=' + exdate.toUTCString()) + ";path=/;" ;

    document.cookie = cookie_name + '=' + cookie_value;
}

getCookie = (cookie_name) => {
    var x, y;
    var val = document.cookie.split(';');

    for (var i = 0; i < val.length; i++) {
        x = val[i].substr(0, val[i].indexOf('='));
        y = val[i].substr(val[i].indexOf('=') + 1);
        x = x.replace(/^\s+|\s+$/g, ''); // 앞과 뒤의 공백 제거하기
        if (x == cookie_name) {
            return unescape(y); // unescape로 디코딩 후 값 리턴
        }
    }
    return "0";
}

const bgm = document.getElementById("bgm");
bgm.currentTime = parseInt(getCookie('time'), 10) + 0.5;
bgm.volume = 0.2;

bgm.onended = () => {
    bgm.currentTime = 0;
    bgm.play();
}

window.onpagehide = () => {
    setCookie('time', bgm.currentTime, 300);
    console.log("전환")
}

window.onbeforeunload = () => {
    setCookie('time', bgm.currentTime, 300);
    console.log("새로")
}
