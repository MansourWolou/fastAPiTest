
function Deferred() {
    var self = this;
    this.promise = new Promise(function (resolve, reject) {
        self.reject = reject
        self.resolve = resolve
    })
}
window.fbLoaded = (new Deferred());

window.fbAsyncInit = function () {
    // JavaScript SDK configuration and setup
    FB.init({
        appId: '1674581429608473', // Facebook App ID
        cookie: true, // enable cookies
        xfbml: true, // parse social plugins on this page
        version: 'v15.0' //Graph API version
    });

    window.fbLoaded.resolve();
};
// Load the JavaScript SDK asynchronously
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    console.log("ok");
    js.src = "https://connect.facebook.net/en_US/sdk.js";

    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

fbLoaded.promise.then(() => { 
    //console.log(fbq);
    // Facebook Login with JavaScript SDK
    function launchWhatsAppSignup() {
        // Conversion tracking code
        //fbq && fbq('trackCustom', 'WhatsAppOnboardingStart', { appId: 'your-facebook-app-id', feature: 'whatsapp_embedded_signup' });

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
                     // Prefilled data can go here
          }
            }
        });
    }
    let button = document.querySelector('#flow')
    button.addEventListener("click",launchWhatsAppSignup())
})
