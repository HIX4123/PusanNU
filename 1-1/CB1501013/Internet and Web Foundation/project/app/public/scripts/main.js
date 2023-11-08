// 유튜브를 선택한 경우
function youtube(key) {
    // UI 색상 변경
    let html = document.getElementsByTagName("html")[0];
    let header = document.getElementsByTagName("header")[0];
    let form = document.getElementsByTagName("form")[0];
    let footer = document.getElementsByTagName("footer")[0];

    html.style.backgroundColor = "#F28080";
    header.style.backgroundColor = "#F22727";
    form.style.backgroundColor = "#593232";
    footer.style.backgroundColor = "#F22727";

    // 유튜브 API 호출
    let youtubeEmbed = document.getElementById("YouTube video player");
    let xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            try{
            json = JSON.parse(this.responseText);} catch (e) {
                alert("ApiCallError: 데이터를 불러오지 못했습니다. 잠시 후 다시 시도해주세요.");
                return;
            }

            // 유튜브 임베디드 재생
            youtubeEmbed.src =
                "https://www.youtube.com/embed/" +
                json["items"][0]["id"]["videoId"];
            youtubeEmbed.style.display = "block";
            youtubeEmbed.scrollIntoView();
        }
    });

    xhr.open("GET", "http://localhost/youtube/?key=" + key);

    xhr.send();
}

// 네이버를 선택한 경우
function naver(key) {
    // UI 색상 변경
    let html = document.getElementsByTagName("html")[0];
    let header = document.getElementsByTagName("header")[0];
    let form = document.getElementsByTagName("form")[0];
    let footer = document.getElementsByTagName("footer")[0];

    html.style.backgroundColor = "#3C8040";
    header.style.backgroundColor = "#66D96E";
    form.style.backgroundColor = "#1E4020";
    footer.style.backgroundColor = "#66D96E";

    // 네이버 API 호출
    let xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            try {
                json = JSON.parse(this.responseText);
            } catch (e) {
                alert("ApiCallError: 데이터를 불러오지 못했습니다. 잠시 후 다시 시도해주세요.");
                return;
            }
            window.open(json["items"][0]["link"]);
            youtubeEmbed.style.display = "none";
        }
    });

    xhr.open("GET", "http://localhost/naver/?key=" + key);

    xhr.send();
}

let log = [];

//I'm feeling lucky 버튼을 누른 경우
function func1() {
    event.preventDefault(); //form 제출 시 새로고침 방지

    let key = document.getElementById("key").value;
    let target = document.getElementById("target").value;

    // 미입력시 경고 처리
    if (key == "") {
        alert("검색어를 입력해주세요.");
        return;
    }
    if (target == "") {
        alert("검색 대상을 선택해주세요.");
        return;
    }

    // 로그 기록
    log.unshift({
        time: new Date().toLocaleString(),
        key: key,
        target: target,
    });

    // 로그 테이블에 추가
    let table = document.getElementById("log");
    let tr = document.createElement("tr");
    let td1 = document.createElement("td");
    td1.innerHTML = log[0]["time"];
    let td2 = document.createElement("td");
    td2.innerHTML = log[0]["key"];
    let td3 = document.createElement("td");
    td3.innerHTML = log[0]["target"];
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    table.prepend(tr);

    // 검색 대상에 따라 함수 호출
    if (log[0].target == "youtube") {
        youtube(key);
    } else if (log[0].target == "naver") {
        naver(key);
    }
}

// Reset 버튼을 누른 경우
function func2() {
    // UI 색상 초기화
    let html = document.getElementsByTagName("html")[0];
    let header = document.getElementsByTagName("header")[0];
    let form = document.getElementsByTagName("form")[0];
    let footer = document.getElementsByTagName("footer")[0];

    html.style.backgroundColor = "";
    header.style.backgroundColor = "";
    form.style.backgroundColor = "";
    footer.style.backgroundColor = "";

    let youtubeEmbed = document.getElementById("YouTube video player");
    youtubeEmbed.style.display = "";
    html.scrollIntoView();
}