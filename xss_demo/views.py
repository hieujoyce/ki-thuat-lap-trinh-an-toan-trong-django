from django.shortcuts import render
import urllib
#from jinja2 import utils
#str(utils.escape('malicious code here'))
# a = 'Example for escaping.php?name=alert("XSS")'
# print()

# Create your views here.

def security_view(request):
    
    ctx = {
        "className": ""
    }
    if request.method == "POST":
        className = request.POST.dict().get("className")
        ctx["className"] = urllib.parse.quote(className)
    return render(request, 'xss_security.html', ctx)

def not_security_view(request):
    
    ctx = {
        "className": ""
    }
    if request.method == "POST":
        className = request.POST.dict().get("className")
        ctx["className"] = className
    return render(request, 'xss_not_security.html', ctx)

# XSS là một lỗ hổng trong các ứng dụng web cho phép thực thi các tập lệnh
# phía máy khách bất hợp pháp. Và từ quan điểm của kẻ tấn công, tấn công 
# XSS là một kỹ thuật trong đó kẻ tấn công đưa các tập lệnh phía máy khách
# độc hại vào ứng dụng web. Khi người dùng yêu cầu trang bị ảnh hưởng, tập
# lệnh độc hại sẽ được thực thi. Các tác nhân độc hại sử dụng XSS cho nhiều
# mục đích khác nhau, bao gồm các sự cố phổ biến sau: Đánh cắp thông tin 
# nhạy cảm, Hành vi trộm cắp danh tính, Thực thi mã từ xa.

#<script>alert('Xss')</script>
# < is converted to &lt;
# > is converted to &gt;
# ' (single quote) is converted to &#x27;
# " (double quote) is converted to &quot;
# & is converted to &amp;
