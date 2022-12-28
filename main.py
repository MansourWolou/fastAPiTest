from fastapi import FastAPI
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "hello world "}


@app.get("/fb", response_class=HTMLResponse)
async def fb():
    return """
 <!DOCTYPE html>
    <html>
    <head>
        <title>Document</title>
    </head>
    <body>
        <script>
           window.fbAsyncInit = function () {
    // JavaScript SDK configuration and setup
    FB.init({
      appId:    '1674581429608473', // Facebook App ID git:490051062609782 moi : 1674581429608473
      cookie:   true, // enable cookies
      xfbml:    true, // parse social plugins on this page
      version:  'v15.0' //Graph API version
    });
  };

  // Load the JavaScript SDK asynchronously
  (function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  // Facebook Login with JavaScript SDK
  function launchWhatsAppSignup() {
    // Conversion tracking code
    //fbq && fbq('trackCustom', 'WhatsAppOnboardingStart', {appId: 'your-facebook-app-id', feature: 'whatsapp_embedded_signup'});
    
    // Launch Facebook login
    FB.login(function (response) {
      if (response.authResponse) {
        const accessToken = response.authResponse.accessToken;
        //Use this token to call the debug_token API and get the shared WABA's ID
      } else {
        console.log('User cancelled login or did not fully authorize.');
      }
    }, {
      scope: 'business_management,whatsapp_business_management',
      extras: {
        feature: 'whatsapp_embedded_signup',
        setup: {
        }
      }
    });
  }
          </script>
          <button onclick="launchWhatsAppSignup()" style="background-color: #1877f2; border: 0; border-radius: 4px; color: #fff; cursor: pointer; font-family: Helvetica, Arial, sans-serif; font-size: 16px; font-weight: bold; height: 40px; padding: 0 24px;">Login with Facebook</button>

    </body>
    </html>
    """

#
#    my_app_id = '1674581429608473'
#    my_app_secret = '48cfd23e1e0a1da3d9d2c976280dc5d5'
#    my_access_token = 'EAAXzBd9CYBkBANxarKskzzKWCBsZBOXdEw9GWwiTuUQUZC3rRiLupXKQYH1x7VyYB8NF4lXEUOkAcV5s5fcC3lyulaYZC7RZApZBZB4F9WhZBj6sxNd8ZCRVNs11csTyNV06OQTm39iKFA0n1PpKysqmQmB5iSNHpsFMOr1xc3K6Ioh9EHEPl9zZBv27MWrczkRjOspnT1fvWfrOw2yCtatbCExXPjU85l7wZD'
#    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
#    my_account = AdAccount('act_{{adaccount-id}}')
#    campaigns = my_account.get_campaigns()      
#    print(campaigns)        
#    return {"message" : "gb"}

