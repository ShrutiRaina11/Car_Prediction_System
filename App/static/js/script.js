function load_car_models(company_id,car_model_id){
  var brand = document.getElementById(company_id);
  var car_model = document.getElementById(car_model_id);

  car_model.value = "";
  car_model.innerHTML = "";

  for(let company of companies){
      if(brand.value == company){
          for(let model of car_models){
              if(model.includes(company)){
                var newOption = document.createElement("option");
                newOption.value = model;
                newOption.innerHTML = model;
                car_model.options.add(newOption)
              }
          }
      }
  }
}
function form_handler(event){
    event.preventDefault();
}
function handleClick(){
    var Modelform = document.querySelector('form')
    Modelform.addEventListener("submit", form_handler)

    var form_data =  new FormData(Modelform)

    var xhr = new XMLHttpRequest()

    xhr.open('POST', '/predict',true)

    var prediction = document.getElementById('prediction')

    prediction.innerHTML = "Wait! Predicting Price......."

    xhr.onreadystatechange = function(){
        if(xhr.readyState == XMLHttpRequest.DONE){
            prediction.innerHTML="Prediction: ₹"+xhr.responseText;
            console.log(xhr.responseText)
        }
    }
    xhr.onload= function(){}
    xhr.send(form_data)
}
