function WM_netscapeCssFix() {
  /*
  // It gets around another unfortunate bug whereby Netscape 
  // fires a resize event when the scrollbars pop up. This 
  // checks to make sure that the window's available size 
  // has actually changed.
  */
  if (document.WM.WM_netscapeCssFix.initWindowWidth != window.innerWidth || document.WM.WM_netscapeCssFix.initWindowHeight != window.innerHeight) {
    document.location = document.location;
  }
}

function WM_netscapeCssFixCheckIn() {
  // This function checks to make sure the version of Netscape 
  // in use contains the bug; if so, it records the window's 
  // width and height and sets all resize events to be handled 
  // by the WM_netscapeCssFix() function.
  if ((navigator.appName == 'Netscape') && (parseInt(navigator.appVersion) == 4)) {
    if (typeof document.WM == 'undefined'){
      document.WM = new Object;
    }
    if (typeof document.WM.WM_scaleFont == 'undefined') {
      document.WM.WM_netscapeCssFix = new Object;
      document.WM.WM_netscapeCssFix.initWindowWidth = window.innerWidth;
      document.WM.WM_netscapeCssFix.initWindowHeight = window.innerHeight;
    }
    window.onresize = WM_netscapeCssFix;
  }
}

WM_netscapeCssFixCheckIn()

// - Preload and Rollover code start

function WM_preloadImages() {
/*
Loads images into the browser's cache for later use.
Usage: WM_preloadImages('image 1 URL', 'image 2 URL', 'image 3 URL', ...);
*/

  // Don't bother if there's no document.images
  if (document.images) {
    if (typeof(document.WM) == 'undefined'){
      document.WM = new Object();
    }
    document.WM.loadedImages = new Array();
    // Loop through all the arguments.
    var argLength = WM_preloadImages.arguments.length;
    for(arg=0;arg<argLength;arg++) {
      // For each arg, create a new image.
      document.WM.loadedImages[arg] = new Image();
      // Then set the source of that image to the current argument.
      document.WM.loadedImages[arg].src = WM_preloadImages.arguments[arg];
    }
  }
}


function WM_imageSwap(daImage, daSrc){
  var objStr,obj;
  /*
    Changes the source of an image.
    Usage: WM_imageSwap(originalImage, 'newSourceUrl');
  */

  // Check to make sure that images are supported in the DOM.
  if(document.images){
    // Check to see whether you are using a name, number, or object
    if (typeof(daImage) == 'string') {
      // This whole objStr nonesense is here solely to gain compatability
      // with ie3 for the mac.
      objStr = 'document.' + daImage;
      obj = eval(objStr);
      obj.src = daSrc;
    } else if ((typeof(daImage) == 'object') && daImage && daImage.src) {
      daImage.src = daSrc;
    }
  }
}



/*-------------------------------------------------- Browser detection ----- */

/*
ua.js revision 0.200 2001-12-03

Contributor(s): Bob Clary, Netscape Communications, Copyright 2001

Netscape grants you a royalty free license to use, modify and 
distribute this software provided that this copyright notice 
appears on all copies.  This software is provided "AS IS," 
without a warranty of any kind.
*/

function xbDetectBrowser()
{
  var oldOnError = window.onerror;
  var element = null;

  window.onerror = null;
  
  // work around bug in xpcdom Mozilla 0.9.1
  window.saveNavigator = window.navigator;

  navigator.OS    = '';
  navigator.version  = parseFloat(navigator.appVersion);
  navigator.org    = '';
  navigator.family  = '';

  var platform;
  if (typeof(window.navigator.platform) != 'undefined')
  {
    platform = window.navigator.platform.toLowerCase();
    if (platform.indexOf('win') != -1)
      navigator.OS = 'win';
    else if (platform.indexOf('mac') != -1)
      navigator.OS = 'mac';
    else if (platform.indexOf('unix') != -1 || platform.indexOf('linux') != -1 || platform.indexOf('sun') != -1)
      navigator.OS = 'nix';
  }

  var i = 0;
  var ua = window.navigator.userAgent.toLowerCase();
  
  if (ua.indexOf('opera') != -1)
  {
    i = ua.indexOf('opera');
    navigator.family  = 'opera';
    navigator.org    = 'opera';
    navigator.version  = parseFloat('0' + ua.substr(i+6), 10);
  }
  else if ((i = ua.indexOf('msie')) != -1)
  {
    navigator.org    = 'microsoft';
    navigator.version  = parseFloat('0' + ua.substr(i+5), 10);
    
    if (navigator.version < 4)
      navigator.family = 'ie3';
    else
      navigator.family = 'ie4'
  }
  else if (ua.indexOf('gecko') != -1)
  {
    navigator.family = 'gecko';
    var rvStart = navigator.userAgent.indexOf('rv:') + 3;
    var rvEnd = navigator.userAgent.indexOf(')', rvStart);
    var rv = navigator.userAgent.substring(rvStart, rvEnd);
    var decIndex = rv.indexOf('.');
    if (decIndex != -1)
    {
      rv = rv.replace(/\./g, '')
      rv = rv.substring(0, decIndex-1) + '.' + rv.substr(decIndex)
    }
    navigator.version = parseFloat(rv);

    if (ua.indexOf('netscape') != -1)
      navigator.org = 'netscape';
    else if (ua.indexOf('compuserve') != -1)
      navigator.org = 'compuserve';
    else
      navigator.org = 'mozilla';
  }
  else if ((ua.indexOf('mozilla') !=-1) && (ua.indexOf('spoofer')==-1) && (ua.indexOf('compatible') == -1) && (ua.indexOf('opera')==-1)&& (ua.indexOf('webtv')==-1) && (ua.indexOf('hotjava')==-1))
  {
    var is_major = parseFloat(navigator.appVersion);
    
    if (is_major < 4)
      navigator.version = is_major;
    else
    {
      i = ua.lastIndexOf('/')
      navigator.version = parseFloat('0' + ua.substr(i+1), 10);
    }
    navigator.org = 'netscape';
    navigator.family = 'nn' + parseInt(navigator.appVersion);
  }
  else if ((i = ua.indexOf('aol')) != -1 )
  {
    // aol
    navigator.family  = 'aol';
    navigator.org    = 'aol';
    navigator.version  = parseFloat('0' + ua.substr(i+4), 10);
  }
  else if ((i = ua.indexOf('hotjava')) != -1 )
  {
    // hotjava
    navigator.family  = 'hotjava';
    navigator.org    = 'sun';
    navigator.version  = parseFloat(navigator.appVersion);
  }

  window.onerror = oldOnError;
}
xbDetectBrowser()

function setDate()
	{
		var months = new Array("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
		var today = new Date();
		var monthNow = months[today.getMonth()];
		var dayNow = today.getDate();
		var yearNow = today.getFullYear();
		var fullDate = monthNow + " " + dayNow + ", " + yearNow;
		document.write(fullDate);
	}
	
function openPlayer(PlayerURL)
 				{
     				window.open(PlayerURL,"Player","left=10,top=10,height=400,width=600,resizable=0");
 				}
 				
function openArchive(PlayerURL)
 				{
     				window.open(PlayerURL,"Player","left=10,top=10,height=560,width=660,resizable=1");
 				} 				
 				
