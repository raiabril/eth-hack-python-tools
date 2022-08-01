if (self.CavalryLogger) { CavalryLogger.start_js_script(document.currentScript); }/*FB_PKG_DELIM*/

__d("CookieConsentDialogFalcoEvent",["FalcoLoggerInternal","getFalcoLogPolicy_DO_NOT_USE"],(function(a,b,c,d,e,f){"use strict";a=b("getFalcoLogPolicy_DO_NOT_USE")("1746397");c=b("FalcoLoggerInternal").create("cookie_consent_dialog",a);e.exports=c}),null);
__d("WebCookieLocaleSelectorHandler",["CookieConsentDialogFalcoEvent","IntlUtils","createArrayFromMixed"],(function(a,b,c,d,e,f,g){var h="blocking_cookie_banner";a={init:function(a,b,e,f,g){a.addEventListener("click",function(){c("CookieConsentDialogFalcoEvent").log(function(){return{event:f?"click_language_selector_on_manage_data":"click_language_selector_on_consent_dialog",product:g,cookie_banner_type:h}})}),b.subscribe("change",function(a,b){a=c("createArrayFromMixed")(b);a.length>=1&&d("IntlUtils").setCookieLocale(a[0].value,e,window.location.href)})}};b=a;g["default"]=b}),98);
__d("PopoverMenuContextMinWidth",["cx","CSS","Style","shield"],(function(a,b,c,d,e,f,g,h){a=function(){function a(a){var b=this;this._onSetMenu=function(){b._menu=b._popoverMenu.getMenu();b._showSubscription=b._popover.subscribe("show",c("shield")(b._updateWidth,b));var a=b._updateWidth.bind(b);b._menuSubscription=b._menu.subscribe(["change","resize"],function(){window.setTimeout(a,0)});b._updateWidth()};this._popoverMenu=a;this._popover=a.getPopover()}var b=a.prototype;b.enable=function(){this._setMenuSubscription=this._popoverMenu.subscribe("setMenu",c("shield")(this._onSetMenu,this))};b.disable=function(){this._setMenuSubscription.unsubscribe(),this._setMenuSubscription=null,this._showSubscription&&(this._showSubscription.unsubscribe(),this._showSubscription=null),this._menuSubscription&&(this._menuSubscription.unsubscribe(),this._menuSubscription=null)};b._updateWidth=function(){var a=this._menu.getRoot(),b=this._popoverMenu.getTriggerElem();b=b.offsetWidth;c("Style").set(a,"min-width",b+"px");d("CSS").conditionClass(a,"_575s",b>=a.offsetWidth)};return a}();Object.assign(a.prototype,{_setMenuSubscription:null,_showSubscription:null,_menuSubscription:null});g["default"]=a}),98);
__d("ContextualLayerPositionClassOnContext",["cx","CSS"],(function(a,b,c,d,e,f,g){a=function(){"use strict";function a(a){this._layer=a}var c=a.prototype;c.enable=function(){this._subscription=this._layer.subscribe("reposition",this._updateClassName.bind(this)),this._layer.isShown()&&this._updateClassName()};c.disable=function(){this._subscription.unsubscribe(),this._subscription=null,this._prevClassName&&(b("CSS").removeClass(this._layer.getContext(),this._prevClassName),this._prevClassName=null)};c._updateClassName=function(a,c){a=this._layer.getContext();c=h(c);if(this._prevClassName){if(this._prevClassName===c)return;b("CSS").removeClass(a,this._prevClassName)}b("CSS").addClass(a,c);this._prevClassName=c};return a}();function h(a){var b=a.getAlignment();a=a.getPosition();if(a==="below")if(b==="left")return"_nk";else if(b==="right")return"_nl";else return"_nm";else if(a==="above")if(b==="left")return"_nn";else if(b==="right")return"_no";else return"_np";else if(a==="left")return"_nq";else return"_nr"}Object.assign(a.prototype,{_subscription:null,_prevClassName:null});e.exports=a}),null);
__d("CookieAccordion",["Animation","CSS"],(function(a,b,c,d,e,f,g){"use strict";var h=125;function a(a,b,c,d,e){d=a.querySelector(d);var f=a.querySelector(c);if(d&&f){var g=d.querySelector(e);g&&d.addEventListener("click",function(){return k(f,g,b)})}}function i(a){new(c("Animation"))(a).hide().blind().to("height",0).ease(c("Animation").ease.end).duration(h).go()}function j(a){new(c("Animation"))(a).show().blind().to("height","auto").ease(c("Animation").ease.begin).duration(h).go()}function k(b,a,c){var e=d("CSS").hasClass(b,c);e?l(b,a,c):m(b,a,c)}function l(b,a,c){j(b),d("CSS").removeClass(b,c),a.style.transform="rotate(270deg)"}function m(b,a,c){i(b),d("CSS").addClass(b,c),a.style.transform="rotate(90deg)"}g.init=a}),98);
__d("CookieConsentAcceptHandlerUtils",["DeferredCookie"],(function(a,b,c,d,e,f,g){"use strict";a={submitCookieConsent:function(a,b,d,e){var f={};if(e!=null){var g=new Map();e=document.getElementsByName(e);for(var h=0;h<e.length;h++){var i=e[h];i instanceof HTMLInputElement&&(i.checked?(g.set(i.value,2),f[i.value]=!0):(g.set(i.value,1),f[i.value]=!1))}c("DeferredCookie").flushAllCookiesINTERNALONLY(d,g,b,a)}else c("DeferredCookie").flushAllCookiesINTERNALONLY(d,null,b,a);return f}};b=a;g["default"]=b}),98);
__d("WebCookieUseSingleLevelManageDialogController",["Arbiter","CSS","CookieConsentAcceptHandlerUtils","CookieConsentDialogFalcoEvent"],(function(a,b,c,d,e,f,g){"use strict";var h="blocking_cookie_banner";a={init:function(a,b,e,f,g){if(document.body&&d("CSS").hasClass(document.body,"hideBanner"))return;document.body&&d("CSS").addClass(document.body,"hasCookieBanner");i(b,a,e,!1,f);g!=null&&i(g,a,e,!0,f);window.addEventListener?window.addEventListener("load",function(){k(a,!0)}):document.attachEvent&&document.attachEvent("load",function(){k(a,!0)});c("CookieConsentDialogFalcoEvent").log(function(){return{event:"render_consent_flow",product:e,cookie_banner_type:h}})},initMobileLocaleMenu:function(a,b,d){j(a,function(){c("CookieConsentDialogFalcoEvent").logImmediately(function(){return{event:"click_language_selector_on_consent_dialog",product:d,cookie_banner_type:h}})}),j(b,function(){c("CookieConsentDialogFalcoEvent").logImmediately(function(){return{event:"click_language_selector_on_manage_data",product:d,cookie_banner_type:h}})})}};function i(a,b,e,f,g,i){var l=function(){c("CookieConsentAcceptHandlerUtils").submitCookieConsent(f,e==="WhatsApp",g,i);document.body&&d("CSS").removeClass(document.body,"hasCookieBanner");k(b,!1);c("Arbiter").inform("WebCookieUseBannerController/close");var a=f==!0?"accept_essential_manage_data":"accept_manage_data";c("CookieConsentDialogFalcoEvent").log(function(){return{event:a,cookie_banner_type:h,product:e,consent_extra_data:null}})};j(a,l)}function j(a,b){a.addEventListener?a.addEventListener("click",b):a.attachEvent&&a.attachEvent("onclick",b)}function k(a,b){a instanceof HTMLElement?(a.style.display=b?"block":"none",b&&(a.tabIndex=a.tabIndex,a.focus())):b?a.show():a.hide()}b=a;g["default"]=b}),98);