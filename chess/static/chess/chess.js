let fields = document.getElementsByClassName('boardField');
let board = new Array(8);
let activeField = {row:null, col:null};
let moveable = false;

setInterval(refreshBoard, 3000);

for(i=0;i<board.length;i++){
    board[i] = new Array(8);
}
let fieldCounter = 0;
for(i = 0; i<board.length; i++){
    for(j = 0; j<board[i].length; j++){
        board[i][j] = fields[fieldCounter];
        fieldCounter ++;
    }
}

for(i=0;i<board.length;i++){
    for(j=0;j<board[i].length;j++){

        board[i][j].addEventListener('click', selectField);

        if(i % 2 == 0 && j % 2 != 0){
            board[i][j].style.backgroundColor = 'black';
            board[i][j].style.color = 'white';
        } else if(i % 2 != 0 && j % 2 == 0){
            board[i][j].style.backgroundColor = 'black';
            board[i][j].style.color = 'white';
        }
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function selectField(){
    field = this;
    req = new XMLHttpRequest();

    req.open('GET', '/chess/moveable', true);
    req.setRequestHeader('X-CSRFToken', csrftoken);
    req.send();
    req.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            if(this.responseText == 'False'){
                moveable = false;

            }else{
                moveable = true;
                if(field.innerHTML != decodeURIComponent('%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20')){
                    removeBorderStyle();
                    for(i=0;i<board.length;i++){
                        for(j=0;j<board[i].length;j++){
                            if(board[i][j] == field){
                                indexRow = i;
                                indexCol = j;
                            }
                        }
                    }
                    field.style.border = '3px solid  #d7dbdd ';
                    activeField.row = indexRow;
                    activeField.col = indexCol;

                    getPossibleMoves(field);


                }
            }

        }
    }

}

function getPossibleMoves(field){

    movesResponse = new Array();
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            possibleMoves = this.responseText;
            movesArray = possibleMoves.split(',');

            for(i=0;i<movesArray.length;i++){
                move = {row:movesArray[i].split('|')[0], col:movesArray[i].split('|')[1]};
                //console.log(movesResponse.length)
                row = move.row;
                col = move.col;
                board[row][col].style.border = '3px solid #91e30a';
                board[row][col].removeEventListener('click', selectField);
                board[row][col].addEventListener('click', moveFigur);

            }

        }

    };

    type = field.innerHTML;
    var getRequest = 'row=' + indexRow + '&' + 'col=' + indexCol + '&' + 'type=' + type;
    console.log(getRequest);
    xhttp.open('GET', '/chess/selectField?'+getRequest, true);
    xhttp.setRequestHeader('X-CSRFToken', csrftoken);
    xhttp.send();

}

function moveFigur(){
    for(i=0;i<board.length;i++){
        for(j=0;j<board[i].length;j++){
            if(this == board[i][j]){
                ajaxMove = new XMLHttpRequest();
                ajaxMove.onreadystatechange = function(){
                    if (this.readyState == 4 && this.status == 200) {
                        xmlDoc = this.responseXML;
                        ajaxArray = xmlDoc.getElementsByClassName('boardField');

                        let counter = 0;
                        for(x = 0; x<board.length; x++){
                            for(y = 0; y<board[x].length; y++){
                                board[x][y].innerHTML = ajaxArray[counter].innerHTML;
                                console.log('hallohallo');
                                board[x][y].removeEventListener('click', moveFigur);
                                board[x][y].removeEventListener('click', selectField);
                                board[x][y].addEventListener('click', selectField);
                                counter ++;
                            }
                        }
                        removeBorderStyle();
                    }
                }

                ajaxMove.open('GET', '/chess/move?row1=' + activeField.row + '&col1=' + activeField.col + '&row2=' + i + '&col2=' + j, true);
                ajaxMove.setRequestHeader('X-CSRFToken', csrftoken);
                ajaxMove.send();
                activeField.row = null;
                activeField.col = null;
            }
        }
    }
    //this.addEventListener('click', selectField);
}

function removeBorderStyle(){
    for(i=0;i<board.length;i++){
        for(j=0;j<board[i].length;j++){
            //console.log(board);
            board[i][j].style.border = '1px solid black';
        }
    }
}

function refreshBoard(){

    ajaxReq = new XMLHttpRequest();
    ajaxReq.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            let c = 0;
            for(x = 0; x<board.length; x++){
                for(y = 0; y<board[x].length; y++){
                    board[x][y].innerHTML =this.responseText[c] ;
                    c ++;
                }
            }
        }
    }
    ajaxReq.open('GET', '/chess/refresh', true);
    ajaxReq.setRequestHeader('X-CSRFToken', csrftoken);
    ajaxReq.send();
}


