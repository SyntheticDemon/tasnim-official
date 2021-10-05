$(document).ready(function() {


        
    // catch the form's submit event
    $('#filter-form').submit(function() {
        // create an AJAX call
        document.getElementById("tbody").innerHTML=""
     
        $.ajax({
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: "/login/Outputs/get_report",
            // on success
            success: function(response) {
            
                console.log(response)
                
                table_body =document.getElementById("tbody")
                table=document.getElementById("results-table")
                for (result of response){
                  const new_row=document.createElement("tr")
                  const project_name=document.createElement("td")
                  const des_card=document.createElement("td")
                  const date =document.createElement("td")
                  const quantity=document.createElement("td")
                  project_name.innerHTML=result['fields']['related_project']
                  date.innerHTML=result['fields']['تاریخ']
                  quantity.innerHTML=result['fields']['مبلغ']
                  des_card.innerHTML=result['fields']['حساب_مقصد']
                  new_row.appendChild(project_name)
                  new_row.appendChild(quantity)
                  new_row.appendChild(des_card)
                  new_row.appendChild(date)
                  table_body.appendChild(new_row)
                  
                }
              },
            error: function(response) {
                // alert the error if any error occured
                console.log('pooria error')

            }
        });

        return false;
    });
})