import java.util.*;
public class myRegex{
    public String ip;

    myRegex(String str){
        this.ip=str;
    }
    public boolean isValid(String ip){
        if(ip.split(".").length<3)
            return false;

    }
}