$(document).ready(function () {
    $("#popular").mouseover(function () {
        // if($("#p-word").css("display")=="block"){
        // $("#p-word").css("display")="block";    
        $("#p-word").fadeOut();
        // $("#p-word").attr('style', 'display:none');
        // $("#c-word").attr('style', 'display:block');
        // $("#h-word").attr('style', 'display:block');
        $("#c-word").fadeIn("5000");
        $("#h-word").fadeIn("5000");
        // }
    });
    $("#popular").mouseleave(function(){
        // 若冷熱門無顯示狀態: 冷門及熱門，淡出 ; 冷熱門，則淡出
        if($("#p-word").css('display') == 'none' ){//$("#p-word").css('display'):判斷冷熱門的狀態
            $("#c-word").fadeOut("5000");
            $("#h-word").fadeOut("5000");
            $("#p-word").fadeIn("5000");
        };
        // });
    });
});



