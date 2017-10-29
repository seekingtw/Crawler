/* global ActiveXObject */
/*
 *  tw591 public JS 
 *  author      yulei@addcn.com
 *  updateTime  2017-08-04
*/
var tw591 = {

    // ajax請求方法
    ajax: function (params) {
        params = params || {};
        params.cache = params.cache || false;
        if (!params.url) {
            throw new Error('参数不合法');
        }
        params.dataType = (params.dataType || 'json').toLowerCase();
        this.ajaxJSON(params);
    },

    /**
    * 通过JSON的方式请求
    * @param  {[type]} params [description]
    * @return {[type]}        [description]
    */
    ajaxJSON: function (params) {
        params.type = (params.type || 'GET').toUpperCase();
        params.data = params.data || {};
        var formatedParams = this.formateParams(params.data, params.cache);
        var xhr;
        // 创建XMLHttpRequest对象
        if (window.XMLHttpRequest) {
            // 非IE6
            xhr = new XMLHttpRequest();
        } else {
            xhr = new ActiveXObject('Microsoft.XMLHTTP');
        }
        // 异步状态发生改变，接收响应数据
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                if (params.success) {
                    if (typeof xhr.responseText === 'string') {
                        params.success(JSON.parse(xhr.responseText));
                    } else {
                        params.success(xhr.responseText);
                    }
                }
            } else {
                params.error && params.error(status);
            }
        }
        xhr.withCredentials = true;

        if (params.type === 'GET') {
            // 连接服务器
            xhr.open('GET', (formatedParams ? params.url + '?' + formatedParams : params.url), true);
            // 发送请求
            xhr.send(null);
        } else {
            // 连接服务器
            xhr.open('POST', params.url, true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            // 发送请求
            xhr.send(formatedParams);
        }
    },

    /**
    * 格式化数据
    * @param  {Obj}     data    需要格式化的数据
    * @param  {Boolean} isCache 是否加入随机参数
    * @return {String}          返回的字符串
    */
    formateParams: function (data, isCache) {
        var arr = [];
        for (var name in data) {
            arr.push(encodeURIComponent(name) + '=' + encodeURIComponent(data[name]));
        }
        if (isCache) {
            arr.push('v=' + (new Date()).getTime());
        }
        return arr.join('&');
    },

    // 與$.cookie用法一致
    cookie: function (key, value, options, issecond) {
        // key and value given, set cookie...
        if (arguments.length > 1 && (value === null || typeof value !== 'object')) {
            if (value === null) {
                options.expires = -1;
            }
            var t = options.expires = new Date();

            if (issecond === true) {
                if (typeof options.expires === 'number') {
                    var seconds = options.expires;
                    t.setTime(t.getTime() + seconds);
                }
            } else {
                if (typeof options.expires === 'number') {
                    var days = options.expires;
                    t.setDate(t.getDate() + days);
                }
            }
            return (document.cookie = [
                encodeURIComponent(key), '=',
                options.raw ? String(value) : encodeURIComponent(String(value)),
                options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
                options.path ? '; path=' + options.path : '',
                options.domain ? '; domain=' + options.domain : '',
                options.secure ? '; secure' : ''
            ].join(''));
        }

        // key and possibly options given, get cookie...
        options = value || {};
        var result;
        var decode = options.raw ? function (s) { return s; } : decodeURIComponent;
        return (result = new RegExp('(?:^|; )' + encodeURIComponent(key) + '=([^;]*)').exec(document.cookie)) ? decode(result[1]) : null;
    },

    /**
     * 执行环境判断
     */
    env: location.host.search('.debug') > -1
        ? 'debug'
        : location.host.search('.dev') > -1
            ? 'dev'
            : ''
}

// 獲取唯一標示
var T591_TOKEN = tw591.cookie('T591_TOKEN');

// 設置唯一token
if (!T591_TOKEN || T591_TOKEN === 'false') {
    var PHPSESSID = tw591.cookie('PHPSESSID');
    tw591.cookie('T591_TOKEN', PHPSESSID || '', {path: '/', expires: 3650, domain: '.591.com.tw'})
}

// 判斷設備
var device = location.hostname === 'm.591.com.tw' ? 'touch' : 'pc';

// 發送請求，統計網站內唯一用戶瀏覽量
tw591.ajax({
    url: '//www.591.com.tw/home/data/clientUniqueCount',
    type: 'post',
    data: {
        title: document.title,
        device: device
    },
    success: function (data) {}
})
