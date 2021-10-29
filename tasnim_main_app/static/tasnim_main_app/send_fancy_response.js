function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
function read_values(response) {
  var input_x = []
  var input_y = []
  var outputs_x = []
  var outputs_y = []
  var input_sum = 0
  var output_sum = 0
 
  for (data of response) {
    if (data['fields'].hasOwnProperty('نام_خیر')) {
      input_x.push(data['fields']['تاریخ'])
      input_y.push(data['fields']['مبلغ'])
      input_sum += parseInt(data['fields']['مبلغ'])
    }
    else {
      outputs_x.push(data['fields']['تاریخ'])
      outputs_y.push(-data['fields']['مبلغ'])
      output_sum += parseInt(data['fields']['مبلغ'])

    }
  }

  document.getElementById("outputs_sum").innerHTML = numberWithCommas( input_sum)
  document.getElementById("inputs_sum").innerHTML = numberWithCommas(output_sum)
  try {
    document.getElementById("background-image-2").remove()
  
  }
  catch {
   console.log("pooria")
  }
  data = input_y.concat(outputs_y)
  const colours = data.map((value) => parseInt(value) <= 0 ? 'red' : 'green');
 
  var my_chart =new Chart("results_chart", {
    type: "bar",
    scales:{
            x:{
              ticks:{
                font:{
                  size:30
                }
              }
            }
    },
    data: {
      labels: input_x.concat(outputs_x),
      datasets: [{
        backgroundColor: colours,
        data: input_y.concat(outputs_y)
      }]
    },
    options: {
       tooltips: {
      callbacks: {
        title: function(tooltipItem, data) {
          return data['labels'][tooltipItem[0]['index']];
        },
        label: function(tooltipItem, data) {
          return data['datasets'][0]['data'][tooltipItem['index']];
        },
      
      },
      backgroundColor: '#FFF',
      titleFontSize: 16,
      titleFontColor: '#0066ff',
      bodyFontColor: '#000',
      bodyFontSize: 14,
      displayColors: false
    },
      responsive: true,
      maintainAspectRatio: false,
      legend: {
        display: false,
        
      },
      title: {
        display: true,
        text: "Report of the project and time span"
      }
    }
  });

}
$(document).ready(function () {
  // catch the form's submit event
  // create an AJAX call

  $.ajax({
    data: {
      "project_name": "",
      "start_date": "",
      "end_date": ""
    }, // get the form data
    type: $(this).attr('method'), // GET or POST
    url: "/login/fancy_report",
    // on success
    success: function (response) {

      console.log(response)
      read_values(response)

    },
    error: function (response) {
      // alert the error if any error occured
      console.log('pooria error')

    }
  });

  return false;
})
$(document).ready(function () {
  // catch the form's submit event
  $('#filter-form').submit(function () {
    // create an AJAX call

    $.ajax({
      data: $(this).serialize(), // get the form data
      type: $(this).attr('method'), // GET or POST
      url: "/login/fancy_report",
      // on success
      success: function (response) {

        console.log(response)
        read_values(response)

      },
      error: function (response) {
        // alert the error if any error occured
        console.log('pooria error')

      }
    });

    return false;
  });
})