function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
function read_values(response){
    document.getElementById("results_chart").innerHTML=''
    input_x=[]
    input_y=[]
    outputs_x=[]
    outputs_y=[]
    for (data of response){
        if (data['fields'].hasOwnProperty('نام_خیر')){
            input_x.push(data['fields']['تاریخ'])
            input_y.push(data['fields']['مبلغ'])
        }
        else{
            outputs_x.push(data['fields']['تاریخ'])
            outputs_y.push(-data['fields']['مبلغ'])
        }
    }
    data=input_y.concat(outputs_y)
    const colours = data.map((value) => parseInt(value) <= 0 ? 'red' : 'green');
    new Chart("results_chart", {
      type: "bar",
      data: { 
        labels: input_x.concat(outputs_x),
        datasets: [{
          backgroundColor: colours,
          data: input_y.concat(outputs_y)
        }]
      },
      options: {
          scales: {
          xAxes: [{
              barPercentage: 3
          }]
        }
        ,
        legend: {display: false},
        title: {
          display: true,
          text: "Report of the project and time span"
        }
      }
    });

}
$(document).ready(function() {
    // catch the form's submit event
    $('#filter-form').submit(function() {
        // create an AJAX call
        
        $.ajax({
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: "/login/fancy_report",
            // on success
            success: function(response) {
            
                console.log(response)
                read_values(response)
     
              },
            error: function(response) {
                // alert the error if any error occured
                console.log('pooria error')

            }
        });

        return false;
    });
})