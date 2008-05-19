/*HM_Loader.js
  * by Peter Belesis. v4.2.3 020402
  * Copyright (c) 2002 Peter Belesis. All Rights Reserved.
  */

     HM_DOM = (document.getElementById) ? true : false;
     HM_NS4 = (document.layers) ? true : false;
      HM_IE = (document.all) ? true : false;
     HM_IE4 = HM_IE && !HM_DOM;
     HM_Mac = (navigator.appVersion.indexOf("Mac") != -1);
    HM_IE4M = HM_IE4 && HM_Mac;

   HM_Opera = (navigator.userAgent.indexOf("Opera")!=-1);
   HM_Konqueror = (navigator.userAgent.indexOf("Konqueror")!=-1);

  //4.2.3
  //HM_IsMenu = !HM_Opera && !HM_Konqueror && !HM_IE4M && (HM_DOM || HM_NS4 || HM_IE4);
  HM_IsMenu = !HM_Opera && !HM_IE4M && (HM_DOM || HM_NS4 || HM_IE4 || HM_Konqueror);

  HM_BrowserString = HM_NS4 ? "NS4" : HM_DOM ? "DOM" : "IE4";

  if(window.event + "" == "undefined") event = null;
  function HM_f_PopUp(){return false};
  function HM_f_PopDown(){return false};
  popUp = HM_f_PopUp;
  popDown = HM_f_PopDown;


  HM_GL_MenuWidth          = 130;
  HM_GL_FontFamily         = "Verdana, Helvetica, Arial, sans-serif";
  HM_GL_FontSize           = HM_NS4 ? 10 : 7;
  HM_GL_FontBold           = true;
  HM_GL_FontItalic         = false;
  HM_GL_FontColor          = "#000000";
  HM_GL_FontColorOver      = "#eaeaea";
  HM_GL_BGColor            = "cccccc";
  HM_GL_BGColorOver        = "b12f2b";
  HM_GL_ItemPadding        = 2;

  HM_GL_BorderWidth        = 1;
  HM_GL_BorderColor        = "#000000";
  HM_GL_BorderStyle        = "solid";
  HM_GL_SeparatorSize      = 1;
  HM_GL_SeparatorColor     = "#000000";
  HM_GL_ImageSrc = "media/global/HM_More_black_right.gif";
  HM_GL_ImageSrcLeft = "media/global/HM_More_black_left.gif";
  HM_GL_ImageSrcOver = "media/global/HM_More_white_right.gif";
  HM_GL_ImageSrcLeftOver = "media/global/HM_More_white_left.gif";

  HM_GL_ImageSize          = 4;
  HM_GL_ImageHorizSpace    = 3;
  HM_GL_ImageVertSpace     = 4;

  HM_GL_KeepHilite         = false;
  HM_GL_ClickStart         = false;
  HM_GL_ClickKill          = 0;
  HM_GL_ChildOverlap       = 0;
  HM_GL_ChildOffset        = 0;
  HM_GL_ChildPerCentOver   = null;
  HM_GL_TopSecondsVisible  = 0;
  HM_GL_ChildSecondsVisible = 0;
  HM_GL_StatusDisplayBuild = 0;
  HM_GL_StatusDisplayLink  = 0;
  HM_GL_UponDisplay        = null;
  HM_GL_UponHide           = null;

  HM_GL_RightToLeft      = false;
  HM_GL_CreateTopOnly      = true;
  HM_GL_ShowLinkCursor     = true;

  HM_GL_ScrollEnabled = false;
  HM_GL_ScrollBarHeight = 14;
  HM_GL_ScrollBarColor = "lightgrey";
  HM_GL_ScrollImgSrcTop = "media/global/HM_More_black_top.gif";
  HM_GL_ScrollImgSrcBot = "media/global/HM_More_black_bot.gif";
  HM_GL_ScrollImgWidth = 9;
  HM_GL_ScrollImgHeight = 5;
  HM_GL_ScrollBothBars = true;

  // the following function is included to illustrate the improved JS expression handling of
  // the left_position and top_position parameters introduced in 4.0.9
  // and modified in 4.1.3 to account for IE6 standards-compliance mode
  // you may delete if you have no use for it

  function HM_f_CenterMenu(topmenuid) {
      var MinimumPixelLeft = 0;
      var TheMenu = HM_DOM ? document.getElementById(topmenuid) : window[topmenuid];
      var TheMenuWidth = HM_DOM ? parseInt(TheMenu.style.width) : HM_IE4 ? TheMenu.style.pixelWidth : TheMenu.clip.width;

  //4.2.3
  //      var TheWindowWidth = HM_IE ? (HM_DOM ? HM_IEcanvas.clientWidth : document.body.clientWidth) : window.innerWidth;
      var TheWindowWidth = HM_IE ? (HM_DOM ? HM_Canvas.clientWidth : document.body.clientWidth) : window.innerWidth;

      return Math.max(parseInt((TheWindowWidth-TheMenuWidth) / 2),MinimumPixelLeft);
  }

  if(HM_IsMenu) {
      document.write("<SCR" + "IPT LANGUAGE='JavaScript1.2' SRC='js/HM_Arrays.js' TYPE='text/javascript'><\/SCR" + "IPT>");
      document.write("<SCR" + "IPT LANGUAGE='JavaScript1.2' SRC='js/HM_Script"+ HM_BrowserString +".js' TYPE='text/javascript'><\/SCR" + "IPT>");
  }

  //end
