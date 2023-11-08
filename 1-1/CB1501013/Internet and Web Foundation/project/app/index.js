// Node.js express 구축
const express = require("express");
const app = express();
const port = 80;

app.use("/public", express.json("public"));

// 도메인 설정
app.get("/", (_req, res) => {
    res.sendFile(__dirname + "/public/index.html");
});
app.get("/styles/styles.css", (_req, res) => {
    res.sendFile(__dirname + "/public/styles/styles.css");
});
app.get("/styles/youtubeEmbed.css", (_req, res) => {
    res.sendFile(__dirname + "/public/styles/youtubeEmbed.css");
});
app.get("/scripts/main.js", (_req, res) => {
    res.sendFile(__dirname + "/public/scripts/main.js");
});

// 패비콘 설정
let favicon = require("serve-favicon")
app.use(favicon(__dirname + "/public/images/fabicon/favicon.ico"));

app.get("/images/fabicon/android-icon-36x36.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/android-icon-36x36.png");
});
app.get("/images/fabicon/android-icon-48x48.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/android-icon-48x48.png");
});
app.get("/images/fabicon/android-icon-72x72.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/android-icon-72x72.png");
});
app.get("/images/fabicon/android-icon-96x96.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/android-icon-96x96.png");
});
app.get("/images/fabicon/android-icon-144x144.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/android-icon-144x144.png");
});
app.get("/images/fabicon/android-icon-192x192.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/android-icon-192x192.png");
});
app.get("/images/fabicon/apple-icon-57x57.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-57x57.png");
});
app.get("/images/fabicon/apple-icon-60x60.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-60x60.png");
});
app.get("/images/fabicon/apple-icon-72x72.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-72x72.png");
});
app.get("/images/fabicon/apple-icon-76x76.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-76x76.png");
});
app.get("/images/fabicon/apple-icon-114x114.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-114x114.png");
});
app.get("/images/fabicon/apple-icon-120x120.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-120x120.png");
});
app.get("/images/fabicon/apple-icon-144x144.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-144x144.png");
});
app.get("/images/fabicon/apple-icon-152x152.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-152x152.png");
});
app.get("/images/fabicon/apple-icon-180x180.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-180x180.png");
});
app.get("/images/fabicon/apple-icon-precomposed.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon-precomposed.png");
});
app.get("/images/fabicon/apple-icon.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/apple-icon.png");
});
app.get("/images/fabicon/browserconfig.xml", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/browserconfig.xml");
});
app.get("/images/fabicon/favicon-16x16.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/favicon-16x16.png");
});
app.get("/images/fabicon/favicon-32x32.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/favicon-32x32.png");
});
app.get("/images/fabicon/favicon-96x96.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/favicon-96x96.png");
});
app.get("/images/fabicon/favicon.ico", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/favicon.ico");
});
app.get("/favicon.ico", (_req, res) => {
    res.sendFile(__dirname + "/favicon.ico");
});
app.get("/images/fabicon/manifest.json", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/manifest.json");
});
app.get("/images/fabicon/ms-icon-70x70.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/ms-icon-70x70.png");
});
app.get("/images/fabicon/ms-icon-144x144.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/ms-icon-144x144.png");
});
app.get("/images/fabicon/ms-icon-150x150.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/ms-icon-150x150.png");
});
app.get("/images/fabicon/ms-icon-310x310.png", (_req, res) => {
    res.sendFile(__dirname + "/public/images/fabicon/ms-icon-310x310.png");
});

//Youtube API 호출 및 반환
app.get("/youtube", function (req, res) {
    let q = req.query.key; // 검색어

    let request = require("request");
    let options = {
        method: "GET",
        url: encodeURI(
            "https://www.googleapis.com/youtube/v3/search?key=AIzaSyBbyMgSvazysCRdXDyG8AMzuC1kCFO1NGA&type=video&maxResults=1&q=" +
                q
        ),
        headers: {},
    };
    request(options, function (error, response) {
        if (error) throw new Error(error);
        res.send(response.body);
    });
});

//Naver API 호출 및 반환
app.get("/naver", function (req, res) {
    q = req.query.key; // 검색어
    var request = require("request");
    var options = {
        method: "GET",
        url: encodeURI(
            "https://openapi.naver.com/v1/search/webkr.json?display=1&query=" +
                q
        ),
        headers: {
            "X-Naver-Client-Id": "HH2fJNFYyJKtPz_WyAl8",
            "X-Naver-Client-Secret": "TymPEM45jw",
        },
    };
    request(options, function (error, response) {
        if (error) throw new Error(error);
        res.send(response.body);
    });
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
