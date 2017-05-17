
$(document).ready(function(){

  $('.button-collapse').sideNav();
  $('.collapsible').collapsible();
  $('.parallax').parallax();
  $('select').material_select();
  $('ul.tabs').tabs();

  $('.datepicker').pickadate({
    monthsFull: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agost', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    weekdaysFull: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado'],
    weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
    weekdaysLetter: [ 'D', 'S', 'T', 'Q', 'Q', 'S', 'S' ],

    // Today and clear

    selectMonths: true,
    selectYears: 15,
    today: 'Hoje',
    format: 'dd/mm/yyyy',
    clear: 'Limpar',
    close: 'Fechar'
  });



  $("#test").submit(function(event){
    event.preventDefault();
    $.ajax({
      type:"POST",
      url:"/edit_favorites/",
      data: {
        'video': $('#test').val() // from form
      },
      success: function(){
        $('#message').html("<h2>Contact Form Submitted!</h2>")
      }
    });
    return false;
  });



  $('#btn').click(function(){
    event.preventDefault();
    $.ajax({
      headers: { "X-CSRFToken": $.cookie("csrftoken") },
      type:"POST",
      url:"/inscricao/credenciamento/"+$('#pk').val(),
      data: {
        'numero': $('#inscricao').val() // from form
      },
      success: function(response) {
        $('#inscricao').val('');
        Materialize.toast(response.msg, 4000);

        // return response; // <- I tried that one as well
      }
    });
    return false;

  });


})
