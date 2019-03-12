$(function () {

    //全局的checkbox选中和未选中的样式
    var $allCheckbox = $('input[type="checkbox"]'),     //全局的全部checkbox
        $wholeChexbox = $('.whole_check'),
        $cartBox = $('.cartBox'),                       //每个商铺盒子
        $shopCheckbox = $('.shopChoice'),               //每个商铺的checkbox
        $sonCheckBox = $('.son_check');                 //每个商铺下的商品的checkbox
    $allCheckbox.click(function () {
        if ($(this).is(':checked')) {
            $(this).next('label').addClass('mark');
        } else {
            $(this).next('label').removeClass('mark')
        }
    });

    //===============================================全局全选与单个商品的关系================================
    $wholeChexbox.click(function () {
        var $checkboxs = $cartBox.find('input[type="checkbox"]');
        if ($(this).is(':checked')) {
            $checkboxs.prop("checked", true);
            $checkboxs.next('label').addClass('mark');
        } else {
            $checkboxs.prop("checked", false);
            $checkboxs.next('label').removeClass('mark');
        }
        totalMoney();
    });


    $sonCheckBox.each(function () {
        $(this).click(function () {
            if ($(this).is(':checked')) {
                //判断：所有单个商品是否勾选
                var len = $sonCheckBox.length;
                var num = 0;
                $sonCheckBox.each(function () {
                    if ($(this).is(':checked')) {
                        num++;
                    }
                });
                if (num == len) {
                    $wholeChexbox.prop("checked", true);
                    $wholeChexbox.next('label').addClass('mark');
                }
            } else {
                //单个商品取消勾选，全局全选取消勾选
                $wholeChexbox.prop("checked", false);
                $wholeChexbox.next('label').removeClass('mark');
            }
        })
    });

    //=======================================每个店铺checkbox与全选checkbox的关系/每个店铺与其下商品样式的变化===================================================

    //店铺有一个未选中，全局全选按钮取消对勾，若店铺全选中，则全局全选按钮打对勾。
    $shopCheckbox.each(function () {
        $(this).click(function () {
            if ($(this).is(':checked')) {
                //判断：店铺全选中，则全局全选按钮打对勾。
                var len = $shopCheckbox.length;
                var num = 0;
                $shopCheckbox.each(function () {
                    if ($(this).is(':checked')) {
                        num++;
                    }
                });
                if (num == len) {
                    $wholeChexbox.prop("checked", true);
                    $wholeChexbox.next('label').addClass('mark');
                }

                //店铺下的checkbox选中状态
                $(this).parents('.cartBox').find('.son_check').prop("checked", true);
                $(this).parents('.cartBox').find('.son_check').next('label').addClass('mark');
            } else {
                //否则，全局全选按钮取消对勾
                $wholeChexbox.prop("checked", false);
                $wholeChexbox.next('label').removeClass('mark');

                //店铺下的checkbox选中状态
                $(this).parents('.cartBox').find('.son_check').prop("checked", false);
                $(this).parents('.cartBox').find('.son_check').next('label').removeClass('mark');
            }
            totalMoney();
        });
    });


    //========================================每个店铺checkbox与其下商品的checkbox的关系======================================================

    //店铺$sonChecks有一个未选中，店铺全选按钮取消选中，若全都选中，则全选打对勾
    $cartBox.each(function () {
        var $this = $(this);
        var $sonChecks = $this.find('.son_check');
        $sonChecks.each(function () {
            $(this).click(function () {
                if ($(this).is(':checked')) {
                    //判断：如果所有的$sonChecks都选中则店铺全选打对勾！
                    var len = $sonChecks.length;
                    var num = 0;
                    $sonChecks.each(function () {
                        if ($(this).is(':checked')) {
                            num++;
                        }
                    });
                    if (num == len) {
                        $(this).parents('.cartBox').find('.shopChoice').prop("checked", true);
                        $(this).parents('.cartBox').find('.shopChoice').next('label').addClass('mark');
                    }

                } else {
                    //否则，店铺全选取消
                    $(this).parents('.cartBox').find('.shopChoice').prop("checked", false);
                    $(this).parents('.cartBox').find('.shopChoice').next('label').removeClass('mark');
                }
                totalMoney();
            });
        });
    });
    //====================================================================================================


    //=================================================商品数量==============================================
    var $plus = $('.plus'),
        $reduce = $('.reduce'),
        $all_sum = $('.sum');
    let update_url = '/car/update/';
    $plus.click(function () {
        var $inputVal = $(this).prev('input'),
            // $count = parseInt($inputVal.val()) + 1,
            $obj = $(this).parents('.amount_box').find('.reduce'),
            $priceTotalObj = $(this).parents('.order_lists').find('.sum_price'),
            $price = $(this).parents('.order_lists').find('.price').html();  //单价

        // $inputVal.val($count);
        let value = parseInt($inputVal.val()) < parseInt($inputVal.attr('max'))
            ? parseInt($inputVal.val()) + 1 : parseInt($inputVal.attr('max'));
        if (parseInt($inputVal.val()) < parseInt($inputVal.attr('max'))) {
            $.post(update_url, {ac: '1', car_id: $(this).attr('car_id')}, function (result) {
                if (result.status === 200) {
                    $('#gouwucar').text(result.car_count + ' ');
                    $inputVal.val(value)
                }
            })
        }
        var $priceTotal = value * parseInt($price.substring(1));
        $priceTotalObj.html('￥' + $priceTotal);
        if ($inputVal.val() > 1 && $obj.hasClass('reSty')) {
            $obj.removeClass('reSty');
        }

        totalMoney();
    });

    $reduce.click(function () {
        var $inputVal = $(this).next('input'),
            // $count = parseInt($inputVal.val()) - 1,
            $priceTotalObj = $(this).parents('.order_lists').find('.sum_price'),
            $price = $(this).parents('.order_lists').find('.price').html();  //单价

        let value = $inputVal.val() > 1
            ? $inputVal.val() - 1 : 1;
        $.post(update_url, {ac: '2 ', car_id: $(this).attr('car_id')}, function (result) {
            if (result.status === 200) {
                $('#gouwucar').text(result.car_count + ' ');
                $inputVal.val(value)
            }
        });
        var $priceTotal = value * parseInt($price.substring(1));
        if ($inputVal.val() > 1) {
            $inputVal.val(value);
            $priceTotalObj.html('￥' + $priceTotal);
        }
        if ($inputVal.val() == 1 && !$(this).hasClass('reSty')) {
            $(this).addClass('reSty');
        }
        totalMoney();
    });

    $all_sum.keyup(function () {
        var $count = 0,
            $priceTotalObj = $(this).parents('.order_lists').find('.sum_price'),
            $price = $(this).parents('.order_lists').find('.price').html(),  //单价
            $priceTotal = 0;
        if ($(this).val() == '') {
            $(this).val('1');
        }
        $(this).val($(this).val().replace(/\D|^0/g, ''));
        $count = $(this).val();
        $priceTotal = $count * parseInt($price.substring(1));
        $(this).attr('value', $count);
        $priceTotalObj.html('￥' + $priceTotal);
        totalMoney();
    });

    //======================================移除商品========================================
    let delete_url = '/car/delete/';

    var car_id;
    var $order_lists = null;
    var $order_content = '';
    $('.delBtn').click(function () {
        $order_lists = $(this).parents('.order_lists');
        $order_content = $order_lists.parents('.order_content');
        car_id = $(this).attr('id');
        $('.model_bg').fadeIn(300);
        $('.my_model').fadeIn(300);
    });

    //关闭模态框
    $('.closeModel').click(function () {
        closeM();
    });
    $('.dialog-close').click(function () {
        closeM();
    });

    function closeM() {
        $('.model_bg').fadeOut(300);
        $('.my_model').fadeOut(300);
    }

    //确定按钮，移除商品
    $('.dialog-sure').click(function () {
        // $order_lists.remove();
        if (car_id) {
            $.post(delete_url, {car_id: car_id}, function (result) {
                //    当数据库删除了数据  删除该条数据
                if (result.status === 200) {
                    //  第一种通过父容器删除子元素
                    // 自身删除
                    // $btn.parents('tr').remove();
                    $order_lists.remove();
                    $('#gouwucar').text(result.car_count + ' ')
                }
                if ($order_content.html().trim() == null || $order_content.html().trim().length == 0) {
                    $order_content.parents('.cartBox').remove();
                }
                closeM();
                $sonCheckBox = $('.son_check');
                totalMoney();
            });
        }
    });

    //======================================总计==========================================
    var confirm_money = 0;
    let confirm_url = '/order/confirm/';

    function totalMoney() {
        var total_money = 0;
        var total_count = 0;
        var calBtn = $('.calBtn a');
        $sonCheckBox.each(function () {
            if ($(this).is(':checked')) {
                var goods = parseInt($(this).parents('.order_lists').find('.sum_price').html().substring(1));
                var num = parseInt($(this).parents('.order_lists').find('.sum').val());
                total_money += goods;
                total_count += num;
            }
        });
        $('.total_text').html('￥' + total_money);
        $('.piece_num').html(total_count);

        // console.log(total_money,total_count);

        if (total_money != 0 && total_count != 0) {
            if (!calBtn.hasClass('btn_sty')) {
                calBtn.addClass('btn_sty');
            }
        } else {
            if (calBtn.hasClass('btn_sty')) {
                calBtn.removeClass('btn_sty');
            }
        }
        confirm_money = total_money;
        //==========================提交订单=======================================================
        // $('.calBtn').click(function () {
        //     $('#car_form').submit()
        // })
        $('.calBtn').click(function () {
            var car_ids = [];
            var numbers = [];
            var book_ids = [];
            var moneys = [];
            $sonCheckBox.each(function (index, ele) {
                if ($(ele).is(':checked')) {
                    car_ids.push($(ele).attr('car_id'));
                    numbers.push($(ele).attr('number'));
                    book_ids.push($(ele).attr('book_id'));
                    moneys.push($(ele).attr('book_id'));

                }
            });
            var Str=newArray.join("-")
            var data = {
                money: confirm_money,
                car_ids: car_ids,
                number: number,
                book_id: book_id,
            };
            $.ajax({
                url: confirm_url,
                type: 'post',
                data: data,
                traditional: true,
                success: function () {
                    // window.location.href="order/confirm/";
                    alert('订单创建成功');
                    $(ele).remove();
                }
            });

        })
    }


});