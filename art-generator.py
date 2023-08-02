from ascii_magic import AsciiArt
from colorama import Fore
import requests

logo = """
 QQQQKQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQKQQQQ
5QQAQQxQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQxQQAQQ5
Q QQwQQ8QQQQQQQQQQQQQQX?          ?XQQQQQQQQQQQQQQ8QQ2QQ Q
QQ QQAQQQ QQQQQQQQ?                    *QQQQQQQQ QQQAQQ QQ
QQQQAQX2QQQ RQQ     i{^ssssssssssss/sv     QQR QQQ5XQAQQQQ
QQQQh QQWQRQQQ?   sssss%ssssssssss%sssss   *QQQRQWQQ SQQQQ
QQQQQQ  QRQQQQQ#vssssssssssssssssssssssssvLQQQQQRQ  QQQQQQ
QQQQQQQ  QRQAQQ s<{ssssssssssssssssssss{<{ QQAQRQ  QQQQQQQ
QQQQQQQA   QQQ {rsssssssssssssssssssssss{r{ QQQ   AQQQQQQQ
QQQQQQ ss   Q%{>ssssssssssssssssssssssssss>{%Q   s{ QQQQQQ
QQQQQ {*ss >{ss\ssssssssssssssssssssssssss){s{> ss*{ QQQQQ
QQQQQss{css.sss:ssssssssssssssssssssssssss:sss sscs{sQQQQQ
QQQQQQ=s%s iss{\ssssssssssssssssssssssssssi{s{v s%s=QQQQQQ
QQQQQQ sss:ss<sssssssssss{ssssssssssssssss{s<ss:sss QQQQQQ
QQQQQQ +sssv ssssssssss{\*ssssss*<{sssssssss{ v*ss+ QQQQQQ
QQQQQQQ:s'sssQ      x!   lssssssr   !x      Qsss's:RQQQQQQ
QQQQQQQ ss ss%QQQQQQQQQRx {ssss{ xRQQQQQQQQQ%ss {s QQQQQQQ
QQQQQQQ)sr sssss-  \\ %{s-sssss{'ss% \\  -sssss rscQQQQQQQ
QQQQQQQ s\s *sssssssssss{*{sssss*{sssssssssss* s\s QQQQQQQ
QQQQQQQQQ ss* sss^ {^<cssssssssssssx>^{ ^sss *ss QQQQQQQQQ
QQQQQQQQ ssss{{*%ss'{ssssssssssssss{{{'ss%*{{ssss QQQQQQQQ
QQQQQQQQ  sss*s{lc+{{*  ssssssssss  *{{/%rss*sss  QQQQQQQQ
QQQQQQQQQw {sssss{crs{sss cssssr sss{srcs*sss{{ wQQQQQQQQQ
QQQQQQQQQQQ" ss si{+soesssssss{sss{eLs^{is ss =QQQQQQQQQQQ
QQQQQQQQQQQQQ  s s  {LQw *{{{s{{* wQLs  s s  QQQQQQQQQQQQQ
QQQQQQQQQQQQQQQ   *KQ?RQLQQ#='#QQ#QR?RK*   QQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQ  ->{ QQQLQQQQQQLQQQ s>-  QQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQ  s^s eQ QQAQQQ Qe s,s  QQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQ +ss - %{ss{s{% - ss+ QQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQ +{ssssss{{ssssss{+ QQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQQ       !!       QQQQQQQQQQQQQQQQQQQQQ
     
          ¡𝒊|¹𝒊¡¡𝒊¹|𝒊¡, 𝗔𝗥𝗧 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ,¡𝒊|¹𝒊¡¡𝒊¹
"""

print (Fore.LIGHTMAGENTA_EX+logo)


def artGenerator(imageUrl, monochromeState, columnsReceived):
    columnsNumber =  int(columnsReceived)
    output =  AsciiArt.from_url(imageUrl).to_ascii(monochrome=monochromeState, columns=columnsNumber)
    print(output)
    # art generator    
def main():
    monochromeState =  False
    imageUrl =  str(input("Enter image Url :\n » "))
    
    monochrome =  str(input("\n» Deactivate Monochrome (colors) ? Y/N  :  "))
    if monochrome=="y" or monochrome=="Y":
     monochromeState = True  
     
    elif monochrome == "n" or monochrome=="N":
        monochrome= False
    else:
        print("Error! Invalid Option")
        return    

    columns = input("\n» Columns Number :  (recommended 70 or 80) \n» ")
    try :
     columnsIsNumber =  int(columns)
     if columnsIsNumber:
         pass
    except Exception as e:
       print("Error! Is not a number")
       return
        
    try:
      imageExists = requests.get(imageUrl)
      if imageExists.status_code == 200:
       artGenerator(imageUrl, monochromeState, columns)            
    except Exception as e :
      print("Image not Found")

if __name__ ==  "__main__":
    main()