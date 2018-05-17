var requestTimes = 0;

function weixinDefaultLogin() {
        var isWeixin = 0;
        var ua = window.navigator.userAgent.toLowerCase();
        if (ua.match(/MicroMessenger/i) == 'micromessenger') {
                isWeixin = 1;
        }
        rpcJSON('getWxLoginUrl', {}, function(backData) {
                if (isWeixin) {
                        window.location.href = backData;
                } else {
                        setTimeout(checkDefaultWxLogin, 3000);
                        var str = '<div style="text-align:center; height:230px;z-index:169999;">请使用微信扫描二维码登录<br /><br /><img src="http://tuweia.cn/api/qrcode.php?level=H&size=8&data=' + backData + '"  width="180" /></div>';
                        Alert(str, function() {
                                $.cookie('randomCode', null, {path: '/'});
                        });
                }
        }, function() {
                Alert('登录链接获取失败');
        }, accountRpcURL);
}
;

function checkDefaultWxLogin() {
        var randomCode = $.cookie('randomCode');
        if (!randomCode) {
                return;
        }
        if (requestTimes > 100) {
                window.location.reload();
                return;
        }
        var signinBack = $.cookie('signinBack') || $.cookie('php_signinBack') || beforeUrl || '/c/default/a/view/ac/account';
        $.getJSON(accountAjaxURL, {"action": "checkWxLogin", "keyCode": randomCode}, function(backData) {
                if (backData.code == 0) {
                        Tips('success', '登录成功，正在为您跳转', 1500, function() {
                                $.cookie('signinBack', null);
                                $.cookie('randomCode', null);
                                window.location.href = signinBack;
                        });
                } else {
                        requestTimes++;
                        setTimeout(checkDefaultWxLogin, 3000);
                }
        });
}


