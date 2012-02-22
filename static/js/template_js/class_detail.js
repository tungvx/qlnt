$(document).ready(function() {

    $("#notify").ajaxSuccess(function(event, request, settings, json) {
        if (json.message != null && json.message != '' && json.message != 'OK') {
            $(this).html("<ul>" + json.message + "</ul>");
            $(this).delay(1000).fadeOut(10000);
        }
        else if (json.message == 'OK') {
            $(this).text('Đã lưu');
            $(this).delay(1000).fadeOut('fast');
            //noinspection JSCheckFunctionSignatures
            location.reload('true');
        }

    });

    $(".manualAddStudent").click(function(){
        if ($("#addStudentForm").css('display') == 'none'){
            $("#addStudentForm").fadeIn(300);
            $(".manualAddStudent").text('Thôi thêm');
            $(document).scrollTop(100000000);
        } else {
            $("#addStudentForm").fadeOut(300);
            $(".manualAddStudent").text('Thêm');
        }
    });

    $("#submitform").bind('submit', function() {
        var d = $(this).serialize();
        d = d + '&request_type=add';
        var self = $(this);
        var theLast = self.prev();
        var arg = {data: d,
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success:function(json) {
                if (!json.success) {
                    $("#notify").showNotification(json.message, 3000);
                } else {
                    $.ajaxSetup({
                        global: false
                    });
                    $("#student_placeholder").load("/school/getStudent/" + json.student_id + "/",
                        function() {
                            $.ajaxSetup({
                                global: true
                            });
                            var newStudent = $("#student_placeholder").find("tr");
                            newStudent.insertBefore(self).click(select);
                            var stt = parseInt(theLast.find('td:eq(1)').text());
                            if (stt) newStudent.find('td:eq(1)').text(stt + 1);
                            else newStudent.find('td:eq(1)').text(1);
                            $(".form").find('input:text').val('');
                            $(".form").find('input#id_dan_toc').val('Kinh');
                            $("#notify").showNotification(json.message);

                        })

                }
            }
        };
        $.ajax(arg);
        return false;
    });

    $("#import").click(function() {
        $("#fileupload").dialog('open');
    });

    $("#id_sms_phone").keydown(function (event) {
        if ((event.keyCode >= 48 && event.keyCode <= 57) || (event.keyCode >= 96 && event.keyCode <= 105)) // 0-9 or numpad 0-9
        {
// check textbox value now and tab over if necessary
        }
        else if (event.keyCode != 8 && event.keyCode != 9 && event.keyCode != 46 && event.keyCode != 37 && event.keyCode != 39) // not esc, del, left or right
        {
            event.preventDefault();
        }
// else the key should be handled normally
    });

    $("#fileupload").dialog({
        modal : true,
        buttons: {
            Đóng: function() {
                //noinspection JSCheckFunctionSignatures
                location.reload('true');
                $(this).dialog('close');
            }
        },
        autoOpen: false,
        width: 700,
        height: 400,
        maxWidth: 700,
        maxHeight: 400,
        title: "Nhập học sinh từ file Excel"
    });

    var select = function() {
        var numberOfSelected;
        if ($(this).hasClass('student')) {
            var id = $(this).attr('class').split(' ')[0];
            var checkBoxId = '#checkbox_' + id;
            var checkBoxAll = '#checkbox_all';
            var n = 0;
            if ($(this).hasClass('selected')) {
                $(this).removeClass('selected');
                $(checkBoxId).prop("checked", false);
                n = $("input.studentCheckbox:checked").length;
                if (n == 1 || n == 0) {
                    $(checkBoxAll).prop("checked", false);
                }
                numberOfSelected = $("tr.selected").length;
                if (numberOfSelected == 0) {
                    $("#showChosenStudent").html("Chưa chọn học sinh nào");
                    $("#send").attr('disabled', 'disabled');
                } else {
                    $("#showChosenStudent").html((numberOfSelected).toString() + " học sinh");
                }
            } else {
                $(this).addClass('selected');
                $(checkBoxId).prop("checked", true);
                $(checkBoxAll).prop("checked", true);
                numberOfSelected = $("tr.selected").length;
                $("#showChosenStudent").html((numberOfSelected).toString() + " học sinh");
                $("#send").removeAttr('disabled');
            }
        }
    };
    var delSelected = function() {
        if (!$("#checkbox_all").is(':checked')) {
            alert("Hãy chọn ít nhất một học sinh để xoá.");
            return false;
        }
        var answer = confirm('Bạn có muốn xóa những học sinh đã chọn không?');
        if (!answer) return false;
        var data = '';
        $(".selected").each(function() {
            data = data + $(this).attr('class').split(' ')[0] + '-';
        });
        $("#notify").text("Đang xóa...");
        $("#notify").show();
        var arg = { type:"POST",
            url:"",
            global: false,
            data: {data:data, request_type:'del'},
            datatype:"json",
            success: function() {
                $("#notify").showNotification("Đã xóa xong");
                //noinspection JSCheckFunctionSignatures
                location.reload('true');
            }
        };
        $.ajax(arg);
        return false;
    };
    $("#delSelected").click(delSelected);

    // individual listener
    $("tr").each(function() {
        $(this).click(select);
    });

    var selectAllStudent = function(){
        $("tr").each(function() {
            if (!$(this).hasClass('selected'))
                $(this).trigger('click');
        });
    };
    var deselectAllStudent = function(){
        $("tr").each(function() {
            if ($(this).hasClass('selected'))
                $(this).trigger('click');
        });
    };

    $("#checkbox_all").click(function() {
        if ($("#checkbox_all").is(':checked'))
            selectAllStudent();
        else deselectAllStudent();

    });

    $("#textSms").click(function() {
        // setting up layout
        if ($("#smsWindow").css('display') == 'none') {
            var buttonOffsetTop = $(this).offset().top;
            var contentWidth = parseInt($("#content").css('width'));
            var smsWindow = $("#smsWindow");
            var smsWindowWidth = parseInt(smsWindow.css('width'));
            smsWindow.css('position', 'absolute');
            smsWindow.css('top', buttonOffsetTop + 30);
            smsWindow.css('left', contentWidth - smsWindowWidth );
            smsWindow.slideDown(400);
        } else {
            $("#smsWindow").slideUp(400);
            deselectAllStudent();
        }
    });
    $("#smsClose").click(function() {
        $("#smsWindow").fadeOut(400);
        deselectAllStudent();
    });
    $("#send").click(function() {
        var content = $("#smsContent").val();
        var studentList = "";
        $("tr.selected").each(function() {
            studentList += $(this).attr('class').split(" ")[0] + "-";
        });
        if (content.replace(/ /g, '') == '') {
            $("#notify").showNotification("Nội dung còn trống");
        } else {
            //noinspection JSUnusedGlobalSymbols
            var arg = { type:"POST",
                url:"",
                global: false,
                data: { content:content,
                    request_type:'send_sms',
                    include_name: $("#includeStudentName").is(':checked'),
                    student_list:studentList},
                datatype:"json",
                success: function(json) {
                    $("#notify").showNotification("Đã gửi " + json.number_of_sent + " tin nhắn");
                    $("#smsProgressbar").hide();
                    if (json.number_of_blank != '0' || json.number_of_failed != '0') {
                        var html = "<ul>";
                        if (parseInt(json.number_of_blank) > 0)
                            html += "<li>" + json.number_of_blank + " học sinh không có số điện thoại.</li>";
                        if (parseInt(json.number_of_failed) > 0)
                            html += "<li>" + json.number_of_failed + " học sinh không gửi được tin nhắn</li>";
                        html += "</ul>";
                        $("#smsErrorDetail").css('width', $("#smsContent").css('width'));
                        $("#smsErrorDetail").html(html).show();
                    }
                },
                error: function() {
                    $("#notify").showNotification("Gặp lỗi khi gửi tin nhắn");
                    $("#smsProgressbar").hide();
                }
            };
            $("#smsProgressbar").css('width', $("#smsContent").css('width'));
            $("#smsProgressbar").show();
            $.ajax(arg);
        }

        return false;
    });

    // setup layout
    $("#addStudentForm").find("input").each(function() {
        var td = $(this).parent("td");
        $(this).css('width', parseInt(td.css('width')) - td.css('padding'));
    });

//    $('table.main-table').css('width', parseInt($('table.main-table').css('width')));

    $('td').each(function(){
        if ($(this).css('display') != 'none'){
            $(this).css('width', parseInt($(this).css('width')));
        }
    });

    $("#addStudentForm").hide();
    // end setting up

    // key function
    $(document).keydown(function(e){
        if (e.which == 27 && $("#smsWindow").css('display') != 'none'){
            // press esc to close sms window
            $("#smsWindow").fadeOut(400);
            deselectAllStudent();
        }
    });
    // recover state when browser uses it's cache
    $('input:checked').each(function(){
        var trParent = $(this).parents('tr');
        if (!trParent.hasClass('thread')) trParent.trigger('click');
    });


});
