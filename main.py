from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import *
from astrbot.api import logger

@register("HD2gl", "灵煞", "绝地潜兵2攻略查询插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.command_group("gl")
    def gl(self):
        pass
    

    @gl.command("help")
    async def help(self, event: AstrMessageEvent):
        chain = [
            Plain("数据日期:25.3.17可使用指令格式如下"),
            Plain("/gl (第一级类) (第二级类)"),
            Plain("第一级类:wq(全部武器),sl(全部手雷),pt(全部炮台),hj(护甲数值详解),zb(非装备类战备),zjz(终结族),jqr(机器人),gnz(光能者)"),
            Plain("终结族第二级类(部分录入):aefzhg(阿尔法指挥官),ccc(穿刺虫),cchw(虫巢护卫),jsqx(巨兽强袭虫),qx(强袭虫和孢子强袭虫),lszl(掠食追猎虫),lszz(掠食追踪虫),sypy(强化酸液喷涌虫),tt(吐酸泰坦),wdc(强化武斗虫),zz(追踪虫),zl(强化追猎虫),jx(尖啸虫)"),
            Plain("机器人第二级类(部分录入):hjzb(火箭纵步者),jx(巨型者),kbz(狂暴者),pt(炮艇),rlz(三种蹂躏者),tkc(三种坦克车),ydgc(移动工厂),ysj(运输舰)"),
            Plain("光能者第二级类(部分录入):jcz(两种监察者),lsq(猎杀器),wpz(肥胖无票者)")
        ]
        yield event.chain_result(chain)

    @gl.command("wq")
    async def wq(self, event: AstrMessageEvent):
        chain = [
            Image.fromFileSystem("./data/plugins/astrbot_plugin_hd2gl/photo/zb/wq1.png"),
            Image.fromFileSystem("./data/plugins/astrbot_plugin_hd2gl/photo/zb/wq2.png"),
            Image.fromFileSystem("./data/plugins/astrbot_plugin_hd2gl/photo/zb/wq3.png")
            ]
        yield event.chain_result(chain)
        
    @gl.command("sl")    
    async def sl(self, event: AstrMessageEvent):  
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zb/sl.png")  
        
    @gl.command("pt")    
    async def pt(self, event: AstrMessageEvent):    
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zb/pt.png")   
        
    @gl.command("hj")    
    async def hj(self, event: AstrMessageEvent):    
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zb/hj.png")  
        
    @gl.command("zb")    
    async def zb(self, event: AstrMessageEvent):    
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zb/zb.png")   
        
    @gl.group("zjz")   
    def zjz():
        pass
    
    @zjz.command("aefzhg") 
    async def aefzhg(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/alfzhg.png") 
        
    @zjz.command("ccc") 
    async def ccc(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/ccc.png")
        
    @zjz.command("cchw") 
    async def cchw(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/cchw.png")
        
    @zjz.command("jsqx") 
    async def jsqx(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/jsqx.png")
        
    @zjz.command("qx") 
    async def qx(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/qx.png")
        
    @zjz.command("lszl") 
    async def lszl(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/lszl.png")
        
    @zjz.command("lszz") 
    async def lszz(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/lszz.png")
        
    @zjz.command("sypy") 
    async def sypy(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/sypy.png")
        
    @zjz.command("tt") 
    async def tt(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/tt.png")
        
    @zjz.command("wd") 
    async def wd(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/wd.png")
        
    @zjz.command("zz") 
    async def zz(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/yszz.png")
        
    @zjz.command("zl") 
    async def zl(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/zl.png")
        
    @zjz.command("jx") 
    async def jx(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/zjz/jx.png")
    
    @gl.group("jqr")
    def jqr():
        pass
    
    @jqr.command("hjzb") 
    async def hjzb(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/jqr/hjzb.png")
        
    @jqr.command("jx") 
    async def jx(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/jqr/jx.png")
        
    @jqr.command("kbz") 
    async def kbz(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/jqr/kbz.png")
        
    @jqr.command("pt") 
    async def pt(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/jqr/pt.png")
        
    @jqr.command("rlz") 
    async def rlz(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/jqr/rlz.png")
        
    @jqr.command("tkc") 
    async def tkc(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/jqr/tkc.png")
        
    @jqr.command("ydgc") 
    async def ydgc(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/jqr/ydgc.png")
        
    @jqr.command("ysj") 
    async def ysj(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/jqr/ysj.png")
        
    @gl.group("gnz")
    def gnz():
        pass    
        
    @gnz.command("jcz") 
    async def jcz(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/gnz/jcz.png")
        
    @gnz.command("lsq") 
    async def lsq(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/gnz/lsq.png")
        
    @gnz.command("wpz") 
    async def wpz(self, event: AstrMessageEvent):
        yield event.image_result("./data/plugins/astrbot_plugin_hd2gl/photo/gnz/wpz.png")                                                                                             