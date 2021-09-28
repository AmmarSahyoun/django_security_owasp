document.body.style.color = '#bbb';
document.body.style.textTransform = 'capitalize';
document.body.style.backgroundSize = "cover";

var div = document.createElement('div');
div.style.background = "rgba(0,0,0,0.7)";
div.style.width = '300px';
div.style.margin = '50px auto';
div.style.padding = '10px';
div.style.borderRadius = '10px';

var log = document.createElement('div');
log.style.padding = "5px";
log.style.textAlign = "center";
log.innerHTML = 'login';
log.style.color = '#bbb';
div.appendChild(log);

var inputCss = "background:none;border-color:#666;border-width:0 0 1px 0;width:100%;color:#eee;padding:5px;margin:5px;",
    btnCss = "background:darkred;border:none;width:100%;color:#eee;padding:5px;margin:5px;",

var loginForm = document.createElement('form');
loginForm.innerHTML = "<label>Email</label><br/>" + 
                 "<input type='text' style='"+ inputCss +"' /><br/>" + 
                 "<label>Password</label><br/>" + 
                 "<input type='password' style='"+ inputCss +"' /><br/>" + 
                 "<input type='submit' value='Login' style='"+ btnCss +"' />";
div.appendChild(loginForm);

document.body.appendChild(div);