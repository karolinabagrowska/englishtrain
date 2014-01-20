


(function($){
    
        
    $.fn.ultraslider = function(options)
    {
    	       
        var defaults = {
        	//DOM elements
            
            //items
            'collection' : false, 

            //events
            'onLoadSlide' : function () {},  
            'custom_events' : function () {},  
            
            //options
			'autoplay': true
        };
         
        
        /* *** CONSTRUCTOR *** */ 
        
        // Settings in every plugin
        var obj = this;
        this.element = $(this); 
        obj.config = $.extend(defaults, options || {});
        
        

        var currentSlide = 0;
        obj.timeOutId = false;
     	var slides = new Array(); // Store array of images collected from DOM
     	
     	
		_getSlides(); // Parse DOM to find a slide elements
        
        /* *** END CONSTRUCTOR *** */
        
      
       
        
        /* PRIVATE METHODS */
        function _getSlides ()
        {        	
        	obj.config.collection.each(function (index, element)
        	{        		
        		var slide_id = index;
        		var slide_elements = new Array(); // reset all slide elements        		
        		var longer_end = 0;
        		
        		$(element).children("div").each(function (index, element){
        			// Find and save all slide elements from DOM to JS array
        			
        			var element_dom = $(element);
        			var slide_element_options = {}; // Reset store options of current slide        			
	        		slide_element_options = {	        			        			
	        			'slide_id': slide_id,	
	        			'element': element_dom,
	        			'x': element_dom.attr("data-x"),			
	        			'y': element_dom.attr("data-y"),			
	        			'speed': element_dom.attr("data-speed"),			
	        			'start': element_dom.attr("data-start"),			
	        			'easing': element_dom.attr("data-easing"),			
	        			'end': element_dom.attr("data-end"),					
	        			'endspeed': element_dom.attr("data-endspeed"),			
	        			'endeasing': element_dom.attr("data-endeasing")	
	        		};
        			slide_element = new SlideElement(slide_element_options, obj);
        			slide_elements[index] = slide_element;
        			
        			// Extend longer end to maximum
        			if (slide_element.end > longer_end){        				
    					longer_end = slide_element.end;
    				}
        		});
        		
        		
        		var options = {}; // Reset store options of current slide
        		options = {
        			'id': $(element).find('img').attr('class'),        			
        			'longer_end': longer_end,        			
        			'slide_elements': slide_elements,
        			'element': element,		
        		};
        		
        		
        		slide = new Slide(options, obj);
        		slides[slide_id] = slide;
        		 		
        	});
        }
        
       	
        
        var _getCurrent = function (index)
        {       	
        	
        	if (typeof(index) != 'number')
        	{
        		return slides[currentSlide];
        	}
        	
        	if (index < 0)
        	{
        		currentSlide = slides.length-1;
        	}
        	else if (index > slides.length-1)
        	{        		
        		currentSlide = 0;
        	}   
        	else 
        	{
        		currentSlide = index
        	}        	
        	
        	return slides[currentSlide]
        }
        
        function _hideAllSlides(){
        	obj.config.collection.hide();
        }
        
        
            
        /*END PRIVATE METHODS*/
        
        
        
        
        
        /* PUBLIC METHODS */       

		this.jumpToNext = function() {
			obj.setSlide(currentSlide + 1);
		}
		
		this.jumpToPrevious = function() {
			obj.setSlide(currentSlide - 1);
		}
       
        this.setSlide = function(index){
        	
        	
        	slide = _getCurrent(index); // Get current slide object
        	
        	obj.config.collection.hide(); // Hide all elements...
        	$(slide.element).show(); // And show only current.
        	
        	
        	slide.startAnimate();
        	
        	// Listen to finish animation
        	slide.animationComplete(function (){
        		
        		obj.jumpToNext();
        	});
        	
        	obj.config.onLoadSlide(currentSlide);
        	
        }
        
        /*END PUBLIC METHODS*/
		
		
		/* CONSTRUCTOR BOTTOM */   
		obj.setSlide(currentSlide);
		/* END CONSTRUCTOR BOTTOM */
        
        return this;
    }
    
    var Slide = function (options, obj)
    {
   
    	var longer_end = options.longer_end; // Time after which change to next slide
    	this.id = options.id;
    	var slide_elements = options.slide_elements;
		this.element = options.element;
    	
    	
    	this.startAnimate = function (){
    		// For every slide element in the slide
    		$.each(slide_elements, function(index, slide_element){    			
    			slide_element.startAnimate();
    		});
    	}
    	
    	
    	/* EVENTS */
    	this.animationComplete = function (customFunction){
    		
    		//if setTimeout is counting already...    		
    		if (obj.timeOutId){
    			clearTimeout(obj.timeOutId); // ...Stop previous counting, and ...
    		}    		
    		obj.timeOutId = setTimeout(customFunction, longer_end); // ...Start another counting.
    		
    	}
    	/* END EVENTS */
    }
    
    var SlideElement = function (options, obj)
    {
    	//options
    	var slide_element = this;
    	this.slide_id = options.slide_id;
    	this.x = options.x;
    	this.y = options.y;
    	this.speed = parseInt(options.speed);
    	this.start = options.start;
    	this.easing = options.easing;
    	this.end = options.end;
    	this.endspeed = parseInt(options.endspeed);
    	this.endeasing = options.endeasing;	
    	this.element = options.element;
    	
    	var start_x, start_y;
    	
    	// parameters    	
    	var time_out_end = false;
    	var time_out_start = false;
    	
    	/* PUBLIC METHODS */    	
    	this.startAnimate = function(){
    		
    		_placeOutOfBox();
    		
    		//if is counting already...
    		if (time_out_start){
    			clearTimeout(time_out_start); // ...Stop previous counting, and ...
    		}    		
    		time_out_start = setTimeout(_startAnimate, slide_element.start); // ...Start another counting, when begin starting animation.
    		
    		//if is counting already...
    		if (time_out_end){
    			clearTimeout(time_out_end); // ...Stop previous counting, and ...
    		}    		
    		time_out_end = setTimeout(_finishAnimate, slide_element.end); // ...Start another counting, when begin finishing animation.
    	}
    	
    	
    	/* END PUBLIC METHODS */
    	
    	
    	/* PRIVATE METHODS */
    	function _startAnimate(){
    		
    		$(slide_element.element)
    		.animate({
    			"left":slide_element.x,
    			"top":slide_element.y
    		},
    		{duration: slide_element.speed,easing: slide_element.easing});
    		
    	}
    	
    	function _finishAnimate(){
    		$(slide_element.element)
    		.animate({
    			left: start_x,
    			top: start_y
    		},
    		{duration: slide_element.endspeed,easing: slide_element.endeasing}); 
    	}
    	
    	function _placeOutOfBox(){
    		/* place element of of visible box and save it's hidden position */
    		
    		var el_width = $(slide_element.element).width(); 
    		var el_height = $(slide_element.element).height();
    		var type = $(slide_element.element).attr("class");
    		
    		
    		// Different values od pos, depend on the type of positioning from class of div
    		if (type == "lefttop"){
    			start_x = el_width * -1;
    			start_y = el_height * -1;
    		}
    		else if (type == "top"){
    			start_x = slide_element.x;
    			start_y = el_height * -1;    			
    		}
    		else if (type == "right"){
    			start_x = $(obj.element).width() + el_width;
    			start_y = slide_element.y;
    		}
    		else if (type == "left"){
    			start_x = el_width * -1;
    			start_y = slide_element.y;
    		}
    		
    		
    		$(slide_element.element).css({
    			left: parseInt(start_x),
    			top: parseInt(start_y)
    		});


    	}
    	/* END PRIVATE METHODS */
    	

    }
    
    
    
})(jQuery);
