// JavaScript Document
function draw()
{
  // Get the canvas element.
	  var elem = document.getElementById('myCanvas');
	  if (!elem || !elem.getContext) {
		return;
	  }
	  // Get the canvas 2d context.
	  var context = elem.getContext('2d');
	  if (!context) {
		return;
	  }
	
	  context.lineWidth   = 3;		
	  context.moveTo(690, 50);
	  context.lineTo(690, 20);
	  context.lineTo(490, 20);
	  context.lineTo(490, 50);	
	  context.lineTo(490, 20);	
	  context.lineTo(290, 20);	
	  context.lineTo(290, 50);	
	  context.lineTo(290, 20);	
	  context.lineTo( 90, 20);	
	  context.lineTo( 90, 175);	
	  context.lineTo( 90, 105);	
	  context.lineTo( 290,105);	
	  context.lineTo( 290,175);	
	  context.lineTo( 290,105);	
	  context.lineTo( 490,105);	
	  context.lineTo( 490,225);
	  context.lineTo( 490,105);	
	  context.lineTo( 690,105);	
	  context.lineTo( 690,175);	
	  context.lineTo( 690,105);	
	  context.lineTo( 890,105);	
	  context.lineTo( 890,175);	          
	  context.strokeStyle= '#999';
	  context.stroke();

	 
	  context.save();
	  context.moveTo(890, 285);		
	  context.lineTo(890, 350);
	  context.stroke();	  
	  
	  context.save();
	  context.lineWidth   = 1;
	  context.moveTo(90, 175);		
	  context.lineTo(1, 175);
	  context.lineTo(1, 197);
	  context.lineTo(90, 197);
	  context.lineTo(1, 197);
	  context.lineTo(1, 232);
	  context.lineTo(90, 232);
	  context.lineTo(1, 232);
	  context.lineTo(1, 267);
	  context.lineTo(90, 267);
	  context.lineTo(1, 267);
	  context.lineTo(1, 302);
	  context.lineTo(90, 302);
	  context.lineTo(1, 302);
	  context.lineTo(1, 337);
	  context.lineTo(90, 337);
	  context.lineTo(1, 337);
	  context.lineTo(1, 372);
	  context.lineTo(90, 372);
	  context.lineTo(1, 372);
	  context.lineTo(1, 407);
	  context.lineTo(90, 407);
	  context.lineTo(1, 407);
	  context.lineTo(1, 442);
	  context.lineTo(90, 442);
	  context.lineTo(1, 442);
	  context.lineTo(1, 477);
	  context.lineTo(90, 477);
	  context.lineTo(1, 477);
	  context.lineTo(1, 512);
	  context.lineTo(90, 512);
	  context.lineTo(1, 512);
	  context.lineTo(1, 547);
	  context.lineTo(90, 547);
	  context.lineTo(1, 547);
	  context.lineTo(1, 582);
	  context.lineTo(90, 582);
	  context.lineTo(1, 582);
	  context.lineTo(1, 617);
      context.lineTo(90, 617);
	  context.stroke();

	  context.save();
	  context.lineWidth   = 1;		
	  context.moveTo(290, 175);		
	  context.lineTo(202, 175);		
	  context.lineTo(202, 197);		
	  context.lineTo(220, 197);		
	  context.lineTo(202, 197);		
	  context.lineTo(202, 232);		
	  context.lineTo(220, 232);		
	  context.lineTo(202, 232);		
	  context.lineTo(202, 267);		
	  context.lineTo(220, 267);		
	  context.lineTo(202, 267);	
	  context.lineTo(202, 302);		
	  context.lineTo(220, 302);		
	  context.lineTo(202, 302);
	  context.lineTo(202, 337);		
	  context.lineTo(220, 337);		
	  context.lineTo(202, 337);
	  context.lineTo(202, 372);		
	  context.lineTo(220, 372);		
	  context.lineTo(202, 372);
	  context.lineTo(202, 407);		
	  context.lineTo(220, 407);		
	  context.lineTo(202, 407);
	  context.lineTo(202, 442);		
	  context.lineTo(220, 442);		
	  context.lineTo(202, 442);
	  context.stroke();	  

	  context.save();
	  context.lineWidth   = 1;		
	  context.moveTo(490, 225);		
	  context.lineTo(402, 225);		
	  context.lineTo(402, 247);		
	  context.lineTo(420, 247);		
	  context.lineTo(402, 247);		
	  context.lineTo(402, 282);		
	  context.lineTo(420, 282);		
	  context.lineTo(402, 282);		
	  context.lineTo(402, 317);		
	  context.lineTo(420, 317);		
	  context.lineTo(402, 317);		
	  context.lineTo(402, 352);		
	  context.lineTo(420, 352);		
	  context.lineTo(402, 352);		
	  context.stroke();

	  context.save();
	  context.lineWidth   = 1;		
	  context.moveTo(690, 175);		
	  context.lineTo(602, 175);		
	  context.lineTo(602, 197);		
	  context.lineTo(620, 197);		
	  context.lineTo(602, 197);		
	  context.lineTo(602, 232);		
	  context.lineTo(620, 232);		
	  context.lineTo(602, 232);		
	  context.lineTo(602, 267);		
	  context.lineTo(620, 267);		
	  context.lineTo(602, 267);	
	  context.lineTo(602, 302);		
	  context.lineTo(620, 302);		
	  context.lineTo(602, 302);
	  context.lineTo(602, 337);		
	  context.lineTo(620, 337);		
	  context.lineTo(602, 337);
	  context.lineTo(602, 372);		
	  context.lineTo(620, 372);		
	  context.lineTo(602, 372);
	  context.lineTo(602, 407);		
	  context.lineTo(620, 407);		
	  context.lineTo(602, 407);
	  context.lineTo(602, 442);		
	  context.lineTo(620, 442);		
	  context.lineTo(602, 442);
	  context.lineTo(602, 483);		
	  context.lineTo(620, 483);		
	  context.lineTo(602, 483);
	  context.lineTo(602, 525);		
	  context.lineTo(620, 525);		
	  context.lineTo(602, 525);
	  context.lineTo(602, 568);		
	  context.lineTo(620, 568);		
	  context.lineTo(602, 568);
	  context.stroke();

	  context.save();
	  context.lineWidth   = 1;		
	  context.moveTo(890, 175);		
	  context.lineTo(802, 175);		
	  context.lineTo(802, 197);		
	  context.lineTo(820, 197);		
	  context.lineTo(802, 197);		
	  context.lineTo(802, 232);		
	  context.lineTo(820, 232);		
	  context.lineTo(802, 232);		
	  context.lineTo(802, 267);		
	  context.lineTo(820, 267);		
	  context.lineTo(802, 267);
	  context.stroke();
		
  	  context.save();
	  context.moveTo(290, 500);		
	  context.lineTo(290, 515);		
	  context.lineTo(202, 515);		
	  context.lineTo(202, 540);
	  context.lineTo(220, 540);
	  context.lineTo(202, 540);
	  context.lineTo(202, 575);
	  context.lineTo(220, 575);
	  context.lineTo(202, 575);
	  context.lineTo(202, 610);
	  context.lineTo(220, 610);
	  context.lineTo(202, 610);
	  context.lineTo(202, 645);
	  context.lineTo(220, 645);
	  context.lineTo(202, 645);
  	  context.stroke();	  

	  context.save();
	  context.moveTo(490, 410);		
	  context.lineTo(490, 430);		
	  context.lineTo(402, 430);		
	  context.lineTo(402, 457);		
	  context.lineTo(420, 457);		
	  context.lineTo(402, 457);		
	  context.lineTo(402, 500);		
	  context.lineTo(420, 500);		
	  context.lineTo(402, 500);		
	  context.stroke();

	  context.save();
	  context.moveTo(490, 550);		
	  context.lineTo(490, 580);		
	  context.lineTo(402, 580);		
	  context.lineTo(402, 600);		
	  context.lineTo(420, 600);		
	  context.lineTo(402, 600);		
	  context.lineTo(402, 635);		
	  context.lineTo(420, 635);		
	  context.lineTo(402, 635);		
	  context.stroke();

}
