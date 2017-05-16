$(function(){
    $(".check-visible").change(function(){
        if(!$(this).attr("checked")){
            $(this).parent().next().children(".check-mandatory").removeAttr("checked");
            $(this).parent().parent().parent().parent().removeClass("field-mandatory");
            $(this).parent().parent().parent().parent().removeClass("field-visible");
            $(this).removeAttr("checked")
        } else{
            $(this).parent().parent().parent().parent().addClass("field-visible");
            $(this).attr("checked","checked");
        }
    });

    $(".check-mandatory").change(function(){
        if($(this).attr("checked")){
            $(this).parent().prev().children('.check-visible').attr("checked","checked");
            $(this).parent().parent().parent().parent().addClass("field-mandatory");
            $(this).parent().parent().parent().parent().addClass("field-visible");
            $(this).attr("checked","checked");
        } else{
            $(this).parent().parent().parent().parent().removeClass("field-mandatory");
            $(this).removeAttr("checked")
        }
    });

    $('.check-all-visible').change(function(){
        if($(this).attr("checked"))
        $('.check-visible').attr("checked","checked").trigger('change');
        else
        $('.check-visible').removeAttr("checked").trigger('change');
    });

    $('.check-all-mandatory').change(function(){
        if($(this).attr("checked"))
        $('.check-mandatory').attr("checked","checked").trigger('change');
        else
        $('.check-mandatory').removeAttr("checked").trigger('change');
    });

    $('html').tooltip({
        selector: "a[rel=tooltip], [rel=tooltip]"
    });

    $('.datepicker').datepicker({
        onClose: function(dateText, inst) {
            var id = $(inst).attr('id');
            $("#"+id+"_month").attr("value",new Date($(this).datepicker("getDate")).getMonth() +1);
            $("#"+id+"_day").attr("value",new Date($(this).datepicker("getDate")).getDate());
            $("#"+id+"_year").attr("value",new Date($(this).datepicker("getDate")).getFullYear());
        }
    });
    $('.datetimepicker').datetimepicker({
        onClose: function(dateText, inst) {
            var id = $(inst).attr('id');
            $("#"+id+"_month").attr("value",new Date($(this).datepicker("getDate")).getMonth() +1);
            $("#"+id+"_day").attr("value",new Date($(this).datepicker("getDate")).getDate());
            $("#"+id+"_year").attr("value",new Date($(this).datepicker("getDate")).getFullYear());
            $("#"+id+"_hour").attr("value",new Date($(this).datepicker("getDate")).getHours());
            $("#"+id+"_minute").attr("value",new Date($(this).datepicker("getDate")).getMinutes());
        }
    });

    $("#intro").css("background-position", Math.floor((Math.random() * 100) + 1) + "%" + Math.floor((Math.random() * 100) + 1) + "%");
});

function toggleFields(target){
    $(target).parent().parent().parent().parent().toggleClass("field-mandatory");
}

function validar(form) {
    var erros = '';
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    var email = form.email.value;
    $("input[type=text]").each(function(){
        $(this).parent().parent().removeClass('error');
        if (!$(this).val()) {
            erros += '<li>Campo '+$(this).data('validation-name')+' é requerido</li>';
            $(this).parent().parent().addClass('error');
        }
        else if ($(this).data('validation-name') == 'Email' && reg.test($(this).val()) == false) {
            erros += '<li>Email inválido.</li>';
            $(this).parent().parent().addClass('error');
        }
        else if (($(this).data('validation-name') == 'Dia do Aniversário' || $(this).data('validation-name') == 'Mês do Aniversário') && (isNaN($(this).val()) || isNaN($(this).val()))) {
            erros += '<li>Campo '+$(this).data('validation-name')+' está inválido</li>';
            $(this).parent().parent().addClass('error');
        }
    });
    if (erros != '') {
        $('.alert-error').html("<a class=\"close\" data-dismiss=\"alert\" href=\"#\">×</a><ul>" + erros + "</ul>").show();
        return false;
    }
}

//página do formulário de adição de submissões
var numAutores = 1;
$("#add-author").click(function(e){
    numAutores++;
    var template = "<div class='autor-"+numAutores+"'><div class='control-group'><label for='autor"+numAutores+"-nome' class='control-label'>Nome</label><div class='controls'><input type='text' placeholder='Nome do autor' name='autor.nome' id='autor"+numAutores+"-nome' class='span5' /><a href='#' class='btn btn-danger pull-right remove-author'><i class=\"icon-remove-sign icon-white\"></i> Remover autor</a></div></div><div class='control-group'><label for='autor"+numAutores+"-linkCurriculo' class='control-label'>Link para currículo online</label><div class='controls'><input type='text' name='autor.linkCurriculo' placeholder='Link para LinkedIn ou Lattes' id='autor"+numAutores+"-linkCurriculo' class='span5' /></div></div><div class='control-group'><label for='autor"+numAutores+"-email' class='control-label'>Email</label><div class='controls'><input type='email' name='autor.email' placeholder='autor@email.com' id='autor"+numAutores+"-email' class='span5' /></div></div></div>";
    $("#dados-autores").append(template);

    $('[class^="autor-"]').one("click", ".remove-author", function(e){
        $(this).parent().parent().parent().remove();
        e.preventDefault();
    });
    e.preventDefault();
});

$("#link_submissao").click(function() {
    $('#artigos_submetidos').toggle(200, function() {
        // Animation complete.
    });
});

$("[name='link_expandir']").click(function() {
    $('#lista_' + this.id).toggle(200, function() {
        // Animation complete.
    });
});

$("th[value]").each(function () {
    var value = $(this).attr("value");
    $(this).attr("title", value);
    $(this).removeAttr("value");
});

$("[name='registrarPresenca']").each(function () {
    var obj = $(this);
    var idPresenca = $(this).attr("idPresenca");
    var idHorario = $(this).attr("idHorario");
    var idInscricao = $(this).attr("idInscricao");
    obj.click(function() {
        obj.html("Registrando...");
        $.post("../../presenca/alterarPresenca", {idPresenca: idPresenca, idHorario: idHorario, idInscricao: idInscricao}, function (data) {
            var retorno = jQuery.parseJSON(data);
            console.log(retorno.msg)
            if (retorno.erro != "") {
                alert(retorno.erro);
            } else {
                obj.attr("style", "color: " + retorno.color);
                obj.attr("data-original-title", retorno.usuario);
                if (retorno.msg == "Presente") {
                    obj.html("<input type='checkbox' checked=''> Presente");
                    if (retorno.idPresenca != "") {
                        idPresenca = retorno.idPresenca;
                    }
                }
                else if (retorno.msg == "Ausente") {
                    obj.html("<input type='checkbox'> Ausente");
                } else if(retorno.msg== "Irregular") {
                    obj.html("<input type='checkbox'> Irregular");
                    $('#inscricaoIrregular').modal({
                    });
                } else if (retorno.msg=="Nao registrado"){
                    obj.html("<input type='checkbox'> Não registrado");
                    $('#inscricaoIrregular').modal({
                    });
                }
            }
        });
    });
});

$("[name='statusInscricao']").each(function () {
    var obj = $(this);
    var id = $(this).attr("id_inscricao");
        obj.click(function() {
        obj.html("Registrando...");
        $.post("../../inscricao/mudarStatusInscricao", {id: id}, function (data) {
            var retorno = jQuery.parseJSON(data);
            if (retorno.erro != "") {
                alert(retorno.erro);
            } else {
                obj.attr("style", "color: " + retorno.color);
                console.log(retorno.msg)
                if (retorno.msg == "Ativa") {
                    obj.html("<input type='checkbox' checked=''> Ativa");
                    obj.attr('cancelada','0');
                    $('#homologa_'+id).html("<input type='checkbox'>Homologar").attr("style","color:red");
                } else if (retorno.msg == "Cancelada") {
                    obj.attr('cancelada','1');
                    obj.html("<input type='checkbox'> Cancelada");
                    $('#homologa_'+id).html("Homologar").attr("style","color:red");
                } else if (retorno.msg == "Esgotada"){
                    obj.html("<input type='checkbox'> Cancelada");
                    $('#semvaga').modal({
                    });
                }
            }
        });
    });
});

$("[name='homologarInscricao']").each(function () {
    var obj = $(this);
    var id = $(this).attr("id_inscricao");

    obj.click(function() {
        var status = $("#inscricao_"+id).attr("cancelada");
        if(status==1)
        return;

        obj.html("Registrando...");
        $.post("../../inscricao/mudarStatusHomologarInscricao", {id: id}, function (data) {
            var retorno = $.parseJSON(data);
            if (retorno.erro != "") {
                alert(retorno.erro);
            } else {
                obj.attr("style", "color: " + retorno.color);
                if (retorno.msg == "Homologada") {
                    obj.html("<input type='checkbox' checked=''> Homologada");
                } else if (retorno.msg == "Homologar") {
                    obj.html("<input type='checkbox'>Homologar");
                } else if (retorno.msg == "Esgotada"){
                    obj.html("<input type='checkbox'>Homologar");
                    $('#semvaga').modal({
                    });
                }
            }
        });
    });

});


$("[title]").tooltip();

function abreModal(id, presenca)
{
    $('#modal_horario_id').val(id);
    console.log("presenca: " + presenca)
    if (presenca == "1") {
        $('#modal_presenca').val(presenca);
        console.log("presenca dentro do 1: " + presenca)
    } else if (presenca == "0") {
        $('#modal_ausencia').val(presenca);
        console.log("presenca dentro do 0: " + presenca)
    }
}

function registrarPresenca(){
    var id=$('#modal_horario_id').val();
    var presenca=$('#modal_presenca').val();
    if(presenca !=1){
        presenca = 0
        console.log("presenca depois: " + presenca)
    }

    console.log("presenca depois: " + presenca)
    $.post("../../presenca/registrarPresencaDeInscritos", {id: id, presenca: presenca}, function (data) {
        var retorno = data;
        $('#registrarAusentes').modal('hide');
        $('#registrarPresentes').modal('hide');
        window.location="../show/" + data;
    });
}

$("[name='administrador']").select2({
  tags: true
});

$("#colunas").popover({
    placement: 'bottom',
    html: true,
    title: function () {
        return $(this).find('.popover-title').html();
    },
    content: function() {
        return $(this).find('.popover-content').html();
    }
}).click( function (){
    $('.popover').draggable();
    $("[name='coluna']").each(function (){
        var tipo = $(this).attr('id');
        if($("[name='col"+tipo+"']").attr('show') == '1'){
            $(this).attr('checked','1','show','1');
            $(this).attr('show','1');
        } else {
            $(this).removeAttr('checked','show','0');
            $(this).attr('show','0');
        }
    });
    $("[name='coluna']").click(function (){
        var status = $(this).attr('show');
        var tipo = $(this).attr('id');
        if(status == 1){
            console.log(tipo);
            console.log("#col"+tipo+"");
            $(this).attr('show','0');
            $("[name='col"+tipo+"']").addClass('oculta');
            $("[name='col"+tipo+"']").attr('show','0');
        } else {
            $(this).attr('show','1');
            $("[name='col"+tipo+"']").removeClass('oculta');
            $("[name='col"+tipo+"']").attr('show','1');
        }
    });
});

$("[name='exportar']").click(function (){
    $("#personalizar").modal().each( function (){
        $("[tipo='coluna']").each( function (){
            var nomeCol = $(this).attr('name');
            console.log(nomeCol)
            if($(this).attr('show') == '1'){
                $("#"+nomeCol+"").attr('checked', ' ');
            } else {
                $("#"+nomeCol+"").removeAttr('checked', ' ');
            }
        })
    });
});
