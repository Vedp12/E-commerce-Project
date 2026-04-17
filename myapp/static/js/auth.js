(function(window){
  window.auth = window.auth || {};
  auth.setUserData = function(user){
    try { localStorage.setItem('UserData', JSON.stringify(user)); } catch(e) { }
  };
  auth.getUserData = function(){
    try { return JSON.parse(localStorage.getItem('UserData') || 'null'); } catch(e) { return null; }
  };
  auth.clearUserData = function(){ try { localStorage.removeItem('UserData'); } catch(e) { } };
  auth.requireAuth = function(){
    if (!auth.getUserData()){
      var params = new URLSearchParams();
      params.set('msg', 'Please login to continue');
      window.location.href = '/login/?' + params.toString();
    }
  };
  auth.redirectIfAuthenticated = function(){
    if (auth.getUserData()){
      window.location.href = '/home';
    }
  };
  window.setUserData = auth.setUserData;
  window.getUserData = auth.getUserData;
  window.clearUserData = auth.clearUserData;
  window.requireAuth = auth.requireAuth;
  window.redirectIfAuthenticated = auth.redirectIfAuthenticated;
})(window);
