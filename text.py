from top_post_bot import *
from twilio.rest import Client
from credentials import *

#accounts_sid, auth_token, to_phone, and from_phone are references to the valuesin credentials.py

client = Client(account_sid, auth_token)

main()

message = ""
message = ", \n".join(mylist)

client.messages.create(
    to=to_phone,
    from_=from_phone,
    body=message,
    # media_url="https://cdn.psychologytoday.com/sites/default/files/styles/article-inline-half/public/field_blog_entry_images/matrix-1460603554sdB.jpg?itok=1Xt3ImBP"
)