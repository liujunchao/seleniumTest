from selenium import webdriver
import time
browser = webdriver.Firefox();
url = "http://ent.sina.com.cn/m/f/2016-05-07/doc-ifxryhhi8476341.shtml"
browser.set_window_size(800,600)
browser.get(url);
browser.execute_script("""
    (function(){
    var y = 0 ;
    var step =100;
    window.scroll(0,0);
    function f() {
        if(y<document.body.scrollHeight){
            y+=step;
            window.scroll(0,y);
            setTimeout(f, 100);

        }else{
            window.scroll(0,0);
            document.title +="scroll-done";
        }
    }
    setTimeout(f,100);
    })();
""");
for i in xrange(60):
    if "scroll-done" in browser.title:
        break
    time.sleep(10)
browser.save_screenshot("ent1.png")
browser.close();
