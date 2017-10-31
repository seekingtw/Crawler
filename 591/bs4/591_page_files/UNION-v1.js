function Union(t){var e=this;if(!(this instanceof Union))return new Union(t);e.defaults={pid:"",kid:0,callback:null,isCreatImg:!0,regionid:getCookie("urlJumpIp")},t=t||{};for(var n in t)t.hasOwnProperty(n)&&(e.defaults[n]=t[n]);var r="callback=unionName_"+e.defaults.pid+"&pid="+e.defaults.pid+"&regionid="+e.defaults.regionid;e.scriptUrl=ENV.PROXY+"/advert?"+r,e.init()}function getCookie(t){if(document.cookie.length>0){var e=document.cookie.indexOf(t+"=");if(-1!==e){e=e+t.length+1;var n=document.cookie.indexOf(";",e);return-1===n&&(n=document.cookie.length),decodeURIComponent(document.cookie.substring(e,n))}}return""}!function(t){function e(t,e){return function(){t.apply(e,arguments)}}function n(t){if("object"!=typeof this)throw new TypeError("Promises must be constructed via new");if("function"!=typeof t)throw new TypeError("not a function");this._state=null,this._value=null,this._deferreds=[],c(t,e(i,this),e(o,this))}function r(t){var e=this;if(null===this._state)return void this._deferreds.push(t);l(function(){var n=e._state?t.onFulfilled:t.onRejected;if(null===n)return void(e._state?t.resolve:t.reject)(e._value);var r;try{r=n(e._value)}catch(e){return void t.reject(e)}t.resolve(r)})}function i(t){try{if(t===this)throw new TypeError("A promise cannot be resolved with itself.");if(t&&("object"==typeof t||"function"==typeof t)){var n=t.then;if("function"==typeof n)return void c(e(n,t),e(i,this),e(o,this))}this._state=!0,this._value=t,a.call(this)}catch(t){o.call(this,t)}}function o(t){this._state=!1,this._value=t,a.call(this)}function a(){for(var t=0,e=this._deferreds.length;t<e;t++)r.call(this,this._deferreds[t]);this._deferreds=null}function u(t,e,n,r){this.onFulfilled="function"==typeof t?t:null,this.onRejected="function"==typeof e?e:null,this.resolve=n,this.reject=r}function c(t,e,n){var r=!1;try{t(function(t){r||(r=!0,e(t))},function(t){r||(r=!0,n(t))})}catch(t){if(r)return;r=!0,n(t)}}var l="function"==typeof setImmediate&&setImmediate||function(t){setTimeout(t,1)},s=Array.isArray||function(t){return"[object Array]"===Object.prototype.toString.call(t)};n.prototype.catch=function(t){return this.then(null,t)},n.prototype.then=function(t,e){var i=this;return new n(function(n,o){r.call(i,new u(t,e,n,o))})},n.all=function(){var t=Array.prototype.slice.call(1===arguments.length&&s(arguments[0])?arguments[0]:arguments);return new n(function(e,n){function r(o,a){try{if(a&&("object"==typeof a||"function"==typeof a)){var u=a.then;if("function"==typeof u)return void u.call(a,function(t){r(o,t)},n)}t[o]=a,0==--i&&e(t)}catch(t){n(t)}}if(0===t.length)return e([]);for(var i=t.length,o=0;o<t.length;o++)r(o,t[o])})},n.resolve=function(t){return t&&"object"==typeof t&&t.constructor===n?t:new n(function(e){e(t)})},n.reject=function(t){return new n(function(e,n){n(t)})},n.race=function(t){return new n(function(e,n){for(var r=0,i=t.length;r<i;r++)t[r].then(e,n)})},n._setImmediateFn=function(t){l=t},n.prototype.always=function(t){var e=this.constructor;return this.then(function(n){return e.resolve(t()).then(function(){return n})},function(n){return e.resolve(t()).then(function(){throw n})})},"undefined"!=typeof module&&module.exports?module.exports=n:t.Promise||(t.Promise=n)}(this);var REGION=[];REGION[1]={id:1,txt:"台北市"},REGION[3]={id:3,txt:"新北市"},REGION[6]={id:6,txt:"桃園市"},REGION[4]={id:4,txt:"新竹市"},REGION[5]={id:5,txt:"新竹縣"},REGION[21]={id:21,txt:"宜蘭縣"},REGION[2]={id:2,txt:"基隆市"},REGION[8]={id:8,txt:"台中市"},REGION[10]={id:10,txt:"彰化縣"},REGION[14]={id:14,txt:"雲林縣"},REGION[7]={id:7,txt:"苗栗縣"},REGION[11]={id:11,txt:"南投縣"},REGION[17]={id:17,txt:"高雄市"},REGION[15]={id:15,txt:"台南市"},REGION[12]={id:12,txt:"嘉義市"},REGION[13]={id:13,txt:"嘉義縣"},REGION[19]={id:19,txt:"屏東縣"},REGION[22]={id:22,txt:"台東縣"},REGION[23]={id:23,txt:"花蓮縣"},REGION[24]={id:24,txt:"澎湖縣"},REGION[25]={id:25,txt:"金門縣"},REGION[26]={id:26,txt:"連江縣"};var ENV={NODE_ENV:"online",PROXY:"//union.591.com.tw"},regionid=getCookie("urlJumpIp"),token=getCookie("T591_TOKEN"),REGION_TXT=REGION[regionid].txt;window.UNION_SHOW=Union,Union.prototype={init:function(){var t=this;this.getScript(t.scriptUrl,function(){}),t.callbackFun()},createImg:function(t){var e={src:t.src||"",alt:t.alt||"",data:t.data||null};return new Promise(function(t,n){var r=new Image;r.onload=function(){t(r)},r.onerror=function(){n(new Error("Could not load image at "+e.src))},r.src=e.src})},creatHTML:function(t){var e=this;return new Promise(function(n,r){e.createImg({src:t.img}).then(function(r){e.hotEventSend(e.getGAString(t.position_name,t.order_number,1));var i=e.createLink({href:t.event_click_url+"&_u="+token,title:t.txt,target:!0,attrValue:e.getGAString(t.position_name,t.order_number)});i.appendChild(r),i.appendChild(e.createStatImg(t.event_show_url)),n(i)})})},createStatImg:function(t){var e=document.createElement("div");return e.className="statImg",e.innerHTML='<img src="'+t+"&_u="+token+'" style="display:none"/>',e},createLink:function(t){var e={href:t.href||"javascript:;",title:t.title||"",target:t.target||!0,attrName:t.attrName||"data-gtm-stat",attrValue:t.attrValue||"UnionEvent_缺省_"+t.title},n=document.createElement("a");return n.setAttribute(e.attrName,e.attrValue),n.href=e.href,n.target="_blank",n},createManyHTML:function(t,e){for(var n=this,r=n.regroup(t,"row"),i=0;i<r.length;i++){var o=r[i],a=n.random(0,o.items.length-1);!function(t){n.creatHTML(o.items[a]).then(function(n){document.getElementById(e+t).innerHTML=n.outerHTML})}(o.name)}},callbackFun:function(){var t=this;window["unionName_"+t.defaults.pid]=function(e){var n=t.defaults.kid?e.data[t.defaults.kid]:e.data;if(t.defaults.callback&&t.defaults.callback.call(t,n),t.defaults.isCreatImg){var r=e.data[t.defaults.kid],i=r.length,o=t.random(0,i-1);i>0?t.creatHTML(r[o]).then(function(e){document.getElementById("UNION_"+t.defaults.pid).innerHTML=e.outerHTML}):document.getElementById("UNION_"+t.defaults.pid).innerHTML=""}window["unionName_"+t.defaults.pid]=null}},hotEventSend:function(t){try{hotEventSend(t)}catch(n){var e=t.split("_");dataLayer.push({event:"public_hot_event",hot_event_1:e[0],hot_event_2:e[1],hot_event_3:e[2],hot_event_4:e[3]})}},getGAString:function(t,e,n){return(1===n?"廣告瀏覽-Union":"廣告點擊-Union")+"_"+REGION_TXT+"-"+t+"_"+(e||1)},random:function(t,e){return parseInt(Math.random()*(e-t+1)+t,10)},getNumberArray:function(t){for(var e=[],n=0;n<t;n++)e.push(n);return e},shuffle:function(t){return t.sort(function(){return Math.random()>.5?-1:1})},getScript:function(t,e){var n=document.createElement("script");n.type="text/javascript",n.src=t,n.onload=n.onreadystatechange=function(){this.readyState&&"loaded"!==this.readyState&&"complete"!==this.readyState||(this.onload=this.onreadystatechange=null,this.parentNode.removeChild(this)),e&&e()},document.getElementsByTagName("head")[0].appendChild(n)},regroup:function(t,e){for(var n=[],r={},i=0,o=0,a=t.length;o<a;o++){var u=t[o];r.hasOwnProperty(u[e])?n[r[u[e]]].items.push(u):(r[u[e]]=i++,n.push({name:u[e],items:[u]}))}return n}};