$('document').ready(function(){
  $(".sidebar-collapse").sideNav();
  $('select').material_select();
  $('.datepicker').pickadate({
  selectMonths: true, // Creates a dropdown to control month
  selectYears: 100, // Creates a dropdown of 100 years to control year
  labelMonthNext: 'Próximo month',
  labelMonthPrev: 'Anterior month',

  // The title label to use for the dropdown selectors
  labelMonthSelect: 'Selecionar um mês',
  labelYearSelect: 'Selecionar um ano',

  // Months and weekdays
  monthsFull: [ 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro' ],
  monthsShort: [ 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez' ],
  weekdaysFull: [ 'Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado' ],
  weekdaysShort: [ 'Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab' ],

  // Materialize modified
  weekdaysLetter: [ 'D', 'S', 'T', 'Q', 'Q', 'S', 'S' ],
  format: 'dd/mm/yyyy',

  // Today and clear
  today: 'Hoje',
  clear: 'Limpar',
  close: 'Fechar',
  });
});
// The title label to use for the month nav buttons
