## 不蒜子自建后端 API

> 直接用 `demo` 版本 ：https://busuanzi.icodeq.com
> 
> 官网归档地址：https://github.com/zkeq/Busuanzi

### 自己搭建步骤

> 这教程确实奇怪，不过我找不到其他不报错的方法

1. 注册 replit.com

2. 重要：创建一个 `Python` 新项目！

3. 重要：选择模板为 flask ！

4. 重要：点击运行，查看 demo 是否正常运行！(正常运行即可进行下一步)

5. 分别创建文件 `pv.py` `uv.py` `main.py` `get_before_data.py` `white_list.json` 和文件夹 `ips`

6. 复制本项目的文件到上一步创建的文件中（复制上一步提及的就可）

7. 在 `white_list.json` 中添加你的域名白名单

8. 点击 `RUN` 运行再次运行（即成功！）

9. 将 `不蒜子` 官网提供的 `js` 代码里面的网址，改成你的

```javascript
var bszCaller,bszTag;!function(){var c,d,e,a=!1,b=[];ready=function(c){return a||"interactive"===document.readyState||"complete"===document.readyState?c.call(document):b.push(function(){return c.call(this)}),this},d=function(){for(var a=0,c=b.length;c>a;a++)b[a].apply(document);b=[]},e=function(){a||(a=!0,d.call(window),document.removeEventListener?document.removeEventListener("DOMContentLoaded",e,!1):document.attachEvent&&(document.detachEvent("onreadystatechange",e),window==window.top&&(clearInterval(c),c=null)))},document.addEventListener?document.addEventListener("DOMContentLoaded",e,!1):document.attachEvent&&(document.attachEvent("onreadystatechange",function(){/loaded|complete/.test(document.readyState)&&e()}),window==window.top&&(c=setInterval(function(){try{a||document.documentElement.doScroll("left")}catch(b){return}e()},5)))}(),bszCaller={fetch:function(a,b){var c="BusuanziCallback_"+Math.floor(1099511627776*Math.random());window[c]=this.evalCall(b),a=a.replace("=BusuanziCallback","="+c),scriptTag=document.createElement("SCRIPT"),scriptTag.type="text/javascript",scriptTag.defer=!0,scriptTag.src=a,scriptTag.referrerPolicy="no-referrer-when-downgrade",document.getElementsByTagName("HEAD")[0].appendChild(scriptTag)},evalCall:function(a){return function(b){ready(function(){try{a(b),scriptTag.parentElement.removeChild(scriptTag)}catch(c){bszTag.hides()}})}}},bszCaller.fetch("//busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback",function(a){bszTag.texts(a),bszTag.shows()}),bszTag={bszs:["site_pv","page_pv","site_uv"],texts:function(a){this.bszs.map(function(b){var c=document.getElementById("busuanzi_value_"+b);c&&(c.innerHTML=a[b])})},hides:function(){this.bszs.map(function(a){var b=document.getElementById("busuanzi_container_"+a);b&&(b.style.display="none")})},shows:function(){this.bszs.map(function(a){var b=document.getElementById("busuanzi_container_"+a);b&&(b.style.display="inline")})}};
```

```
//busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback
改成
你的域名，例如：
https://counter.busuanzi.icodeq.com/?jsonpCallback=BusuanziCallback
```

10. 将第九步替换后的 `js` 代码替换为你正在使用的即可

出现下图表示安装成功！


![7fb1645befad5bbbff33a6578eef0a50](https://user-images.githubusercontent.com/62864752/163296339-168c05ad-dc10-48c8-a046-1c8e46635681.png)
