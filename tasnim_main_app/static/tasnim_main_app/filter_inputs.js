function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
function make_table(response){
    table_body =document.getElementById("tbody")
    table=document.getElementById("results-table")
    for (result of response){
      const new_row=document.createElement("tr")
      const donor_name=document.createElement("td")
      const new_card_num=document.createElement("td")
      const date =document.createElement("td")
      const quantity=document.createElement("td")
      const operation_element=document.createElement("td")
      const remove_element=document.createElement("a",id="remove-link", href="/login/Inputs/delete/"+result['fields']['pk'])
      const edit_element=document.createElement("a",id="update-link", href="/login/Inputs/update/"+result['fields']['pk'] )
      remove_element.innerHTML='<i class="fa fa-remove" style="color: red;" ></i>'
      edit_element.innerHTML='<i class="fa fa-remove" style="color: red;" ></i>'
      operation_element.appendChild(remove_element)
      operation_element.appendChild(edit_element)

      donor_name.innerHTML=result['fields']['نام_خیر']
      date.innerHTML=result['fields']['تاریخ']
      quantity.innerHTML=numberWithCommas( result['fields']['مبلغ'])
      new_card_num.innerHTML=result['fields']['حساب_خیر']
      new_row.appendChild(donor_name)
      new_row.appendChild(quantity)
      new_row.appendChild(new_card_num)
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
            url: "/login/Inputs/get_report",
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