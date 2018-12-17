$('.likephoto').each(function() {

    if($(this).data('liked') == true) {
        $(this).css('color', '')
        $('i', this).attr('class','')
    } else {
        $(this).css('color', '')
        $('i',this).attr('class', '')
    }
    $(this).off('click')
    $(this).click(function() {
        var but = $(this)
        var buti = $('i',this)
        $.ajax({
            type: "GET",
            url: "ajax-like-photo?id="+$(this).data('postid'),
            processData: false,
            contentType: "applicatio/json",
            data: '',
            success: function(r) {
                if(JSON.parse(r).Status == 'Success'){

                    if(but.data('liked') == false){
                        but.data('liked',true)
                        but.css('color','')
                        buti.attr('class','')
                    }
                    else {
                        but,data('liked',false)
                        but.css('color','')
                        buti.attr('class', '')
                    }
                }
            }
        })
    }




    }



}