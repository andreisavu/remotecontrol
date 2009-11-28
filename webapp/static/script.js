
function init() {
    function keyval(n) {
        if (n == null) return 'undefined';
        var s= '' + n;
        if (n >= 32 && n < 127) s+= ' (' + String.fromCharCode(n) + ')';
        while (s.length < 9) s+= ' ';
        return s;
    }

    function showmesg(t) {
       var el = document.getElementById("log");
       var old= el.value;
       el.value= old + t + '\n';
    }

    function pressmesg(w,e) {
       showmesg(w + '  keyCode=' + keyval(e.keyCode) +
                     ' which=' + keyval(e.which) +
                     ' charCode=' + keyval(e.charCode));
       showmesg(' shiftKey='+e.shiftKey
              + ' ctrlKey='+e.ctrlKey
              + ' altKey='+e.altKey
              + ' metaKey='+e.metaKey);
    }

    function suppressdefault(e,flag) {
       if (flag) {
           if (e.preventDefault) e.preventDefault();
           if (e.stopPropagation) e.stopPropagation();
       }
       return !flag;
    }

    function keypress(e) {
       if (!e) e= event;
       pressmesg('keypress',e);
       return suppressdefault(e, true);
    }

    if(document.addEventListener) {
        document.addEventListener("keypress", keypress, false);
    } else if(document.attachEvent) {
        document.attachEvent("onkeypress", keypress);
    } else {
        document.onkeypress = keypress;
    }
}

