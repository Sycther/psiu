// Your API KEY
const API_KEY = "AIzaSyCdYd2JqL12cCzz4HoGcre_2xcd_13pDGY";

const tableWrapperFront = `<>`;

const tableWrapperBacl = ``;

const cellWrapperFront = `
<div>
    <div class="wsite-image wsite-image-border-none wsite-image-border-black" style="padding-top:10px;padding-bottom:10px;margin-left:0px;margin-right:0px;text-align:center">
        <a>
            <img src="https://drive.google.com/uc?export=view&id=`;

const cellWrapperBack = `
" alt="NAME" style="width:353;max-width:100%" />
        </a>
        <div style="display:block;font-size:90%"></div>
    </div>
</div>
`;

const rowDivider = `
<div>
    <div style="height: 20px; overflow: hidden; width: 100%;"></div>
    <hr class="styled-hr" style="width:100%;"></hr>
    <div style="height: 20px; overflow: hidden; width: 100%;"></div>
</div>
`;

function displayResult2(response) {
    let tableBody = "";
    let columnNum = 1;

    response.result.values.forEach((row, index) => {
        if (index > 0) {
            if (columnNum === 1) {
                tableBody += "<tbody><tr>";
            }

            tableBody += "<td>";
            let text = "";
            let imgId = "";
            let colI = 0;
            row.forEach((val) => {
                if (colI === 0) {
                    text += "<strong>" + val + "</strong> <br />";
                } else if (colI === 1) {
                    text += "<em>" + val + "</em> <br />"
                } else if (colI === 2) {
                    text += val + "<br />"
                } else if (colI === 3) {
                    imgId = val;
                }
                colI += 1;
            });
            tableBody += cellWrapperFront + imgId + cellWrapperBack;
            tableBody += '<div style="text-align:center;">' + text + "</div>"

            tableBody += "</td>";

            if (columnNum === 3) {
                columnNum = 1;
                tableBody += "</tr></tbody>" + rowDivider;
            } else { columnNum += 1; }

        }
    });

    document.getElementById("table").innerHTML = tableBody;
}

function loadData() {
    // Spreadsheet ID
    const spreadsheetId = "1bDsre6HGd51MQnORGjGZHF2KmWk0eDlCBrmBjBmWjNE";
    const range = "A:Z";
    getPublicValues({ spreadsheetId, range }, displayResult2);
}

window.addEventListener("load", (e) => {
    initOAuthClient({
        apiKey: API_KEY
    });
});

document.addEventListener("gapi-loaded", (e) => {
    console.log("Gapi is loaded");
    loadData();
});