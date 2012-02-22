/**
 * Created by PyCharm.
 * User: leeyun
 * Date: 2/11/12
 * Time: 10:58 PM
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function() {
    function findClass(sub){
            if (sub == "Toán") return ("toan");
            else if (sub == "Vật lí")return("li");
            else if (sub == "Hóa học")return("hoa");
            else if (sub == "Sinh học")return("sinh");
            else if (sub == "Tin học")return("tinhoc");
            else if (sub == "Ngữ văn")return("van");
            else if (sub == "Lịch sử")return("su");
            else if (sub == "Địa lí")return("dia");
            else if (sub == "Ngoại ngữ")return("ngoaingu");
            else if (sub == "NN2")return("ngoaingu2");
            else if (sub == "GDCD")return("gdcd");
            else if (sub == "Công nghệ")return("congnghe");
            else if (sub == "Thể dục")return("theduc");
            else if (sub == "GDQP-AN")return("gdqp");
            else if ((sub != "None") && (sub) && (sub != "---------"))return("other");
        }
    $("#import").click(function() {
        $("#fileupload").dialog('open');
    });

    $("#fileupload").dialog({
        modal : true,
        buttons: {
            Đóng: function() {
                location.reload('true');
                $(this).dialog('close');
            }
        },
        autoOpen: false,
        width: 700,
        height: 400,
        maxWidth: 700,
        maxHeight: 400,
        title: "Nhập TKB toàn trường từ file Excel"
    });

    $("#changeTeacher").click(function() {
        if ($(this).hasClass('checked')) {
            $(this).removeClass('checked');
            $(this).html('Hiện giáo viên dạy');
            $(".teacher").each(function() {
                $(this).hide();
            })
        } else {
            $(this).addClass('checked');
            $(this).html('Ẩn giáo viên dạy');
            $(".teacher").each(function() {
                $(this).show();
            })
        }
    });

    $("td").each(function() {
        var sub = $(this).children("p:first").text();
        $(this).addClass(findClass(sub));
    });
});