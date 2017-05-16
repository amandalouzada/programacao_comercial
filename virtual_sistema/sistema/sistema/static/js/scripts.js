
$(document).ready(function(){

  $('.button-collapse').sideNav();
  $('.collapsible').collapsible();
  $('.parallax').parallax();
  $('select').material_select();


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


})
