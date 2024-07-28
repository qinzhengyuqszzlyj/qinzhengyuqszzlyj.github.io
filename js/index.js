var index = 0;
var tab = $('.tz-title');
var tz = $('.tz-con');//
var title=$('.tz-title');
$(tab[0]).css('color','#A43239');
$(tz[0]).css('display','block');
$(title[0]).css('border-color','#A43239');

for(var i = 0 ; i < tab.length ; i++){
	(function(p){
		$(tab[p]).mouseover(function(){
			if(index == 0 || index){
				$(tab[index]).css('color','#666');
				$(tz[index]).css('display','none');
				$(title[index]).css('border-color','lightgray');
			}
			$(tab[p]).css('color','#A43239');
			$(tz[p]).css('display','block');
			$(title[p]).css('border-color','#A43239');
			index =p;	
		})
	})(i)
}


var list = $('.result');
var co = $('#content').html();
var lii = $('.lii');
for(var i = 0 ; i < list.length ; i++ ){
	/*(function(r){
		$(list[r]).html() == co)
	})(i)*/
	if(list[i].innerHTML == co){
		$(list[i]).css('color','#A43239');
		$(lii[i]).css('color','#A43239');
	}
}