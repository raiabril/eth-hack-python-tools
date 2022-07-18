if (self.CavalryLogger) { CavalryLogger.start_js_script(document.currentScript); }/*FB_PKG_DELIM*/

__d("CometLruCache",["recoverableViolation"],(function(a,b,c,d,e,f,g){"use strict";var h=function(){function a(a){this.$1=a,a<=0&&c("recoverableViolation")("CometLruCache: Unable to create instance of cache with zero or negative capacity.","CometLruCache"),this.$2=new Map()}var b=a.prototype;b.set=function(a,b){this.$2["delete"](a);this.$2.set(a,b);if(this.$2.size>this.$1){a=this.$2.keys().next();a.done||this.$2["delete"](a.value)}};b.get=function(a){var b=this.$2.get(a);b!=null&&(this.$2["delete"](a),this.$2.set(a,b));return b};b.has=function(a){return this.$2.has(a)};b["delete"]=function(a){this.$2["delete"](a)};b.size=function(){return this.$2.size};b.capacity=function(){return this.$1-this.$2.size};b.clear=function(){this.$2.clear()};return a}();function a(a){return new h(a)}g.create=a}),98);
__d("ConstUriUtils",["CometLruCache","FBLogger","PHPQuerySerializer","PHPQuerySerializerNoEncoding","URIRFC3986","URISchemes","UriNeedRawQuerySVConfig","recoverableViolation"],(function(a,b,c,d,e,f,g){"use strict";var h=d("CometLruCache").create(5e3),i=new RegExp("(^|\\.)facebook\\.com$","i"),j=new RegExp("^(?:[^/]*:|[\\x00-\\x1f]*/[\\x00-\\x1f]*/)"),k=new RegExp("[\\x00-\\x2c\\x2f\\x3b-\\x40\\x5c\\x5e\\x60\\x7b-\\x7f\\uFDD0-\\uFDEF\\uFFF0-\\uFFFF\\u2047\\u2048\\uFE56\\uFE5F\\uFF03\\uFF0F\\uFF1F]"),l=c("UriNeedRawQuerySVConfig").uris.map(function(a){return{domain:a,valid:r(a)}}),m=[];function n(a,b){var d={};if(a!=null)for(var a=a.entries(),e=Array.isArray(a),f=0,a=e?a:a[typeof Symbol==="function"?Symbol.iterator:"@@iterator"]();;){var g;if(e){if(f>=a.length)break;g=a[f++]}else{f=a.next();if(f.done)break;g=f.value}g=g;d[g[0]]=g[1]}else c("FBLogger")("ConstUriUtils").warn("Passed a null query map in, this means poor client side flow coverage or client/server boundary type issue.");return b.serialize(d)}function o(a,b,d){var e=c("PHPQuerySerializer");if(["http","https"].includes(b)&&p(a)){if(a.includes("doubleclick.net")&&d!=null&&!d.startsWith("http"))return e;e=c("PHPQuerySerializerNoEncoding")}return e}function p(a){return a!=null&&l.some(function(b){return b.valid&&q(a,b.domain)})}function q(a,b){if(b===""||a==="")return!1;if(a.endsWith(b)){b=a.length-b.length-1;if(b===-1||a[b]===".")return!0}return!1}function r(a){return!k.test(a)}function s(a,b){var c=b.protocol!=null&&b.protocol!==""?b.protocol:a.getProtocol();c=b.domain!=null?o(b.domain,c):a.getSerializer();c={domain:a.getDomain(),fragment:a.getFragment(),fragmentSeparator:a.hasFragmentSeparator(),isGeneric:a.isGeneric(),originalRawQuery:a.getOriginalRawQuery(),path:a.getPath(),port:a.getPort(),protocol:a.getProtocol(),queryParams:a.getQueryParams(),serializer:c,subdomain:a.getSubdomain()};a=babelHelpers["extends"]({},c,b);c=b.queryParams!=null&&b.queryParams.size!==0;return x.getUribyObject(a,c)}function t(a,b,c,d){c===void 0&&(c=!1);var e=a.protocol!==""?a.protocol+":"+(a.isGeneric?"":"//"):"",f=a.domain!==""?a.domain:"",g=a.port!==""?":"+a.port:"",h=a.path!==""?a.path:e!==""&&e!=="mailto:"||f!==""||g!==""?"/":"";c=u(f,a.originalRawQuery,a.queryParams,b,c,(b=d)!=null?b:a.serializer);d=c.length>0?"?":"";b=a.fragment!==""?"#"+a.fragment:"";a=a.fragment===""&&a.fragmentSeparator?"#":"";return""+e+f+g+h+d+c+a+b}function u(a,b,c,d,e,f){e===void 0&&(e=!1);if(!d&&(e||p(a))){return(d=b)!=null?d:""}return n(c,f)}function v(a){var b=a.trim();b=d("URIRFC3986").parse(b)||{fragment:null,host:null,isGenericURI:!1,query:null,scheme:null,userinfo:null};var c=b.host||"",e=c.split(".");e=e.length>=3?e[0]:"";var f=o(c,b.scheme||"",b.query),g=f.deserialize(b.query||"")||{};g=new Map(Object.entries(g));g=w({domain:c,fragment:b.fragment||"",fragmentSeparator:b.fragment==="",isGeneric:b.isGenericURI,originalRawQuery:b.query,path:b.path||"",port:b.port!=null?String(b.port):"",protocol:(b.scheme||"").toLowerCase(),queryParams:g,serializer:f,subdomain:e,userInfo:(c=b==null?void 0:b.userinfo)!=null?c:""},a);return g}function w(a,b){var c={components:babelHelpers["extends"]({},a),error:"",valid:!0},e=c.components;if(!d("URISchemes").isAllowed(a.protocol)){c.valid=!1;c.error='The URI protocol "'+String(a.protocol)+'" is not allowed.';return c}if(!r(a.domain||"")){c.valid=!1;c.error="This is an unsafe domain "+String(a.domain);return c}e.port=a.port!=null&&String(a.port)||"";if(Boolean(a.userInfo)){c.valid=!1;c.error="Invalid URI: (userinfo is not allowed in a URI "+String(a.userInfo)+")";return c}a=b!=null&&b!==""?b:t(e,!1);if(e.domain===""&&e.path.indexOf("\\")!==-1){c.valid=!1;c.error="Invalid URI: (no domain but multiple back-slashes "+a+")";return c}if(!e.protocol&&j.test(a)){c.valid=!1;c.error="Invalid URI: (unsafe protocol-relative URI "+a+")";return c}if(e.domain!==""&&e.path!==""&&!e.path.startsWith("/")){c.valid=!1;c.error="Invalid URI: (domain and pathwhere path lacks leading slash "+a+")";return c}return c}var x=function(){function a(a){this.queryParams=new Map(),this.domain=a.domain,this.fragment=a.fragment,this.fragmentSeparator=Boolean(a.fragmentSeparator),this.isGenericProtocol=Boolean(a.isGeneric),this.path=a.path,this.originalRawQuery=a.originalRawQuery,this.port=a.port,this.protocol=a.protocol,this.queryParams=a.queryParams,this.serializer=a.serializer,this.subdomain=a.subdomain}var b=a.prototype;b.addQueryParam=function(a,b){if(Boolean(a)){var c=this.getQueryParams();c.set(a,b);return s(this,{queryParams:c})}return this};b.addQueryParams=function(a){if(a.size>0){var b=this.getQueryParams();a.forEach(function(a,c){b.set(c,a)});return s(this,{queryParams:b})}return this};b.addQueryParamString=function(a){if(Boolean(a)){a=a.startsWith("?")?a.slice(1):a;var b=this.getQueryParams();a.split("&").map(function(a){a=a.split("=");var c=a[0];a=a[1];b.set(c,a)});return s(this,{queryParams:b})}return this};b.addTrailingSlash=function(){var a=this.getPath();return a.length>0&&a[a.length-1]!=="/"?this.setPath(a+"/"):this};b.getDomain=function(){return this.domain};b.getFragment=function(){return this.fragment};b.getOrigin=function(){var a=this.getPort();return this.getProtocol()+"://"+this.getDomain()+(a?":"+a:"")};b.getOriginalRawQuery=function(){return this.originalRawQuery};b.getPath=function(){return this.path};b.getPort=function(){return this.port};b.getProtocol=function(){return this.protocol.toLowerCase()};b.getQualifiedUri=function(){if(!this.getDomain()){var b=String(window.location.href);b=b.slice(0,b.indexOf("/",b.indexOf(":")+3));return a.getUri(b+this.toString())}return this};b.getQueryParam=function(a){a=this.queryParams.get(a);if(typeof a==="string")return a;else{a=JSON.stringify(a);return a==null?a:JSON.parse(a)}};b.getQueryData=function(){return Object.fromEntries(this.getQueryParams())};b.getQueryParams=function(){return new Map(JSON.parse(JSON.stringify(Array.from(this.queryParams))))};b.getQueryString=function(a){a===void 0&&(a=!1);return u(this.domain,this.originalRawQuery,this.queryParams,!1,a,this.serializer)};b.getRegisteredDomain=function(){if(!this.getDomain())return"";if(!this.isFacebookUri())return null;var a=this.getDomain().split("."),b=a.indexOf("facebook");b===-1&&(b=a.indexOf("workplace"));return a.slice(b).join(".")};b.getSerializer=function(){return this.serializer};b.getSubdomain=function(){return this.subdomain};b.getUnqualifiedUri=function(){if(this.getDomain()){var b=this.toString();return a.getUri(b.slice(b.indexOf("/",b.indexOf(":")+3)))}return this};a.getUri=function(b){b=b.trim();var d=h.get(b);if(d==null){var e=v(b);if(e.valid)d=new a(e.components),h.set(b,d);else{c("FBLogger")("ConstUriUtils").blameToPreviousFrame().warn(e.error);return null}}return d};a.getUribyObject=function(b,d){var e=t(b,d),f=h.get(e);if(f==null){d&&(b.originalRawQuery=n(b.queryParams,b.serializer));d=w(b);if(d.valid)f=new a(d.components),h.set(e,f);else{c("recoverableViolation")(d.error,"ConstUri");return null}}return f};b.hasFragmentSeparator=function(){return this.fragmentSeparator};b.isEmpty=function(){return!(this.getPath()||this.getProtocol()||this.getDomain()||this.getPort()||this.queryParams.size>0||this.getFragment())};b.isFacebookUri=function(){var a=this.toString();if(a==="")return!1;return!this.getDomain()&&!this.getProtocol()?!0:["https","http"].indexOf(this.getProtocol())!==-1&&i.test(this.getDomain())};b.isGeneric=function(){return this.isGenericProtocol};b.isSameOrigin=function(a){if(this.getProtocol()&&this.getProtocol()!==a.getProtocol())return!1;if(this.getDomain()&&this.getDomain()!==a.getDomain())return!1;if(this.getPort()&&this.getPort()!==a.getPort())return!1;return this.toString()===""||a.toString()===""?!1:!0};b.isSubdomainOfDomain=function(b){var c=a.getUri(b);return c!=null&&q(this.domain,b)};b.isSecure=function(){return this.getProtocol()==="https"};b.removeQueryParams=function(a){if(Array.isArray(a)&&a.length>0){var b=this.getQueryParams();a.map(function(a){return b["delete"](a)});return s(this,{queryParams:b})}return this};b.removeQueryParam=function(a){if(Boolean(a)){var b=this.getQueryParams();b["delete"](a);return s(this,{queryParams:b})}return this};b.replaceQueryParam=function(a,b){if(Boolean(a)){var c=this.getQueryParams();c.set(a,b);return s(this,{queryParams:c})}return this};b.replaceQueryParams=function(a){return s(this,{queryParams:a})};b.replaceQueryParamString=function(a){if(a!=null){a=a.startsWith("?")?a.slice(1):a;var b=this.getQueryParams();a.split("&").map(function(a){a=a.split("=");var c=a[0];a=a[1];b.set(c,a)});return s(this,{queryParams:b})}return this};b.setDomain=function(a){if(Boolean(a)){var b=a.split(".");b=b.length>=3?b[0]:"";return s(this,{domain:a,subdomain:b})}return this};b.setFragment=function(a){return a==="#"?s(this,{fragment:"",fragmentSeparator:!0}):s(this,{fragment:a,fragmentSeparator:a!==""})};b.setPath=function(a){return a!=null?s(this,{path:a}):this};b.setPort=function(a){return Boolean(a)?s(this,{port:a}):this};b.setProtocol=function(a){return Boolean(a)?s(this,{protocol:a}):this};b.setSecure=function(a){return this.setProtocol(a?"https":"http")};b.setSubDomain=function(a){if(Boolean(a)){var b=this.domain.split(".");b.length>=3?b[0]=a:b.unshift(a);return s(this,{domain:b.join("."),subdomain:a})}return this};b.stripTrailingSlash=function(){return this.setPath(this.getPath().replace(/\/$/,""))};a.$1=function(a){a=a;for(var b=0;b<m.length;b++){var c=m[b];a=c(a)}return a};b.$2=function(b,c){c===void 0&&(c=!1);return t({domain:a.$1(this.domain),fragment:this.fragment,fragmentSeparator:this.fragmentSeparator,isGeneric:this.isGenericProtocol,originalRawQuery:this.originalRawQuery,path:this.path,port:this.port,protocol:this.protocol,queryParams:this.queryParams,serializer:b,subdomain:this.subdomain,userInfo:""},!1,c)};b.toStringRawQuery=function(){this.rawStringValue==null&&(this.rawStringValue=this.$2(c("PHPQuerySerializerNoEncoding")));return this.rawStringValue};b.toString=function(){this.stringValue==null&&(this.stringValue=this.$2(this.serializer));return this.stringValue};b.toStringPreserveQuery=function(){return this.$2(this.serializer,!0)};a.isValidUri=function(b){var c=h.get(b);if(c!=null)return!0;c=v(b);if(c.valid){h.set(b,new a(c.components));return!0}return!1};return a}();function a(a){if(a instanceof x)return a;else return null}function b(a){m.push(a)}e=x.getUri;f=x.isValidUri;g.isSubdomainOfDomain=q;g.isConstUri=a;g.registerDomainFilter=b;g.getUri=e;g.isValidUri=f}),98);
__d("HostnameRewriter",["ConstUriUtils","Env","URI","isFacebookURI","lowerFacebookDomain"],(function(a,b,c,d,e,f,g){var h=function(a){return String(a).replace(/([.*+?^=!:${}()|[\]\/\\])/g,"\\$1")},i=null,j=null,k=new RegExp("facebook\\.com$"),l=new RegExp("^www\\.(|.*\\.)facebook\\.com$"),m=null,n="facebook.com",o=null,p=new RegExp("fbcdn\\.net$"),q=new RegExp("^www\\."),r=new RegExp("(^|\\.)(facebook\\.com|workplace\\.com)$","i");function s(){i=null;var a="(^|\\.)";m=a+h(n)+"$";j=null}function t(){if(m==null)return null;if(i)return i;i=new RegExp(m,"i");return i}function u(){if(j)return j;j=new RegExp("(^|\\.)("+h(n)+"|facebook\\.com)$","i");return j}function v(a){if(u().test(a)&&n!=null)return a.replace(k,n);else if(o!=null&&a!==null)return a.replace(p,o);return a}function w(a){return l.test(a)?a.replace(q,"web."):a}function x(a){return function(b){b=new(c("URI"))(b);b.setDomain(a(b.getDomain()));return b}}function y(a,b){n=a,o=b,s(),c("isFacebookURI").setRegex(t()),c("URI").registerFilter(x(v)),d("ConstUriUtils").registerDomainFilter(v),c("lowerFacebookDomain").setDomain(n)}function a(a,b){n=a,c("URI").registerFilter(x(w))}function b(){var a=c("Env").hostnameRewriterConfig;if(a==null)return;switch(a.site){case"onion":y(a.inboundName,a.cdnDomainName);break}}function e(){c("isFacebookURI").setRegex(r)}g.registerFacebookOverTorFilters=y;g.registerInternetDotOrgFilters=a;g.maybeRegisterFilters=b;g.treatWorkplaceAsFacebookURI=e}),98);
__d("EventEmitterWithValidation",["BaseEventEmitter"],(function(a,b,c,d,e,f){"use strict";a=function(a){babelHelpers.inheritsLoose(b,a);function b(b,c){var d;d=a.call(this)||this;d.$EventEmitterWithValidation1=Object.keys(b);d.$EventEmitterWithValidation2=Boolean(c);return d}var c=b.prototype;c.emit=function(b){if(this.$EventEmitterWithValidation1.indexOf(b)===-1){if(this.$EventEmitterWithValidation2)return;throw new TypeError(g(b,this.$EventEmitterWithValidation1))}return a.prototype.emit.apply(this,arguments)};return b}(b("BaseEventEmitter"));function g(a,b){a='Unknown event type "'+a+'". ';a+="Known event types: "+b.join(", ")+".";return a}e.exports=a}),null);
__d("mixInEventEmitter",["invariant","EventEmitterWithHolding","EventEmitterWithValidation","EventHolder"],(function(a,b,c,d,e,f,g,h){"use strict";function a(a,b,c){b||h(0,3159);var d=a.prototype||a;d.__eventEmitter&&h(0,3160);a=a.constructor;a&&(a===Object||a===Function||h(0,3161));d.__types=babelHelpers["extends"]({},d.__types,b);d.__ignoreUnknownEvents=Boolean(c);Object.assign(d,i)}var i={emit:function(a,b,c,d,e,f,g){return this.__getEventEmitter().emit(a,b,c,d,e,f,g)},emitAndHold:function(a,b,c,d,e,f,g){return this.__getEventEmitter().emitAndHold(a,b,c,d,e,f,g)},addListener:function(a,b,c){return this.__getEventEmitter().addListener(a,b,c)},once:function(a,b,c){return this.__getEventEmitter().once(a,b,c)},addRetroactiveListener:function(a,b,c){return this.__getEventEmitter().addRetroactiveListener(a,b,c)},listeners:function(a){return this.__getEventEmitter().listeners(a)},removeAllListeners:function(){this.__getEventEmitter().removeAllListeners()},removeCurrentListener:function(){this.__getEventEmitter().removeCurrentListener()},releaseHeldEventType:function(a){this.__getEventEmitter().releaseHeldEventType(a)},__getEventEmitter:function(){if(!this.__eventEmitter){var a=new(c("EventEmitterWithValidation"))(this.__types,this.__ignoreUnknownEvents),b=new(c("EventHolder"))();this.__eventEmitter=new(c("EventEmitterWithHolding"))(a,b)}return this.__eventEmitter}};g["default"]=a}),98);
__d("pageID",["WebSession"],(function(a,b,c,d,e,f,g){"use strict";a=d("WebSession").getPageId_DO_NOT_USE();g["default"]=a}),98);
__d("NavigationMetricsCore",["mixInEventEmitter","pageID"],(function(a,b,c,d,e,f,g){var h={NAVIGATION_DONE:"NAVIGATION_DONE",EVENT_OCCURRED:"EVENT_OCCURRED"},i={tti:"tti",e2e:"e2e",all_pagelets_loaded:"all_pagelets_loaded",all_pagelets_displayed:"all_pagelets_displayed"},j=0,k={},l=function(){function a(){this.eventTimings={tti:null,e2e:null,all_pagelets_loaded:null,all_pagelets_displayed:null},this.lid=c("pageID")+":"+j++,this.extras={}}var b=a.prototype;b.getLID=function(){return this.lid};b.setRequestStart=function(a){this.start=a;return this};b.setTTI=function(a){this.eventTimings.tti=a;this.$1(i.tti,a);return this};b.setE2E=function(a){this.eventTimings.e2e=a;this.$1(i.e2e,a);return this};b.setExtra=function(a,b){this.extras[a]=b;return this};b.setDisplayDone=function(a){this.eventTimings.all_pagelets_displayed=a;this.setExtra("all_pagelets_displayed",a);this.$1(i.all_pagelets_displayed,a);return this};b.setAllPageletsLoaded=function(a){this.eventTimings.all_pagelets_loaded=a;this.setExtra("all_pagelets_loaded",a);this.$1(i.all_pagelets_loaded,a);return this};b.setServerLID=function(a){this.serverLID=a;return this};b.$1=function(a,b){var c={};k!=null&&this.serverLID!=null&&k[this.serverLID]!=null&&(c=k[this.serverLID]);c=babelHelpers["extends"]({},c,{event:a,timestamp:b});m.emitAndHold(h.EVENT_OCCURRED,this.serverLID,c);return this};b.doneNavigation=function(){var a=babelHelpers["extends"]({start:this.start,extras:this.extras},this.eventTimings);if(this.serverLID&&k[this.serverLID]){var b=this.serverLID;Object.assign(a,k[b]);delete k[b]}m.emitAndHold(h.NAVIGATION_DONE,this.lid,a)};return a}(),m={Events:h,postPagelet:function(a,b,c){},siteInit:function(a){a(l)},setPage:function(a){if(!a.serverLID)return;k[a.serverLID]={page:a.page,pageType:a.page_type,pageURI:a.page_uri,serverLID:a.serverLID}},getFullPageLoadLid:function(){throw new Error("getFullPageLoadLid is not implemented on this site")}};c("mixInEventEmitter")(m,h);a=m;g["default"]=a}),98);
__d("NavigationMetrics",["Arbiter","BigPipeInstance","NavigationMetricsCore","PageEvents","performance"],(function(a,b,c,d,e,f,g){var h="0";c("NavigationMetricsCore").getFullPageLoadLid=function(){return h};c("NavigationMetricsCore").siteInit(function(a){var b=new a(),e=!0;c("Arbiter").subscribe(d("BigPipeInstance").Events.init,function(f,g){var i=e?b:new a();e&&(h=g.lid);e=!1;i.setServerLID(g.lid);f=g.arbiter;f.subscribe(d("BigPipeInstance").Events.tti,function(a,b){a=b.ts;i.setTTI(a)});f.subscribe(c("PageEvents").AJAXPIPE_SEND,function(a,b){a=b.ts;i.setRequestStart(a)});f.subscribe(c("PageEvents").AJAXPIPE_ONLOAD,function(a,b){a=b.ts;i.setE2E(a).doneNavigation()});f.subscribe(d("BigPipeInstance").Events.displayed,function(a,b){a=b.ts;i.setDisplayDone(a)});f.subscribe(d("BigPipeInstance").Events.loaded,function(a,b){a=b.ts;i.setAllPageletsLoaded(a)})});c("Arbiter").subscribe(c("PageEvents").BIGPIPE_ONLOAD,function(a,d){a=d.ts;e=!1;b.setRequestStart(c("performance").timing&&c("performance").timing.navigationStart).setE2E(a).doneNavigation()})});g["default"]=c("NavigationMetricsCore")}),98);
__d("FBJSON",[],(function(a,b,c,d,e,f){a=JSON.parse;b=JSON.stringify;f.parse=a;f.stringify=b}),66);
__d("Banzai",["cr:1642797"],(function(a,b,c,d,e,f,g){g["default"]=b("cr:1642797")}),98);
__d("OdsWebBatchFalcoEvent",["FalcoLoggerInternal","getFalcoLogPolicy_DO_NOT_USE"],(function(a,b,c,d,e,f){"use strict";a=b("getFalcoLogPolicy_DO_NOT_USE")("1838142");c=b("FalcoLoggerInternal").create("ods_web_batch",a);e.exports=c}),null);
__d("WebStorageMutex",["WebStorage","clearTimeout","pageID","setTimeout"],(function(a,b,c,d,e,f,g){"use strict";var h=null,i=!1,j=c("pageID");function k(){i||(i=!0,h=c("WebStorage").getLocalStorage());return h}a=function(){function a(a){this.name=a}a.testSetPageID=function(a){j=a};var b=a.prototype;b.$2=function(){var a,b=k();if(!b)return j;b=b.getItem("mutex_"+this.name);b=((a=b)!=null?a:"").split(":");return b&&parseInt(b[1],10)>=Date.now()?b[0]:null};b.$3=function(a){var b=k();if(!b)return;a=a==null?1e3:a;a=Date.now()+a;c("WebStorage").setItemGuarded(b,"mutex_"+this.name,j+":"+a)};b.hasLock=function(){return this.$2()===j};b.lock=function(a,b,d){var e=this;this.$1&&c("clearTimeout")(this.$1);j===(this.$2()||j)&&this.$3(d);this.$1=c("setTimeout")(function(){e.$1=null;var c=e.hasLock()?a:b;c&&c(e)},0)};b.unlock=function(){this.$1&&c("clearTimeout")(this.$1);var a=k();a&&this.hasLock()&&a.removeItem("mutex_"+this.name)};return a}();g["default"]=a}),98);
__d("guid",[],(function(a,b,c,d,e,f){function a(){return"f"+(Math.random()*(1<<30)).toString(16).replace(".","")}f["default"]=a}),66);
__d("requestAnimationFrame",["TimeSlice","TimerStorage","requestAnimationFrameAcrossTransitions"],(function(a,b,c,d,e,f,g){function a(a){function b(b){c("TimerStorage").unset(c("TimerStorage").ANIMATION_FRAME,d),a(b)}c("TimeSlice").copyGuardForWrapper(a,b);b.__originalCallback=a;var d=c("requestAnimationFrameAcrossTransitions")(b);c("TimerStorage").set(c("TimerStorage").ANIMATION_FRAME,d);return d}g["default"]=a}),98);
__d("PersistedQueue",["BaseEventEmitter","ExecutionEnvironment","FBJSON","Run","WebStorage","WebStorageMutex","err","guid","nullthrows","performanceAbsoluteNow","requestAnimationFrame"],(function(a,b,c,d,e,f,g){"use strict";var h=24*60*60*1e3,i=30*1e3,j=new(c("BaseEventEmitter"))(),k;function l(){if(k===void 0){var a="check_quota";try{var b=c("WebStorage").getLocalStorage();b?(b.setItem(a,a),b.removeItem(a),k=b):k=null}catch(a){k=null}}return k}function m(a){var b=a.prev,c=a.next;c&&(c.prev=b);b&&(b.next=c);a.next=null;a.prev=null}function n(a){return{item:a,next:null,prev:null}}function o(a,b){return a+"^$"+((a=b==null?void 0:b.queueNameSuffix)!=null?a:"")}var p={},q={},r={},s=!1;a=function(){function a(a,b){var d,e=this;this.$7=0;this.$3=a;this.$5=(d=b==null?void 0:b.queueNameSuffix)!=null?d:"";this.$4=o(a,b);this.$11=this.$4+"^$"+c("guid")();this.$13=!1;if(b){this.$8=(d=b.max_age_in_ms)!=null?d:h;this.$12=b.migrate}else this.$8=h;this.$9=[j.addListener("active",function(){(e.$10!=null||!e.$13)&&(e.$13=!0,e.$10=null,e.$14())}),j.addListener("inactive",function(){e.$10==null&&(e.$10=Date.now(),e.$15())})];(c("ExecutionEnvironment").canUseDOM||c("ExecutionEnvironment").isInWorker)&&c("requestAnimationFrame")(function(){return e.$14()})}var b=a.prototype;b.isActive=function(){var a=this.$10;if(a==null)return!0;if(Date.now()-a>i){this.$10=null;j.emit("active",null);return!0}return!1};b.$14=function(){this.$16(),this.$17()};b.$15=function(){this.$18()};b.getFullName=function(){return this.$4};b.getQueueNameSuffix=function(){return this.$5};a.isQueueActivateExperiment=function(){return s};a.setOnQueueActivateExperiment=function(){s=!0};a.create=function(b,d){var e=o(b,d);if(e in p)throw c("err")("Duplicate queue created: "+b);d=new a(b,d);p[e]=d;r[b]?r[b].push(d):r[b]=[d];e=q[b];e&&d.setHandler(e);return d};a.setHandler=function(a,b){if(r[a]){var c=r[a];for(var c=c,d=Array.isArray(c),e=0,c=d?c:c[typeof Symbol==="function"?Symbol.iterator:"@@iterator"]();;){var f;if(d){if(e>=c.length)break;f=c[e++]}else{e=c.next();if(e.done)break;f=e.value}f=f;f.setHandler(b)}}q[a]=b};b.destroy=function(){this.$9.forEach(function(a){return a.remove()})};a.destroy=function(a,b){a=o(a,b);p[a].destroy();delete p[a]};b.setHandler=function(a){this.$6=a;this.$17();return this};b.$17=function(){this.$7>0&&this.$6&&this.$6(this)};b.length=function(){return this.$7};b.enumeratedLength=function(){return this.$19().length};a.getSuffixesForKey=function(a){var b=[];try{var c=l();if(!c)return b;a=a+"^$";for(var d=0;d<c.length;d++){var e=c.key(d);if(typeof e==="string"&&e.startsWith(a)){e=e.split("^$");if(e.length>2){e=e[1];b.push(e)}else b.push("")}}}catch(a){}return b};b.$16=function(){var b=this;if(this.$5===""){this.$20();return}var a=l();if(!a)return;var e=this.$4+"^$",f=new(c("WebStorageMutex"))(e),g=this.$12;f.lock(function(f){var h=Date.now()-b.$8;for(var i=0;i<a.length;i++){var j=a.key(i);if(typeof j==="string"&&j.startsWith(e)){var k=a.getItem(j);a.removeItem(j);if(k!=null&&k.startsWith("{")){j=d("FBJSON").parse(c("nullthrows")(k));if(j.ts>h)try{for(var k=j.items,j=Array.isArray(k),l=0,k=j?k:k[typeof Symbol==="function"?Symbol.iterator:"@@iterator"]();;){var m;if(j){if(l>=k.length)break;m=k[l++]}else{l=k.next();if(l.done)break;m=l.value}m=m;m=g!=null?g(m):m;b.$21(m)}}catch(a){}}}}f.unlock()})};b.$20=function(){var b=this,a=l();if(!a)return;var e=this.$4,f=new(c("WebStorageMutex"))(e),g=this.$12;f.lock(function(f){var h=Date.now()-b.$8;for(var i=0;i<a.length;i++){var j=a.key(i);if(typeof j==="string"&&j.startsWith(e)){var k=j.split("^$");if(k.length<=2||k[1]===""){k=a.getItem(j);a.removeItem(j);if(k!=null&&k.startsWith("{")){j=d("FBJSON").parse(c("nullthrows")(k));if(j.ts>h)try{for(var k=j.items,j=Array.isArray(k),l=0,k=j?k:k[typeof Symbol==="function"?Symbol.iterator:"@@iterator"]();;){var m;if(j){if(l>=k.length)break;m=k[l++]}else{l=k.next();if(l.done)break;m=l.value}m=m;m=g!=null?g(m):m;b.$21(m)}}catch(a){}}}}}f.unlock()})};b.$18=function(){var a=l();if(!a)return;var b=this.$19();if(b.length===0){a.getItem(this.$11)!=null&&a.removeItem(this.$11);return}c("WebStorage").setItemGuarded(a,this.$11,d("FBJSON").stringify({items:b.map(function(a){return a}),ts:c("performanceAbsoluteNow")()}))};b.$19=function(){var a=this.$1,b=[];if(!a)return b;do b.push(a.item);while(a=a.prev);return b.reverse()};b.markItemAsCompleted=function(a){var b=a.prev;m(a);this.$1===a&&(this.$1=b);this.$7--;this.isActive()||this.$18()};b.markItemAsFailed=function(a){m(a);var b=this.$2;if(b){var c=b.prev;c&&(c.next=a,a.prev=c);a.next=b;b.prev=a}this.$2=a;this.isActive()&&this.$17()};b.markItem=function(a,b){b?this.markItemAsCompleted(a):this.markItemAsFailed(a)};b.$21=function(a){a=n(a);var b=this.$1;b&&(b.next=a,a.prev=b);this.$1=a;this.$2||(this.$2=a);this.$7++};b.wrapAndEnqueueItem=function(a){this.$21(a),this.isActive()?this.$17():this.$18()};b.dequeueItem=function(){if(this.$10!=null)return null;var a=this.$2;if(!a)return null;this.$2=a.next;return a};return a}();a.eventEmitter=j;if(c("ExecutionEnvironment").canUseDOM){var t=d("Run").maybeOnBeforeUnload(function(){j.emit("inactive",null),t==null?void 0:t.remove()},!1);if(!t)var u=d("Run").onUnload(function(){j.emit("inactive",null),u.remove()})}g["default"]=a}),98);
__d("ServerTime",["ServerTimeData"],(function(a,b,c,d,e,f,g){var h,i=0;f=0;var j=null;h=(h=window.performance)==null?void 0:h.timing;if(h){var k=h.requestStart;h=h.domLoading;if(k&&h){var l=c("ServerTimeData").timeOfResponseStart-c("ServerTimeData").timeOfRequestStart;k=h-k-l;f=k/2;l=h-c("ServerTimeData").timeOfResponseStart-f;h=Math.max(50,k*.8);Math.abs(l)>h&&(i=l,j=Date.now())}}else d(c("ServerTimeData").serverTime);function a(){return Date.now()-i}function b(){return i}function d(a){a=Date.now()-a;Math.abs(i-a)>6e4&&(i=a,j=Date.now())}function e(){return j===null?null:Date.now()-j}f=a;k=b;g.getMillis=a;g.getOffsetMillis=b;g.update=d;g.getMillisSinceLastUpdate=e;g.get=f;g.getSkew=k}),98);
__d("isPromise",[],(function(a,b,c,d,e,f){"use strict";function a(a){return!!a&&typeof a.then==="function"}f["default"]=a}),66);
__d("FalcoLoggerInternal",["AnalyticsCoreData","BaseEventEmitter","FBLogger","ODS","PersistedQueue","Random","ServerTime","isPromise","nullthrows","performanceAbsoluteNow","regeneratorRuntime"],(function(a,b,c,d,e,f,g){"use strict";var h=500*1024*.6,i="ods_web_batch",j=new Map();function k(a){"rate"in a&&(a.policy={r:a.rate});var b=a.extra;typeof b!=="string"&&(a.extra=JSON.stringify(b));return a}function a(){var a=c("AnalyticsCoreData").identity;if(a){var b=a.fbIdentity,d=a.appScopedIdentity;a=a.claim;var e="";if(b){var f=b.accountId;b=b.actorId;e=f+"^#"+b+"^#"}else d&&(e="^#^#"+d.appUid);return e+"^#"+a}return""}function e(a,b){var d;d=(d=c("PersistedQueue").getSuffixesForKey(a))!=null?d:[];d.push(b);for(var d=d,e=Array.isArray(d),f=0,d=e?d:d[typeof Symbol==="function"?Symbol.iterator:"@@iterator"]();;){var g;if(e){if(f>=d.length)break;g=d[f++]}else{f=d.next();if(f.done)break;g=f.value}g=g;var h=a+"^$"+g;if(j.has(h))continue;g=c("PersistedQueue").create(a,{migrate:k,queueNameSuffix:g});j.set(h,g)}return c("nullthrows")(j.get(a+"^$"+b))}a=a();var l=e("falco_queue_log",a),m=e("falco_queue_immediately",a),n=e("falco_queue_critical",a),o=new(c("BaseEventEmitter"))();function p(a,b){d("ODS").bumpEntityKey(1344,"falco.fabric.www."+c("AnalyticsCoreData").push_phase,a,b)}function q(a,b,c,e){if(a===i)return;d("ODS").bumpEntityKey(1344,"falco.event."+a,b,c);e&&p(b,c)}function r(a,e,f,g,i){var j,k,l,m,n,p,r,s,t;return b("regeneratorRuntime").async(function(u){while(1)switch(u.prev=u.next){case 0:j=c("Random").coinflip(e.r);if(!(j||c("AnalyticsCoreData").enable_observer)){u.next=29;break}k=c("performanceAbsoluteNow")()-d("ServerTime").getOffsetMillis();if(!j){u.next=28;break}l=g();if(!c("isPromise")(l)){u.next=11;break}u.next=8;return b("regeneratorRuntime").awrap(l);case 8:n=u.sent;u.next=12;break;case 11:n=l;case 12:if(!f){u.next=21;break}p=f();if(!c("isPromise")(p)){u.next=20;break}u.next=17;return b("regeneratorRuntime").awrap(p);case 17:m=u.sent;u.next=21;break;case 20:m=p;case 21:r=JSON.stringify(n);if(!(r.length>h)){u.next=26;break}q(a,"js.drop.oversized_message",1,!0);c("FBLogger")("falco","oversized_message:"+a).warn('Dropping event "%s" due to exceeding the max size %s at %s',a,h,r.length);return u.abrupt("return");case 26:i.wrapAndEnqueueItem({name:a,policy:e,time:k,extra:r,privacyContext:m}),q(a,"js.event.write_to_queue",1,!0);case 28:c("AnalyticsCoreData").enable_observer&&(s=function(){var a;return(a=l)!=null?a:g()},t={name:a,time:k,sampled:j,getData:s,policy:e},f&&(t.getPrivacyContext=function(){var a;return(a=m)!=null?a:f()}),o.emit("event",t));case 29:case"end":return u.stop()}},null,this)}function f(a,b){return{log:function(c,d){r(a,b,d,c,l)},logAsync:function(c,d){r(a,b,d,c,l)},logImmediately:function(c,d){r(a,b,d,c,m)},logCritical:function(c,d){r(a,b,d,c,n)},logRealtimeEvent:function(c,d){r(a,b,d,c,n)}}}g.observable=o;g.create=f}),98);
__d("ODS",["ExecutionEnvironment","OdsWebBatchFalcoEvent","Random","Run","clearTimeout","gkx","setTimeout","unrecoverableViolation"],(function(a,b,c,d,e,f,g){var h,i=c("ExecutionEnvironment").canUseDOM||c("ExecutionEnvironment").isInWorker,j={};function k(a,b,c,d,e){var f;d===void 0&&(d=1);e===void 0&&(e=1);var g=(f=j[b])!=null?f:null;if(g!=null&&g<=0)return;h=h||{};var i=h[a]||(h[a]={}),k=i[b]||(i[b]={}),l=k[c]||(k[c]=[0,null]),n=Number(d),o=Number(e);g>0&&(n/=g,o/=g);if(!isFinite(n)||!isFinite(o))return;l[0]+=n;if(arguments.length>=5){var p=l[1];p==null&&(p=0);l[1]=p+o}m()}var l;function m(){if(l!=null)return;l=c("setTimeout")(function(){n()},c("gkx")("708253")?13e3/2:5e3)}function a(a,b){if(!i)return;j[a]=d("Random").random()<b?b:0}function b(a,b,c,d){d===void 0&&(d=1);if(!i)return;k(a,b,c,d)}function e(a,b,c,d,e){d===void 0&&(d=1);e===void 0&&(e=1);if(!i)return;k(a,b,c,d,e)}function n(a){a===void 0&&(a="normal");if(!i)return;c("clearTimeout")(l);l=null;if(h==null)return;var b=h;h=null;function d(){return{batch:b}}a==="critical"?c("OdsWebBatchFalcoEvent").logCritical(d):c("OdsWebBatchFalcoEvent").log(d)}i&&d("Run").onUnload(function(){n("critical")});g.setEntitySample=a;g.bumpEntityKey=b;g.bumpFraction=e;g.flush=n}),98);
__d("JstlMigrationFalcoEvent",["FalcoLoggerInternal","getFalcoLogPolicy_DO_NOT_USE"],(function(a,b,c,d,e,f){"use strict";a=b("getFalcoLogPolicy_DO_NOT_USE")("1814852");c=b("FalcoLoggerInternal").create("jstl_migration",a);e.exports=c}),null);
__d("getDataWithLoggerOptions",[],(function(a,b,c,d,e,f){"use strict";function a(a,b){return babelHelpers["extends"]({},a,{__options:babelHelpers["extends"]({},{event_time:Date.now()/1e3},b)})}f["default"]=a}),66);
__d("GeneratedLoggerUtils",["invariant","Banzai","JstlMigrationFalcoEvent","getDataWithLoggerOptions"],(function(a,b,c,d,e,f,g){"use strict";var h=window.location.search.indexOf("showlog")>-1;function a(a,c,d,e){var f=b("getDataWithLoggerOptions")(c,e);c=a.split(":")[0];var g=a.split(":")[1];c=="logger"?b("JstlMigrationFalcoEvent").log(function(){return{logger_config_name:g,payload:f}}):b("Banzai").post(a,f,d);h}c={log:a,serializeVector:function(a){if(!a)return a;if(Array.isArray(a))return a;if(a.toArray){var b=a;return b.toArray()}if(typeof a==="object"&&a[typeof Symbol==="function"?Symbol.iterator:"@@iterator"])return Array.from(a);g(0,3874,a)},serializeMap:function(a){if(!a)return a;if(a.toJS){var b=a;return b.toJS()}if(typeof a==="object"&&a[typeof Symbol==="function"?Symbol.iterator:"@@iterator"]){b=a;var c={};for(var b=b,d=Array.isArray(b),e=0,b=d?b:b[typeof Symbol==="function"?Symbol.iterator:"@@iterator"]();;){var f;if(d){if(e>=b.length)break;f=b[e++]}else{e=b.next();if(e.done)break;f=e.value}f=f;c[f[0]]=f[1]}return c}if(Object.prototype.toString.call(a)==="[object Object]")return a;g(0,3875,a)},checkExtraDataFieldNames:function(a,b){Object.keys(a).forEach(function(a){Object.prototype.hasOwnProperty.call(b,a)&&g(0,3876,a)})},warnForInvalidFieldNames:function(a,b,c,d){},throwIfNull:function(a,b){a||g(0,3877,b);return a}};e.exports=c}),null);
__d("Base64",[],(function(a,b,c,d,e,f){var g="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";function h(a){a=a.charCodeAt(0)<<16|a.charCodeAt(1)<<8|a.charCodeAt(2);return String.fromCharCode(g.charCodeAt(a>>>18),g.charCodeAt(a>>>12&63),g.charCodeAt(a>>>6&63),g.charCodeAt(a&63))}var i=">___?456789:;<=_______\0\x01\x02\x03\x04\x05\x06\x07\b\t\n\v\f\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19______\x1a\x1b\x1c\x1d\x1e\x1f !\"#$%&'()*+,-./0123";function j(a){a=i.charCodeAt(a.charCodeAt(0)-43)<<18|i.charCodeAt(a.charCodeAt(1)-43)<<12|i.charCodeAt(a.charCodeAt(2)-43)<<6|i.charCodeAt(a.charCodeAt(3)-43);return String.fromCharCode(a>>>16,a>>>8&255,a&255)}var k={encode:function(a){a=unescape(encodeURI(a));var b=(a.length+2)%3;a=(a+"\0\0".slice(b)).replace(/[\s\S]{3}/g,h);return a.slice(0,a.length+b-2)+"==".slice(b)},decode:function(a){a=a.replace(/[^A-Za-z0-9+\/]/g,"");var b=a.length+3&3;a=(a+"AAA".slice(b)).replace(/..../g,j);a=a.slice(0,a.length+b-3);try{return decodeURIComponent(escape(a))}catch(a){throw new Error("Not valid UTF-8")}},encodeObject:function(a){return k.encode(JSON.stringify(a))},decodeObject:function(a){return JSON.parse(k.decode(a))},encodeNums:function(a){return String.fromCharCode.apply(String,a.map(function(a){return g.charCodeAt((a|-(a>63?1:0))&-(a>0?1:0)&63)}))}};a=k;f["default"]=a}),66);
__d("QueryString",[],(function(a,b,c,d,e,f){function g(a){var b=[];Object.keys(a).sort().forEach(function(c){var d=a[c];if(d===void 0)return;if(d===null){b.push(c);return}b.push(encodeURIComponent(c)+"="+encodeURIComponent(String(d)))});return b.join("&")}function a(a,b){b===void 0&&(b=!1);var c={};if(a==="")return c;a=a.split("&");for(var d=0;d<a.length;d++){var e=a[d].split("=",2),f=decodeURIComponent(e[0]);if(b&&Object.prototype.hasOwnProperty.call(c,f))throw new URIError("Duplicate key: "+f);c[f]=e.length===2?decodeURIComponent(e[1]):null}return c}function b(a,b){return a+(a.indexOf("?")!==-1?"&":"?")+(typeof b==="string"?b:g(b))}c={encode:g,decode:a,appendToUrl:b};f["default"]=c}),66);
__d("SessionName",["SessionNameConfig"],(function(a,b,c,d,e,f){e.exports={getName:function(){return b("SessionNameConfig").seed}}}),null);
__d("isLinkshimURI",["isBulletinDotComURI","isFacebookURI","isMessengerDotComURI"],(function(a,b,c,d,e,f,g){"use strict";function a(a){var b=a.getPath();return(b==="/l.php"||b.indexOf("/si/ajax/l/")===0||b.indexOf("/l/")===0||b.indexOf("l/")===0)&&(c("isFacebookURI")(a)||c("isMessengerDotComURI")(a)||c("isBulletinDotComURI")(a))?!0:!1}g["default"]=a}),98);
__d("routeBuilderUtils",[],(function(a,b,c,d,e,f){"use strict";function a(a){a=a.split("/");return a.filter(function(a){return a!==""}).map(function(a){var b=a.split(/{|}/);if(b.length<3)return{isToken:!1,part:a};else{a=b[0];var c=b[1];b=b[2];var d=c[0]==="?",e=c[d?1:0]==="*";c=c.substring((d?1:0)+(e?1:0));return{isToken:!0,optional:d,catchAll:e,prefix:a,suffix:b,token:c}}})}f.getPathParts=a}),66);
__d("jsRouteBuilder",["ConstUriUtils","FBLogger","routeBuilderUtils"],(function(a,b,c,d,e,f,g){"use strict";var h="#";function a(a,b,e,f,g){g===void 0&&(g=!1);var i=d("routeBuilderUtils").getPathParts(a);function j(j){try{var k=f!=null?babelHelpers["extends"]({},f,j):j,l={};j="";var m=!1;j=i.reduce(function(a,c){if(!c.isToken)return a+"/"+c.part;else{var d,e=c.optional,f=c.prefix,g=c.suffix;c=c.token;if(e&&m)return a;d=(d=k[c])!=null?d:b[c];if(d==null&&e){m=!0;return a}if(d==null)throw new Error("Missing required template parameter: "+c);if(d==="")throw new Error("Required template parameter is an empty string: "+c);l[c]=!0;return a+"/"+f+d+g}},"");a.slice(-1)==="/"&&(j+="/");j===""&&(j="/");var n=d("ConstUriUtils").getUri(j);for(var o in k){var p=k[o];!l[o]&&p!=null&&n!=null&&(e!=null&&e.has(o)?p!==!1&&(n=n.addQueryParam(o,null)):n=n.addQueryParam(o,p))}return[n,j]}catch(b){p=b==null?void 0:b.message;o=c("FBLogger")("JSRouteBuilder").blameToPreviousFrame().blameToPreviousFrame();g&&(o=o.blameToPreviousFrame());o.mustfix("Failed building URI for base path: %s message: %s",a,p);return[null,h]}}return{buildUri:function(a){a=(a=j(a)[0])!=null?a:d("ConstUriUtils").getUri(h);if(a==null)throw new Error("Not even the fallback URL parsed validly!");return a},buildUriNullable:function(a){return j(a)[0]},buildURLStringDEPRECATED:function(a){a=j(a);var b=a[0];a=a[1];return(b=b==null?void 0:b.toString())!=null?b:a},buildURL:function(a){a=j(a);var b=a[0];a=a[1];return(b=b==null?void 0:b.toString())!=null?b:a}}}g["default"]=a}),98);
__d("getCrossOriginTransport",["invariant","ExecutionEnvironment","err"],(function(a,b,c,d,e,f,g){function h(){if(!b("ExecutionEnvironment").canUseDOM)throw b("err")("getCrossOriginTransport: %s","Cross origin transport unavailable in the server environment.");try{var a=new XMLHttpRequest();!("withCredentials"in a)&&typeof XDomainRequest!=="undefined"&&(a=new XDomainRequest());return a}catch(a){throw b("err")("getCrossOriginTransport: %s",a.message)}}h.withCredentials=function(){var a=h();"withCredentials"in a||g(0,5150);var b=a.open;a.open=function(){b.apply(this,arguments),this.withCredentials=!0};return a};e.exports=h}),null);
__d("ZeroRewrites",["URI","ZeroRewriteRules","getCrossOriginTransport","getSameOriginTransport","isFacebookURI"],(function(a,b,c,d,e,f){var g,h={rewriteURI:function(a){if(!b("isFacebookURI")(a)||h._isWhitelisted(a))return a;var c=h._getRewrittenSubdomain(a);c!==null&&c!==void 0&&(a=a.setSubdomain(c));return a},getTransportBuilderForURI:function(a){return h.isRewritten(a)?b("getCrossOriginTransport").withCredentials:b("getSameOriginTransport")},isRewriteSafe:function(a){if(Object.keys(b("ZeroRewriteRules").rewrite_rules).length===0||!b("isFacebookURI")(a))return!1;var c=h._getCurrentURI().getDomain(),d=new(g||(g=b("URI")))(a).qualify().getDomain();return c===d||h.isRewritten(a)},isRewritten:function(a){a=a.getQualifiedURI();if(Object.keys(b("ZeroRewriteRules").rewrite_rules).length===0||!b("isFacebookURI")(a)||h._isWhitelisted(a))return!1;var c=a.getSubdomain(),d=h._getCurrentURI(),e=h._getRewrittenSubdomain(d);return a.getDomain()!==d.getDomain()&&c===e},_isWhitelisted:function(a){a=a.getPath();a.endsWith("/")||(a+="/");return b("ZeroRewriteRules").whitelist&&b("ZeroRewriteRules").whitelist[a]===1},_getRewrittenSubdomain:function(a){a=a.getQualifiedURI().getSubdomain();return b("ZeroRewriteRules").rewrite_rules[a]},_getCurrentURI:function(){return new(g||(g=b("URI")))("/").qualify()}};e.exports=h}),null);
__d("once",[],(function(a,b,c,d,e,f){"use strict";function a(a){var b=g(a);for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&&(b[c]=a[c]);return b}function g(a){var b=a,c;a=function(){if(b){for(var a=arguments.length,d=new Array(a),e=0;e<a;e++)d[e]=arguments[e];c=b.apply(this,d);b=null}return c};return a}f["default"]=a}),66);