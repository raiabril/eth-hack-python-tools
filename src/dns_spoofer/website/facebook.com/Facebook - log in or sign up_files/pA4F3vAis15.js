if (self.CavalryLogger) { CavalryLogger.start_js_script(document.currentScript); }/*FB_PKG_DELIM*/

__d("DOMScroll",["Arbiter","DOM","DOMQuery","Vector","ViewportBounds","emptyFunction","ge","isAsyncScrollQuery","nullthrows","requireDeferred"],(function(a,b,c,d,e,f){var g=b("requireDeferred")("Animation").__setRef("DOMScroll"),h={SCROLL:"dom-scroll",_scrolling:!1,_scrollingFinishedTimeout:null,getScrollState:function(){var a=b("Vector").getViewportDimensions(),c=b("Vector").getDocumentDimensions(),d=c.x>a.x;c=c.y>a.y;d+=0;c+=0;return new(b("Vector"))(d,c)},_scrollbarSize:null,_initScrollbarSize:function(){var a=b("DOM").create("p");a.style.width="100%";a.style.height="200px";var c=b("DOM").create("div");c.style.position="absolute";c.style.top="0px";c.style.left="0px";c.style.visibility="hidden";c.style.width="200px";c.style.height="150px";c.style.overflow="hidden";c.appendChild(a);b("nullthrows")(document.body).appendChild(c);var d=a.offsetWidth;c.style.overflow="scroll";a=a.offsetWidth;d==a&&(a=c.clientWidth);b("nullthrows")(document.body).removeChild(c);h._scrollbarSize=d-a},getScrollbarSize:function(){h._scrollbarSize===null&&h._initScrollbarSize();return b("nullthrows")(h._scrollbarSize)},scrollTo:function(a,c,d,e,f,i){var j,k=0;c==null||c===!0?k=750:typeof c==="number"?k=c:parseInt(c,10)&&(k=parseInt(c,10));b("isAsyncScrollQuery")()&&(k=0);if(a instanceof b("Vector"))c=a;else{var l=b("Vector").getScrollPosition().x;a=b("Vector").getElementPosition(b("ge")(a)).y;c=new(b("Vector"))(l,a,"document");e||(c.y-=b("ViewportBounds").getTop()/(d?2:1))}d?c.y-=b("Vector").getViewportDimensions().y/2:e&&(c.y-=b("Vector").getViewportDimensions().y,c.y+=e);f&&(c.y-=f);c=c.convertTo("document");if(k)if("scrollBehavior"in b("nullthrows")(document.documentElement).style&&k===750&&!i)try{window.scrollTo({left:c.x,top:c.y,behavior:"smooth"})}catch(a){window.scrollTo(c.x,c.y)}else{l=g.getModuleIfRequired();if(l!=null){h._setScrollingForDuration(k);var m=new l(b("nullthrows")(document.body)).to("scrollTop",c.y).to("scrollLeft",c.x).ease(l.ease.end).duration(k).ondone(i).go();j=function(){m.stop()}}else window.scrollTo(c.x,c.y),i&&i()}else window.scrollTo(c.x,c.y),i&&i();b("Arbiter").inform(h.SCROLL);return j||b("emptyFunction")},scrollToID:function(a){h.scrollTo(a)},ensureVisible:function(a,c,d,e,f){var g=b("Vector").getScrollPosition().x;a=h._getBounds(a,c,d);c=a[0];d=a[1];var i=a[2];a=a[3];i<c?h.scrollTo(new(b("Vector"))(g,i,"document"),e,!1,0,0,f):a>d?i-(a-d)<c?h.scrollTo(new(b("Vector"))(g,i,"document"),e,!1,0,0,f):h.scrollTo(new(b("Vector"))(g,a,"document"),e,!1,1,0,f):f&&f()},isCurrentlyVisible:function(a,b,c){a=h._getBounds(a,b,c);b=a[0];c=a[1];var d=a[2];a=a[3];return d>=b&&a<=c},_getBounds:function(a,c,d){d==null&&(d=10);a=b("ge")(a);c&&(a=b("DOMQuery").find(a,c));c=b("Vector").getScrollPosition().y;var e=c+b("Vector").getViewportDimensions().y,f=b("Vector").getElementPosition(a).y;a=f+b("Vector").getElementDimensions(a).y;f-=b("ViewportBounds").getTop();f-=d;a+=d;return[c,e,f,a]},scrollToTop:function(a){var c=b("Vector").getScrollPosition();h.scrollTo(new(b("Vector"))(c.x,0,"document"),a!==!1)},currentlyScrolling:function(){return h._scrolling},_setScrollingForDuration:function(a){h._scrolling=!0,h._scrollingFinishedTimeout&&(clearTimeout(h._scrollingFinishedTimeout),h._scrollingFinishedTimeout=null),h._scrollingFinishedTimeout=setTimeout(function(){h._scrolling=!1,h._scrollingFinishedTimeout=null},a)}};e.exports=h}),null);
__d("LayerHideOnEscape",["Event","Keys","LayerHideSources"],(function(a,b,c,d,e,f,g){a=function(){function a(a){this._layer=a}var b=a.prototype;b.enable=function(){this._subscription=this._layer.subscribe("key",this.handle.bind(this))};b.disable=function(){this._subscription!=null&&this._subscription.unsubscribe(),this._subscription=null};b.handle=function(a,b){if(c("Event").getKeyCode(b)===c("Keys").ESC){this._layer.hide(c("LayerHideSources").ESCAPE);return!1}return void 0};return a}();Object.assign(a.prototype,{_subscription:null});g["default"]=a}),98);