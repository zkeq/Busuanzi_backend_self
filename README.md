## 不蒜子自建后端 API

> 直接用 `demo` 版本 ：https://busuanzi.icodeq.com
> 
> 官网归档地址：https://github.com/zkeq/Busuanzi

### 安装

##### 个人版

- 点击：[![Run on Replit](https://replit.com/badge/github/zkeq/Busuanzi_backend_self)](https://replit.com/github/zkeq/Busuanzi_backend_selfl)

  本项目仅占用 50MB 内存，个人版完全够用

##### 教育版 or 专业版

> 【资源额度更高，但好像无法一键导入】

1. 创建新项目

2. 复制本项目的文件到上一步创建的项目中

出现下图表示安装成功！


![7fb1645befad5bbbff33a6578eef0a50](https://user-images.githubusercontent.com/62864752/163296339-168c05ad-dc10-48c8-a046-1c8e46635681.png)

### 使用

1. 在 `white_list.json` 中添加你的域名白名单

2. 将 `不蒜子` 官网提供的 `js` 代码里面的网址，改成你的 **即可**



```javascript
//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js

var bszCaller,bszTag;!function(){var c,d,e,a=!1,b=[];ready=function(c){return a||"interactive"===document.readyState||"complete"===document.readyState?c.call(document):b.push(function(){return c.call(this)}),this},d=function(){for(var a=0,c=b.length;c>a;a++)b[a].apply(document);b=[]},e=function(){a||(a=!0,d.call(window),document.removeEventListener?document.removeEventListener("DOMContentLoaded",e,!1):document.attachEvent&&(document.detachEvent("onreadystatechange",e),window==window.top&&(clearInterval(c),c=null)))},document.addEventListener?document.addEventListener("DOMContentLoaded",e,!1):document.attachEvent&&(document.attachEvent("onreadystatechange",function(){/loaded|complete/.test(document.readyState)&&e()}),window==window.top&&(c=setInterval(function(){try{a||document.documentElement.doScroll("left")}catch(b){return}e()},5)))}(),bszCaller={fetch:function(a,b){var c="BusuanziCallback_"+Math.floor(1099511627776*Math.random());window[c]=this.evalCall(b),a=a.replace("=BusuanziCallback","="+c),scriptTag=document.createElement("SCRIPT"),scriptTag.type="text/javascript",scriptTag.defer=!0,scriptTag.src=a,scriptTag.referrerPolicy="no-referrer-when-downgrade",document.getElementsByTagName("HEAD")[0].appendChild(scriptTag)},evalCall:function(a){return function(b){ready(function(){try{a(b),scriptTag.parentElement.removeChild(scriptTag)}catch(c){bszTag.hides()}})}}},bszCaller.fetch("//busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback",function(a){bszTag.texts(a),bszTag.shows()}),bszTag={bszs:["site_pv","page_pv","site_uv"],texts:function(a){this.bszs.map(function(b){var c=document.getElementById("busuanzi_value_"+b);c&&(c.innerHTML=a[b])})},hides:function(){this.bszs.map(function(a){var b=document.getElementById("busuanzi_container_"+a);b&&(b.style.display="none")})},shows:function(){this.bszs.map(function(a){var b=document.getElementById("busuanzi_container_"+a);b&&(b.style.display="inline")})}};
```

```
把里面的这个链接
//busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback
改成
你的域名，例如：
https://counter.busuanzi.icodeq.com/?jsonpCallback=BusuanziCallback
```

3. 将第九步替换后的 `js` 代码替换为你正在使用的即可

