jQuery(document).ready(function($){

  $('header').css('display','none');

  var search_bar = '<div class="col-md-6 col-md-offset-3 col-xs-12" style="margin-top:20px;">'+
    '<form action="/search" method="GET" class="form-inline" style="width:100%;">'+
      '<div class="col-md-10 col-xs-10 no-padding">'+
        '<input type="text" placeholder="Search Movie" class="form-control search-bar" style="width:100%;height:35px;" required name="moviename">'+
      '</div>'+
      '<div class="col-md-2 col-xs-2 no-padding">'+
        '<button class="btn search-btn"><span class="fontawesome-search"></button>'+
      '</div>'+
    '</form>'+
  '</div>'


  var mobile_content = '<div class="col-md-12 col-xs-12 no-padding senti-main-content center">'+
  '<div class="col-md-12 col-xs-10 no-padding">'+
  '<img src="/static/website/img/sentimov.png" alt="" class="img-responsive" />'+ search_bar +
  '</div></div>';

  var desktop_content = '<div class="center skip">SKIP VIDEO</div><video id="myVideo" autoplay style="width:100%;">'+
  '<source src="/static/website/vid/main_vid.mp4" type="video/mp4">Your browser does not support the video tag.</video>';

  var desktop_content_later = '<div class="col-md-12 col-xs-12 no-padding center home-bg-desktop">'+
  '<img src="/static/website/img/bg.jpg" alt="" class="img-responsive" />'+
  '<div class="col-md-12 no-padding center" style="position:absolute;">'+
  '<div class="col-md-6 no-padding">'+
  '<div class="col-md-12 no-padding center"><img src="/static/website/img/sentimov.png" alt="" class="img-responsive" /></div>'  + search_bar +
  '</div>'+
  '</div></div>';

	//cache some jQuery objects
	var transitionLayer = $('.cd-transition-layer'),
		transitionBackground = transitionLayer.children(),
    homeContent = $('.home-content'),
    navbar = $('.cd-auto-hide-header');

    //check device
    if( /Android|webOS|iPhone|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
      homeContent.css('height','calc(100% - 60px)');
      homeContent.append(mobile_content);
    }
    else {
      
      homeContent.css('opacity', '1');
      homeContent.css('height','calc(100%)');
      homeContent.append(desktop_content_later);
      $('.home-bg-desktop').addClass('fade-in');

      /*
      homeContent.append(desktop_content);

      function endVideo(){
        homeContent.removeClass('fade-in').addClass('fade-out');
        setTimeout(function(){
          homeContent.empty();
          homeContent.css('opacity', '1');
          homeContent.css('height','calc(100%)');
          homeContent.append(desktop_content_later);
          $('.home-bg-desktop').addClass('fade-in');
        },2000);
      }

      $('.skip').click(function(){
        endVideo();
        $('#myVideo').get(0).pause();
      });

      document.getElementById('myVideo').addEventListener('ended',myHandler,false);
      function myHandler(e){
        endVideo();
      }
      */
    }

  homeContent.addClass('fade-in');
  navbar.addClass('fade-in').css('z-index','11');

	var frameProportion = 1.78, //png frame aspect ratio
		frames = 25, //number of png frames
		resize = false;

	//set transitionBackground dimentions
	setLayerDimensions();
	$(window).on('resize', function(){
		if( !resize ) {
			resize = true;
			(!window.requestAnimationFrame) ? setTimeout(setLayerDimensions, 300) : window.requestAnimationFrame(setLayerDimensions);
		}
	});

  transitionLayer.addClass('visible opening');
  var delay = ( $('.no-cssanimations').length > 0 ) ? 0 : 600;

	function setLayerDimensions() {
		var windowWidth = $(window).width(),
			windowHeight = $(window).height(),
			layerHeight, layerWidth;

		if( windowWidth/windowHeight > frameProportion ) {
			layerWidth = windowWidth;
			layerHeight = layerWidth/frameProportion;
		} else {
			layerHeight = windowHeight*1.2;
			layerWidth = layerHeight*frameProportion;
		}

		transitionBackground.css({
			'width': layerWidth*frames+'px',
			'height': layerHeight+'px',
		});

		resize = false;
	}

});
