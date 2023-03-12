var counter = 4;


document.getElementById('DaVotJeBlyatKnopka').onclick =
    function(){
    counter += 1;
    let name = "word" + counter;
    let description = "description" + counter;
    let butoon = document.querySelector('#IphoneCHikiCHikiBlyat');
    butoon.insertAdjacentHTML("afterend", "" +
        "<div class=\"container FormPadding\" id=" + "form" + counter + ">\n" +
"            <div class=\"mx-5\">\n" +
"                <label for=" +  name + " class=\"form-label\">Введите слово</label>\n" +
"                <input type=\"text\" pattern=\"[A-zА-я]{2,33}\" required=\"\" class=\"form-control\" id=" + name + " name=" + name + " placeholder=\"Яблоко\" minlength=\"2\" maxlength=\"33\">\n" +
"            </div>\n" +
"            <div class=\"mx-5\">\n" +
"              <label for=\"description1\" class=\"form-label\">Описание слова</label>\n" +
"              <textarea class=\"form-control\" id=\"description1\" name=\"description1\" rows=\"3\" minlength=\"2\" maxlength=\"200\" placeholder=\"Введите описание слова\"></textarea>\n" +
"            </div>\n" +
"        </div>")
    return true;};

document.getElementById('butooooon').onclick =
    function(){
    if (counter > 4){
        let formulascorosti = "#form" + counter;
        document.querySelector(formulascorosti).remove();
        counter -= 1;
    }
    return true;};