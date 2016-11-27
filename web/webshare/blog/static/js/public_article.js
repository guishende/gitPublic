$(document).ready(function() {
    // 控制下拉导航的出现关闭
    var $navToggle = $('#mobile img');
    var $navList = $('#mobile li ul');
    var $navListData = $('#mobile li ul li');
    $navToggle.click(function() {
        $navList.animate({ height: 'toggle', opacity: 'toggle' }, 600);
    });
    $navListData.filter(':not(.search)').click(function() {
        $navList.animate({ height: 'hide', opacity: 'hide' }, 600);
    });

    //下拉的时候改变下拉导航的定位模式,并给其加上阴影
    var $navPc = $('nav');
    var $win = $(window);
    var $document = $(document);
    var $wrapper = $('#wrapper');
    $win.scroll(function() {
        if ($document.scrollTop() >= 1) {
            $navPc.addClass('shadow');
        } else {
            $navPc.removeClass('shadow');
        }
    });

    //控制添加文章表单的弹出与关闭
    var $popup = $('div#popup');
    var $addForm = $('div#addForm');
    var $addFormToggle = $('.close');
    var $write = $('.write');
    $addFormToggle.click(function() {
        $popup.fadeOut();
        $addForm.fadeOut();
    });
    $write.click(function() {
        $popup.fadeIn();
        $addForm.fadeIn();
    });

    //添加表单的验证
    var $title = $('#title');
    var $tag = $('#tag');
    var $content = $("#addForm form textarea");
    $('#addForm form').submit(function() {
        if ($title.val() == '' || $title.val().length > 20) {
            $title.focus();
            showInform('标题不能为空且不能超过20个字符,请重新输入标题');
            return false;
        }
        if ($tag.val() == '' || $tag.val().length > 20) {
            $tag.focus();
            showInform('标签不能为空且不能超过20个字符,请重新输入标签');
            return false;
        }
        if ($content.val() == '') {
            $content.focus();
            showInform('内容不能为空,请输入内容');
            return false;
        }
    });

    //控制联系站长表单的弹出与关闭
    var $contractForm = $('div#contractForm');
    var $contractToggle = $('.turnOff');
    var $contractMe = $('.contractMe');
    $contractToggle.click(function() {
        $popup.fadeOut();
        $contractForm.fadeOut();
    });
    $contractMe.click(function() {
        $popup.fadeIn();
        $contractForm.fadeIn();
    });

    //切换文章详情的可编辑性
    var $edit = $('#edit');
    var $delete = $('#delete');
    var $cancel = $('#cancel');
    var $save = $('#save');
    var $textarea = $('#articleDetail textarea');
    $edit.click(function(){
    	$(this).hide();
    	$delete.hide();
    	$cancel.fadeIn();
    	$save.fadeIn();
    	$textarea.removeAttr('readonly').focus().css('border', '1px solid gray');
    });
    $cancel.click(function(){
    	$(this).hide();
    	$save.hide();
    	$edit.fadeIn();
    	$delete.fadeIn();
    	$textarea.attr('readonly', 'readonly').css('border', 'none');
    });

    //textarea的高度自适应
    var srcollHeight = $textarea[0].scrollHeight;
    $textarea.css('height', srcollHeight);

    //确认删除框的弹出
    $('button#delete a').click(function() {
        var r = confirm('确定要删除该文章？')
        if (r == true) {
            return true;
        } else {
            return false;
        }});
	
	});
	
//提示框的出现消失
var $inform = $('#inform');
function showInform(src) {
    $inform.slideDown('slow').text(src);
    setTimeout(hideInformByAuto, 3000);
}
var hideInformByAuto = function () {
    $inform.slideUp('slow');
};
$inform.click(function () {
    $(this).slideUp('slow');
});
