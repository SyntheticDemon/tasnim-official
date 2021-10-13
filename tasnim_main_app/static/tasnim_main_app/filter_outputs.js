function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
function make_table(response){

    table_body =document.getElementById("tbody")
    table=document.getElementById("results-table")
    for (result of response){
      const new_row=document.createElement("tr")
      const project_name=document.createElement("td")
      const des_card=document.createElement("td")
      const date =document.createElement("td")
      const quantity=document.createElement("td")
      const operation_element=document.createElement("td")
      const remove_element=document.createElement("a",id="remove-link")
      remove_element.href="/login/Outputs/delete/" + result['pk']
      const edit_element=document.createElement("a",id="update-link" )
      edit_element.href="/login/Outputs/edit/" + result['pk']
      remove_element.innerHTML='<i class="fa fa-trash" style="color: red;" ></i> <br>'
      edit_element.innerHTML='<i class="fa fa-edit" style="color: blue; transform: rotate(45);" ></i>'
      operation_element.appendChild(remove_element)
      operation_element.appendChild(edit_element)
      project_name.innerHTML=result['fields']['related_project']
      date.innerHTML=result['fields']['تاریخ']
      quantity.innerHTML=numberWithCommas( result['fields']['مبلغ'])
      des_card.innerHTML=result['fields']['حساب_مقصد']
      new_row.appendChild(project_name)
      new_row.appendChild(quantity)
      new_row.appendChild(des_card)
      new_row.appendChild(date)
      new_row.appendChild(operation_element)
      table_body.appendChild(new_row)
      
    }
}
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
                make_table(response)
         
              },
            error: function(response) {
                // alert the error if any error occured
                console.log('pooria error')

            }
        });

        return false;
    });
})